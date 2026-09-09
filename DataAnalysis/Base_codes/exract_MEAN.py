import h5py
import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Base_codes.get_parameters import *

folder="DataFiles/QLAX_Re1000"

fname = "mean.h5"
filename = f"{folder}/{fname}"

#window for rms calculations
dt=0.05
savestatsint=1
Time_window=10000
window= int(Time_window/(dt*savestatsint))

nu =0.001


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
t_phys = time_steps*dt

u_mean=data[:,2,:]
v_mean=data[:,3,:]
w_mean=data[:,4,:]
u_rms=data[:,5,:]
v_rms=data[:,6,:]
w_rms=data[:,7,:]
uv=data[:,8,:]
uw=data[:,9,:]
wv=data[:,10,:]
dudy=data[:,11,:]
dwdy=data[:,12,:]
p=data[:,13,:]
shear=data[:,14,:]
omega_x=data[:,15,:]
omega_y=data[:,16,:]
omega_z=data[:,17,:]


data_to_plot = w_rms  # Change this to plot different variables
data_name="w_rms"  # Change this to the name of the variable you're plotting

sum = False
data_to_plot2= np.array(dudy)*nu  # Change this to plot different variables
data2_name = "dudy*nu"

phys_target_y = 0.2
#targety is index of physical y closest to target y
target_y = np.argmin(np.abs(y_phys - phys_target_y))



#delete if necessary

# data_to_plot= data_to_plot[:,1:-1]
# data_to_plot2 = data_to_plot2[:,1:-1]
# y_phys =y_phys[1:-1]

# 3. Plotting with Physical Axes
title=f"Evolution of {data_name} Profile"
fig, ax = plt.subplots(figsize=(8, 6))
# Pass time_steps and y_phys to contourf to get physical axes!
contour = ax.contourf(t_phys, y_phys, data_to_plot.T, levels=10, cmap="viridis")
fig.colorbar(contour, ax=ax, label=data_name)
ax.set_title(title, fontsize=14)
ax.set_xlabel("t*Uw_h", fontsize=12)
ax.set_ylabel("y", fontsize=12)

plt.tight_layout()
plt.show()
# plt.savefig(f"{title}.png", dpi=300)


data_to_plot_middle=data_to_plot[:, target_y] 

title=f"{data_name} at y_h = {phys_target_y}"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(t_phys[:window], data_to_plot_middle[:window], label=f"{data_name} at y_h= {phys_target_y}", marker= 'x', color="blue", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("t*Uw_h", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)


# t=time_steps[-1]-1  # Last time step index

data_to_plot_avg=np.mean(data_to_plot[-window:, :], axis=0)  # Average over the last 'window' time steps to get a 1D profile across y at the final time
title=f"{data_name} average over last {Time_window} Uw_h as a function of y_h"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot( y_phys,data_to_plot_avg, label=f"{data_name} at last time step", marker= 'x', color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y_h", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)


if sum == True:

    data_to_plot2_avg=np.mean(data_to_plot2[-window:, :], axis=0)
    data_sum = data_to_plot_avg + data_to_plot2_avg
    title=f"{data_name} + {data2_name} average over last {Time_window} Uw_h"
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot( y_phys,data_sum, label=f"sum of {data_name} and {data2_name} at last time step", marker= 'x', color="red", linewidth=2)
    ax.set_title(title, fontsize=14)
    ax.set_xlabel("y_h", fontsize=12)
    ax.set_ylabel(f"{data_name} + {data2_name}", fontsize=12)
    plt.grid(True, which="both", linestyle=":", alpha=0.5)
    plt.legend(fontsize=11)
    plt.show()
    plt.savefig(f"{title}.png", dpi=300)




#plot urms, vrms and wrms averaged over a few timeteps
U_RMS=np.mean(u_rms[-window:, :], axis=0)  # Take the last time step to get a 1D profile across y at the final time
V_RMS=np.mean(v_rms[-window:, :], axis=0)
W_RMS=np.mean(w_rms[-window:, :], axis=0)
title=f"RMS Values average over last {Time_window} Uw_h"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot( y_phys,U_RMS, label=f"U-RMS", marker= 'x', color="red", linewidth=2)
plt.plot( y_phys,V_RMS, label=f"V-RMS", marker= 'o', color="blue", linewidth=2)
plt.plot( y_phys,W_RMS, label=f"W-RMS", marker= '*', color="green", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y_h", fontsize=12)
ax.set_ylabel("RMS Values", fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
# plt.savefig(f"{title}.png", dpi=300)