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