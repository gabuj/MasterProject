import h5py
import numpy as np
import matplotlib.pyplot as plt
from pyevtk.hl import gridToVTK
from AnalysisCode.Base_codes.get_parameters import get_phys_y

# 1. Load the spectral data
fname="LEAST"
folder="DataFiles/QLAX_Re1000_ShortPeriod"

filename = f"{folder}/{fname}.h5"
x_pos=-1

Lx=10.9
Lz=5.5

with h5py.File(filename, "r") as f:
    print("Available datasets in the file:")
    for name in f["/Timestep"]:
        print(f" - {name}")
    # Read the 3D arrays (shape: [Nz, Ny, Nx])
    u = f["/Timestep/U"][:]
    v = f["/Timestep/V"][:]
    w = f["/Timestep/W"][:]
    p= f["/Timestep/P"][:]

    
    print("Data loaded successfully. Array shape:", u.shape)

data_to_plot = v  # Change this to plot different variables
data_name="v"  # Change this to the name of the variable you're plotting


Ny, Nx, Nz = data_to_plot.shape[1], data_to_plot.shape[2], data_to_plot.shape[0]
x = np.arange(0, Nx)
y = get_phys_y(folder)
print(y)
z= np.arange(0, Nz)

# Adjust Lx, Lz and the y-stretching to match your DNS setup
x = x*Lx / Nx  # streamwise
z = z*Lz / Nz  # spanwise


#plot data_to_plot at specific streamwise location (e.g. last point in x)
title=f"{data_name} Profilefff at x={x[x_pos]}"
data_to_plot_x = data_to_plot[:, :, x_pos]  # Select the last point in the x-direction
fig, ax = plt.subplots(figsize=(10, 5))
contour = ax.contourf(z, y, data_to_plot_x.T, levels=10, cmap="YlGnBu_r")
fig.colorbar(contour, ax=ax, label=f"{data_name} at x={x[x_pos]}")
ax.set_title(title, fontsize=14)
ax.set_xlabel("z", fontsize=12)
ax.set_ylabel("y", fontsize=12)
plt.show()
# plt.savefig(f"{title}.png", dpi=300)

#plot data_to_plot spanwise average
#take spanwise average of u
data_to_plot = np.mean(data_to_plot, axis=0)  # Average over the spanwise direction

title=f"{data_name} Profile Across the Channel"
fig, ax = plt.subplots(figsize=(10, 5))
contour = ax.contourf(x, y, data_to_plot[:,:], levels=10, cmap="viridis")
fig.colorbar(contour, ax=ax, label=f"{data_name} (spanwise averaged)")
ax.set_title(title, fontsize=14)
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("y", fontsize=12)
plt.show()
plt.savefig(f"{title}.png", dpi=300)

#take streamwise average of u
data_to_plot_avg = np.mean(data_to_plot, axis=1)

title=f"Streamwise Average {data_name} Profile Across the Channel"
fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(y, data_to_plot_avg, label=data_name, color="blue", marker= 'x', linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_ylabel(f"Streamwise Average {data_name}", fontsize=12)
ax.set_xlabel("y/h", fontsize=12)
plt.show()
# plt.savefig(f"{title}.png", dpi=300)






#----------------------------------------
#WRITE VTK FILE


# --- Define the physical grid coordinates ---
# Couette flow: x=streamwise, y=wall-normal [-1,1], z=spanwise

# --- pyevtk requires Fortran-contiguous (column-major) C-contiguous arrays ---
# Force float64 and contiguous memory layout
def to_vtk_array(arr):
    """Transpose (Nz, Ny, Nx) → (Nx, Ny, Nz) and make Fortran-contiguous float64."""
    return np.asfortranarray(arr.transpose(2, 1, 0), dtype=np.float64)

u_vtk = to_vtk_array(u)
v_vtk = to_vtk_array(v)
w_vtk = to_vtk_array(w)
p_vtk = to_vtk_array(p)
mag_vtk = to_vtk_array(np.sqrt(u**2 + v**2 + w**2))

output_path = f"{folder}/{fname}"

gridToVTK(
    output_path,
    x, y, z,
    cellData={
        # Scalars: pass the array directly (NO tuple wrapping)
        "U":                  u_vtk,
        "V":                  v_vtk,
        "W":                  w_vtk,
        "P":                  p_vtk,
        "velocity_magnitude": mag_vtk,
        # Vector: pass a 3-tuple — enables streamlines/glyphs in ParaView
        "velocity":           (u_vtk, v_vtk, w_vtk),
    },
)

print(f"Written → {output_path}.vtr")
print("are you sure y goes from -1 to 1?")