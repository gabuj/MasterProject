import h5py
import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Base_codes.get_parameters import get_phys_y, clean_spectra

# 1. Load the spectral data
fname="spectra"
folder="Temp_DataAnalysis/Files_KAWAHARA"
folder="Temp_DataAnalysis/Files_Re1000"

filename = f"{folder}/{fname}.h5"

Re_tau=65

Lx=5.513
Lz=3.770

Lx=10.9
Lz=5.5


with h5py.File(filename, "r") as f:
    # Read the 3D arrays (shape: [Nz, Ny, Nx])
    Epp= f["/Spectra/Epp"][:]
    Euu= f["/Spectra/Euu"][:]
    Evv= f["/Spectra/Evv"][:]
    Eww= f["/Spectra/Eww"][:]
    Euv= f["/Spectra/Euv"][:]
    diffx = f["/Spectra/diffx"][:]
    diffy = f["/Spectra/diffy"][:]
    diffz = f["/Spectra/diffz"][:]
    pix = f["/Spectra/pix"][:]
    piy = f["/Spectra/piy"][:]
    piz = f["/Spectra/piz"][:]
    prestransx = f["/Spectra/prestrans"][:]
    prod = f["/Spectra/prod"][:]
    sgsx = f["/Spectra/sgsx"][:]
    sgsy = f["/Spectra/sgsy"][:]
    sgsz = f["/Spectra/sgsz"][:]
    turbtransx = f["/Spectra/turbtransx"][:]
    turbtransy = f["/Spectra/turbtransy"][:]
    turbtransz = f["/Spectra/turbtransz"][:]
    vistransx = f["/Spectra/vistransx"][:]
    vistransy = f["/Spectra/vistransy"][:]
    vistransz = f["/Spectra/vistransz"][:]


    print("Data loaded successfully. Array shape:", prod.shape)


data_to_plot = Euu  # Change this to plot different variables
data_name="Euu"  # Change this to the name of the variable you're plotting
phys_target_y = 0



y = get_phys_y(folder)
data_to_plot, kx, kz = clean_spectra(data_to_plot, Lx, Lz)


#targety is index of physical y closest to target y
target_y = np.argmin(np.abs(y - phys_target_y))

# Integrate or average over the spanwise wavenumbers (axis 0, Nz=288) 
# to get clean 2D planes of (Ny, Nx)
data_to_plot_spavg = np.mean(data_to_plot, axis=0)

# Create the plots
fig, ax = plt.subplots(figsize=(8, 6))
title=f"spanwise-averaged {data_name} Profile Across the Channel"
# -------------------------------------------------------------
# PLOT 1: 2D Contour of Production vs Wall Distance & Wavenumber
# -------------------------------------------------------------
# Use a logarithmic scale or symmetric log if numbers span orders of magnitude
contour = ax.contourf(kx, y, data_to_plot_spavg, levels=10, cmap="viridis")
# ax.set_xscale("log")
fig.colorbar(contour, ax=ax, label=f"{data_name} (spanwise averaged)")
ax.set_title(title, fontsize=14)
ax.set_xlabel("Streamwise Wavenumber ($k_x$)", fontsize=12)
ax.set_ylabel("($y$)", fontsize=12)
plt.show()
# plt.savefig(f"{title}.png", dpi=300)

# -------------------------------------------------------------
# PLOT 2: spanwise-averaged variable at specific y location vs wavenumber
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(kx, data_to_plot_spavg[target_y, :], label=f"{data_name}", marker= 'x', color="black", linewidth=2)
title=f"spanwise-averaged {data_name} at y = {phys_target_y}"
ax.set_title(title, fontsize=14)
ax.set_xlabel(f"($k_x$)", fontsize=12)
ax.set_ylabel(f"spanwise-averaged {data_name}", fontsize=12)
# ax.set_xscale("log")  # Standard log scale for wavenumber spectra
# ax.set_yscale("log")  # Standard log scale for Euu/production

ax.grid(True, which="both", linestyle=":", alpha=0.5)
ax.legend(fontsize=11)
plt.tight_layout()
# plt.savefig("diablo_spectral_analysis.png", dpi=300)
plt.show()
# plt.savefig(f"{title}.png", dpi=300)

# Integrate or average over the streamwise wavenumbers (axis 2) 
# to get clean 2D planes of (Ny, Nz)
data_to_plot_stavg = np.mean(data_to_plot, axis=2)
#create the plots
# -------------------------------------------------------------
# PLOT 3: 2D Contour of Production vs Wall Distance & Spanwise Wavenumber
# -------------------------------------------------------------

title=f"streamwise-averaged {data_name} Profile Across the Channel"
fig, ax = plt.subplots(figsize=(8, 6))
contour = ax.contourf(kz, y, data_to_plot_stavg.T, levels=10, cmap="viridis")
fig.colorbar(contour, ax=ax, label=f"{data_name} (streamwise averaged)")
ax.set_title(title, fontsize=14)
ax.set_xlabel("Spanwise Wavenumber ($k_z$)", fontsize=12)
ax.set_ylabel("($y$)", fontsize=12)
# ax.set_xscale("log")  # Standard log scale for wavenumber spectra
ax.set_xlim(0, kz[4])  # Limit x-axis to positive wavenumbers
plt.show()
plt.savefig(f"{title}.png", dpi=300)

# -------------------------------------------------------------
# PLOT 4: streamwise-averaged variable at specific y location vs spanwise wavenumber
# -------------------------------------------------------------
title=f"streamwise-averaged {data_name} at y = {phys_target_y}"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(kz, data_to_plot_stavg[:, target_y], label=f"{data_name}", marker= 'x', color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel(f"($k_z$)", fontsize=12)
ax.set_ylabel(f"streamwise-averaged {data_name}", fontsize=12)
# ax.set_yscale("log")  # Standard log scale for Euu/production
# ax.set_xscale("log")  # Standard log scale for wavenumber spectra
ax.grid(True, which="both", linestyle=":", alpha=0.5)
ax.legend(fontsize=11)
plt.tight_layout()
plt.show()
# plt.savefig(f"{title}.png", dpi=300)


#--------------------------------------------------------------
#FINAL PLOT of variable at specific y location vs both wavenumbers
# -------------------------------------------------------------

#data at ytarget
z_data = data_to_plot[:, target_y, :]

# # #only plot z_data > 1e-5
# z_data[z_data < -1e-14] = np.nan

title=f"{data_name} at y = {phys_target_y} vs Both Wavenumbers"
fig, ax = plt.subplots(figsize=(8, 6))
contour = ax.contourf(kx, kz, z_data, levels=10, cmap="viridis")
fig.colorbar(contour, ax=ax, label=f"{data_name} at y={phys_target_y}")
ax.set_title(title, fontsize=14)
ax.set_xlabel("Streamwise Wavenumber ($k_x$)", fontsize=12)
ax.set_ylabel("Spanwise Wavenumber ($k_z$)", fontsize=12)
# ax.set_xscale("log")
# ax.set_yscale("log")
plt.show()
# plt.savefig(f"{title}.png", dpi=300)


data_to_plot_integrated= np.sum(data_to_plot, axis=(0, 2))  # Sum over kz and kx
#sum across first and second axis and plot as function of y
title=f"{data_name} integrated over all kx and kz"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(y, data_to_plot_integrated, label=f"{data_name}", marker= 'x', color="black", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel(f"y", fontsize=12)
ax.set_ylabel(f"summed {data_name}", fontsize=12)
ax.grid(True, which="both", linestyle=":", alpha=0.5)
ax.legend(fontsize=11)
plt.tight_layout()
plt.show()
# plt.savefig(f"{title}.png", dpi=300)


#--------------------------------------------------------
#UNDERSTANDING STREAKS AND INSTABILITIES
# streak_energy= Euu[1, :, 0].copy()  # Energy of the k_z=0 mode (streaks) across y
# instability_energy= Euu[1, :, 1].copy()  # Energy of the k_z=1 mode (instability) across y
# mean_energy= Euu[0, :, 0].copy()  # Energy of the k_z=0 mode (mean) across y
# rest_flucs_energy= Euu[2:, :, 2:].sum(axis=(0, 2))  # Sum of all modes except the mean and streaks
# random_energy= Euu[2, :, 0].copy()  # Energy of a random mode (k_z=2, kx=0) across y


# #plot streak, instability and mean energy profiles across y
# title=f"Energy Profiles Across y (kz=2)"
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(y, streak_energy, label=f"Streak Energy (k_z=1, kx=0)", marker= 'x', color="blue", linewidth=2)
# ax.plot(y, instability_energy, label=f"Instability Energy (k_z=1, kx=1)", marker= 'x', color="red", linewidth=2)
# ax.plot(y, random_energy, label=f"Random Energy (k_z=2, kx=0)", marker= 'x', color="orange", linewidth=2)
# # ax.plot(y, rest_flucs_energy, label=f"Rest Fluctuations Energy (k_z>1, kx>1)", marker= 'x', color="green", linewidth=2)
# # ax.plot(y, mean_energy, label=f"Mean Energy (k_z=0, k_x=0)", marker= 'x', color="green", linewidth=2)
# ax.set_title(title, fontsize=14)
# ax.set_xlabel(f"y", fontsize=12)
# ax.set_ylabel(f"Energy", fontsize=12)
# ax.grid(True, which="both", linestyle=":", alpha=0.5)
# ax.legend(fontsize=11)
# plt.tight_layout()
# plt.show()
# plt.savefig(f"{title}.png", dpi=300)    


# #plot streak, instability and mean energy profiles across y
# title=f"Ratio between all flucs and (random) kz=2"
# ratio=rest_flucs_energy / random_energy
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(y, ratio, label=f"ratio between kz=2 energy and rest of fluctuations", marker= 'x', color="blue", linewidth=2)
# ax.set_title(title, fontsize=14)
# ax.set_xlabel(f"y", fontsize=12)
# ax.set_ylabel(f"Energy", fontsize=12)
# ax.grid(True, which="both", linestyle=":", alpha=0.5)
# ax.legend(fontsize=11)
# plt.tight_layout()
# plt.show()
# plt.savefig(f"{title}.png", dpi=300)   