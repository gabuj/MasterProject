"""
This script processes the mean and RMS velocity data from the DIABLO simulation. It extracts the relevant statistical data, computes time-averaged profiles, and saves the results to text files for further analysis.
"""
import h5py
import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Advanced.get_parameters import *

folder="DataFiles/QLAZ_Re1428"
savefolder="DataFiles/QLAZ_Re1428"

fname = "mean.h5"
filename = f"{folder}/{fname}"

#window for rms calculations
dt=0.03
savestatsint=10
Time_window=6000000
window= int(Time_window/(dt*savestatsint))

# 1. Load the physical statistical data
with h5py.File(filename, "r") as f:
    # Dynamically get all the dataset names (0001, 0002, etc.) and sort them
    dataset_names = (list(f["/statistics"].keys()))
    steps = len(dataset_names)
    
    # Read the first dataset just to find out what 'ny' is dynamically
    first_dataset = f[f"/statistics/{dataset_names[0]}"][:]
    ny = first_dataset.shape[1] 
    
    print(f"Found {steps} time steps and {ny} grid points in y.")
    
    # Pre-allocate array
    data = np.zeros((steps, 18, ny))
    
    # Loop through the actual names in the file
    for i, name in enumerate(dataset_names):
        data[i, :, :] = f[f"/statistics/{name}"][:]
        
print("Data loaded successfully. Array shape:", data.shape)


# 2. Extract Variables
# Since the grid doesn't move, we only need a 1D array for the y-coordinates
y_phys = data[0, 1, :]

time_steps = np.arange(1, steps + 1)
t_phys = time_steps*dt*savestatsint

u_mean=data[:,2,:]
v_mean=data[:,3,:]
w_mean=data[:,4,:]
u_rms=data[:,5,:]
v_rms=data[:,6,:]
w_rms=data[:,7,:]
uv=-data[:,8,:]
uw=data[:,9,:]
wv=data[:,10,:]
dudy=data[:,11,:]
dwdy=data[:,12,:]
p=data[:,13,:]
shear=data[:,14,:]
omega_x=data[:,15,:]
omega_y=data[:,16,:]
omega_z=data[:,17,:]


u_mean=np.mean(u_mean[-window:,:], axis=0)
v_mean=np.mean(v_mean[-window:,:], axis=0)
w_mean=np.mean(w_mean[-window:,:], axis=0)
u_rms=np.mean(u_rms[-window:,:], axis=0)
v_rms=np.mean(v_rms[-window:,:], axis=0)
w_rms=np.mean(w_rms[-window:,:], axis=0)
uv=np.mean(uv[-window:,:], axis=0)

np.savetxt(f"{savefolder}/u_mean.d", np.column_stack((y_phys, u_mean)), header="y umean", comments="")
np.savetxt(f"{savefolder}/u_rms.d", np.column_stack((y_phys, u_rms)), header="y u_rms", comments="")
np.savetxt(f"{savefolder}/v_rms.d", np.column_stack((y_phys, v_rms)), header="y v_rms", comments="")
np.savetxt(f"{savefolder}/w_rms.d", np.column_stack((y_phys, w_rms)), header="y w_rms", comments="")
np.savetxt(f"{savefolder}/uv.d", np.column_stack((y_phys, uv)), header="y uv", comments="")





# # -------------------------------------------------------------
# #uv in time for DNS
# data_name=f"$-<u'v'>_{{x,z}}$"
# # plot only negative uv values, keeping the original array shape
# neg_uv = np.where(uv < 0, uv, 0)
# print(f"Number of negative uv values: {neg_uv.shape}")
# title=f"QLAZ_evolution of {data_name} Profile Across the Channel"
# fig, ax = plt.subplots(figsize=(8, 6))
# contour = ax.contourf(t_phys, y_phys, uv.T, levels=10, cmap="viridis")
# fig.colorbar(contour, ax=ax, label=f"{data_name}", pad=0.12)
# ax.set_title(title, fontsize=14)
# ax.set_xlabel(f"$t$", fontsize=12)
# ax.set_ylabel("$y/h$", fontsize=12)
# # ax.set_xscale("log")  # Standard log scale for wavenumber spectra

# plt.tight_layout()
# plt.show()
# plt.savefig(f"{title}.png", dpi=300)