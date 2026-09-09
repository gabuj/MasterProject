import h5py
import numpy as np
import matplotlib.pyplot as plt

filename = "Temp_DataAnalysis/Files/mean_les.h5"

# 1. Load the physical statistical data
with h5py.File(filename, "r") as f:
    # Dynamically get all the dataset names (0001, 0002, etc.) and sort them
    dataset_names = sorted(list(f["/statistics"].keys()))
    steps = len(dataset_names)
    
    # Read the first dataset just to find out what 'ny' is dynamically
    first_dataset = f[f"/statistics/{dataset_names[0]}"][:]
    ny = first_dataset.shape[1] 
    
    print(f"Found {steps} time steps and {ny} grid points in y.")
    
    # Pre-allocate array
    data = np.zeros((steps, 10, ny))
    
    # Loop through the actual names in the file
    for i, name in enumerate(dataset_names):
        data[i, :, :] = f[f"/statistics/{name}"][:]
        
print("Data loaded successfully. Array shape:", data.shape)


# 2. Extract Variables
# Since the grid doesn't move, we only need a 1D array for the y-coordinates
y_phys = data[0, 1, :] 
time_steps = np.arange(1, steps + 1)

#CHANGE!!!  
u_mean=data[:,2,:]
v_mean=data[:,3,:]
w_mean=data[:,4,:]
u_rms=data[:,5,:]
v_rms=data[:,6,:]
w_rms=data[:,7,:]
uv=data[:,8,:]
uw=data[:,9,:]


data_to_plot = p  # Change this to plot different variables
data_name="omega_x"  # Change this to the name of the variable you're plotting


# 3. Plotting with Physical Axes

title=f"Evolution of {data_name} Profile"
fig, ax = plt.subplots(figsize=(10, 5))
# Pass time_steps and y_phys to contourf to get physical axes!
contour = ax.contourf(time_steps, y_phys, data_to_plot.T, levels=50, cmap="viridis")
fig.colorbar(contour, ax=ax, label=data_name)
ax.set_title(title, fontsize=14)
ax.set_xlabel("Time Step (Save Index)", fontsize=12)
ax.set_ylabel("y", fontsize=12)

plt.tight_layout()
plt.show()
plt.savefig(f"{title}.png", dpi=300)

# title=f"Mean {data_name} Profile"
# fig, ax = plt.subplots(figsize=(10, 5))
# im = plt.imshow(u_mean.T, origin='lower', aspect='auto', cmap='viridis')
# plt.colorbar(im, label='u_mean')
# plt.xlabel('Time Step (Index)')
# plt.ylabel('Y Height (Index)')
# plt.title(title)
# plt.show()
# plt.savefig(f"{title}.png", dpi=300)


data_to_plot_middle=data_to_plot[:, int(ny/2)]  # Take the middle y-index (9) to get a 1D profile across time

title=f"{data_name} at middle y"
fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(time_steps, data_to_plot_middle, label=f"{data_name} at middle y", color="blue", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("Time Step", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)


t=time_steps[-1]-1  # Last time step index
data_to_plot_time=data_to_plot[t, :]  # Take the last time step to get a 1D profile across y at the final time

title=f"{data_name} at last time step"
fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(y_phys, data_to_plot_time, label=f"{data_name} at last time step", color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)