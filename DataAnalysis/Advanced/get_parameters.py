"""
This module provides functions for analyzing and processing spectral data from DIABLO simulations.
many other code files import this module to access the functions defined here.
"""
from math import tau

import h5py
import numpy as np
import matplotlib.pyplot as plt
dt = 0.05

def get_phys_y(folder):
    # 1. Load the spectral data
    fname="grid"
    filename = f"{folder}/{fname}.h5"
    with h5py.File(filename, "r") as f:
        # Read the 3D arrays (shape: [Nz, Ny, Nx])
        yf = f["/grids/yF"][:]     
    return np.array(yf)


def calculate_normalized_correlation(ei, t, ej=None, normalize_time_by_u_tau=False, u_tau=65*0.001):
    """
    Calculates the normalized correlation function C_ij(tau).
    
    Parameters:
    ei (array-like): The primary data array (e.g., data_to_plot).
    ej (array-like): The secondary data array. If None, 
                               computes the auto-correlation of ei.
                               
    Returns:
    tau (numpy array): Array of time lags.
    c_ij (numpy array): The normalized correlation values.
    """
    print("starting correlation calculation")

    ei = np.asarray(ei)
    
    # If no second signal is provided, compute auto-correlation
    if ej is None:
        ej = ei
    else:
        ej = np.asarray(ej)
        
    if len(ei) != len(ej):
        raise ValueError("Both signals must have the same length.")

    N = len(ei)

    # 1. Extract fluctuations by subtracting the mean
    ei = ei - np.mean(ei)
    ej = ej - np.mean(ej)


    # 1. Calculate the Denominator: sqrt(<Ei^2>) * sqrt(<Ej^2>)
    # < > denotes the time average (mean)
    mean_sq_i = np.mean(ei**2)
    mean_sq_j = np.mean(ej**2)
    denominator = np.sqrt(mean_sq_i) * np.sqrt(mean_sq_j)
    # Prevent division by zero if a signal is perfectly flat at zero
    if denominator == 0:
        raise ValueError("somehow your denominator is zero.")

    # 2. Calculate the Numerator: <Ei(t+tau) * Ej(t)>
    # We divide by N to compute the expectation value (time average).
    cross_corr_sum = np.correlate(ei, ej, mode='full') # modes of np
    numerator = cross_corr_sum / N
    # 3. Final Normalized Correlation
    c_ij = numerator / denominator

    # Generate the corresponding lag array (tau)
    # mode='full' produces lags from -(N-1) to (N-1)
    tau = np.concatenate((-t[:0:-1], t))
    if normalize_time_by_u_tau:
        print("normalised correlation by u_tau")
        tau = tau * u_tau  # Normalize time by friction velocity
    return tau, c_ij

def clean_spectra(data_to_plot, Lx, Lz, ONLYPOSKZ=True, slicemean=True):
    
    if ONLYPOSKZ==False:
        slicemean=False
    Nz, Ny, Nx_half = data_to_plot.shape
    Nx=Nx_half*2

    #KX
    cutoff_kx=Nx // 3 +1

    #KZ
    cutoff_kz = Nz // 3
    TNKZ = 2 * cutoff_kz
    # 1. Extract the blocks
    pos_block = data_to_plot[0 : cutoff_kz + 1, :, :]      # Includes k_z = 0 up to +Nz/3
    neg_block = data_to_plot[cutoff_kz + 1 : TNKZ + 1, :, :] # Includes k_z = -Nz/3 up to -1


    if ONLYPOSKZ:
        data_to_plot = pos_block
        kz = np.arange(0, cutoff_kz + 1)
    else:
        kz = np.arange(-cutoff_kz, cutoff_kz + 1)
        # 2. Stitch them together in monotonic order (-Nz/3 to +Nz/3)
        data_to_plot = np.concatenate((neg_block, pos_block), axis=0)



    if slicemean:
        data_to_plot=data_to_plot[1:, :, 1:cutoff_kx]
        kx = np.arange(1, cutoff_kx)
        kz = np.arange(1, cutoff_kz + 1)
    else:
        data_to_plot=data_to_plot[:, :, :cutoff_kx]
        kx = np.arange(0, cutoff_kx)

    # 2. Scale to physical wavenumbers
    kx = kx * (2.0 * np.pi / Lx)
    kz = kz * (2.0 * np.pi / Lz)
    return data_to_plot, kx, kz



import numpy as np

def expand_spanwise_field(u_zy, Lz, Nz_new):
    """
    Expands a DIABLO streamwise velocity field u(z,y) to a finer spanwise grid.
    
    u_zy   : 2D numpy array of shape (Nz_old, Ny) e.g., (4, 97)
    Lz     : Spanwise domain length (from your DIABLO input.dat)
    Nz_new : Number of points desired in the new z grid
    """
    Nz_old, Ny = u_zy.shape
    
    # 1. Transform to Fourier space along the spanwise direction (axis=0)
    # MUST divide by Nz_old to recover the exact mathematical mode amplitudes
    u_hat = np.fft.fft(u_zy, axis=0) / Nz_old
    
    # Extract the wavenumbers (kz). For Nz_old=4, this returns [0, 1, -2, -1].
    # Note: DIABLO dealiasing means the Nyquist mode (-2) should already be ~0.
    kz_modes = np.fft.fftfreq(Nz_old) * Nz_old
    
    # 2. Define the new, refined physical grid
    z_new = np.linspace(0, Lz, Nz_new, endpoint=False)
    u_expanded = np.zeros((Nz_new, Ny), dtype=float)
    
    # 3. Evaluate the exact Fourier expansion sum
    # u(z, y) = SUM [ u_hat(kz, y) * exp(i * kz * 2*pi/Lz * z) ]
    # This loop is mathematically exact but scales poorly for massive 3D arrays.
    for j in range(Ny):
        for i, z in enumerate(z_new):
            u_val = 0.0 + 0.0j
            for m, kz in enumerate(kz_modes):
                phase = np.exp(1j * kz * (2.0 * np.pi / Lz) * z)
                u_val += u_hat[m, j] * phase
            
            # Hermitian symmetry guarantees the imaginary part is effectively zero.
            # We strictly cast to real to drop the machine-precision imaginary artifacts.
            u_expanded[i, j] = u_val.real
            
    return z_new, u_expanded


def extract_spanwise_eigenmode(u_fluct):
    """
    Extracts the complex eigenmode phi(x,y) for kz = beta from a physical field.
    
    Parameters:
    u_fluct : 3D numpy array of shape (Nx, Ny, Nz) containing the physical fluctuations
              (mean spanwise flow already subtracted).
    Lz      : Spanwise domain length.
    
    Returns:
    phi_xy  : 2D complex numpy array of shape (Nx, Ny) for the kz = beta mode.
    """
    Nz = u_fluct.shape[0]
    
    # 1D Fast Fourier Transform along the z-axis (axis 0)
    # The result is normalized by Nz to give true amplitude coefficients
    u_hat = np.fft.fft(u_fluct, axis=0) / Nz
    
    # In np.fft, index 1 corresponds to the fundamental mode kz = 2*pi/Lz (beta)
    beta_index = 1
    
    # Extract the complex 2D field for the fundamental beta mode
    phi_xy = u_hat[beta_index, :, :]
    
    return phi_xy



def compute_spectral_energy_partition(phi_u, phi_v, phi_w, y_grid):
    """
    Computes the kinetic energy of each k_x harmonic within the k_z = beta eigenmode.
    
    Parameters:
    phi_u, phi_v, phi_w : 2D complex arrays of shape (Nx, Ny) for the beta mode.
    y_grid              : 1D array of length Ny containing wall-normal coordinates.
    
    Returns:
    E_kx                : 1D array of length Nx containing the kinetic energy of each k_x mode.
    """
    Nx = phi_u.shape[1]
    
    # 1. 1D Fast Fourier Transform along the streamwise direction (axis 0)
    # Normalized by Nx to yield true Fourier coefficients
    u_hat_kx = np.fft.fft(phi_u, axis=1) / Nx
    v_hat_kx = np.fft.fft(phi_v, axis=1) / Nx
    w_hat_kx = np.fft.fft(phi_w, axis=1) / Nx
    
    # 2. Compute the kinetic energy density in the (kx, y) plane
    # Energy density = 0.5 * (|u|^2 + |v|^2 + |w|^2)
    # Using np.abs() computes the absolute magnitude of the complex coefficients
    E_density_kx = 0.5 * (np.abs(u_hat_kx)**2 + np.abs(v_hat_kx)**2 + np.abs(w_hat_kx)**2)
    
    # 3. Integrate the energy density across the wall-normal direction (y)
    # This yields the total kinetic energy contained in each k_x harmonic
    # axis=0 corresponds to the Ny dimension
    E_kx = np.trapezoid(E_density_kx, y_grid, axis=0)  # Use trapezoidal integration for better accuracy
    
    return E_kx

def analyze_instability_components(E_kx, Estreak_0, Einstab_0):
    """
    Prints the energy partition between the streak and fundamental instability.
    Assumes standard FFT ordering where index 0 is kx=0, index 1 is kx=alpha.
    """
    E_total = np.sum(E_kx)
    
    # Extract energies based on standard np.fft frequency ordering
    E_streak = E_kx[0]/Estreak_0      # k_x = 0      (0, beta) mode
    E_instab = E_kx[1]/Einstab_0      # k_x = alpha  (alpha, beta) mode
    E_instab2 = E_kx[2]     # k_x = 2alpha (2alpha, beta) mode
    
    print("--- Eigenmode Spectral Energy Partition ---")
    print(f"Total Mode Energy: {E_total:.6e}")
    print(f"Streak (0, beta) Energy Fraction:       {E_streak / E_total * 100:.2f}%")
    print(f"Instability (alpha, beta) Fraction:     {E_instab / E_total * 100:.2f}%")
    # print(f"Instability (2alpha, beta) Fraction:    {E_instab2 / E_total * 100:.2f}%")
    print(f"Ratio (Streak / Fundamental Instab):    {E_streak / E_instab:.2f}")