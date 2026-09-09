"""
This script reads 3D velocity data from an output000n file and visualizes the flow field using isosurfaces for the u and v velocity components.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from skimage.measure import marching_cubes
import h5py
from AnalysisCode.Advanced.get_parameters import get_phys_y

# 1. Load the spectral data
fname="end"
folder="DataFiles/DNS_Re1000"

filename = f"{folder}/{fname}.h5"

u_level_image = 0 # in article its -3.2
v_level_image = 1 # in article its 1.4

Re_tau=65.7
nu=0.001
u_tau=nu*Re_tau
print("ARE YOU SURE RE_TAU= ", Re_tau)

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
    p = f["/Timestep/P"][:]

    print("Data loaded successfully. Array shape:", u.shape)

# normalise velocities
u = u / u_tau
v = v / u_tau
w = w / u_tau

Ny, Nx, Nz = u.shape[1], u.shape[2], u.shape[0]
x_vals = np.arange(0, Nx)
y_vals = get_phys_y(folder)
z_vals = np.arange(0, Nz)

# Adjust Lx, Lz and the y-stretching to match your DNS setup
x_vals = x_vals * Lx / Nx  # streamwise
z_vals = z_vals * Lz / Nz  # spanwise

# ==========================================
# 2. Plotting Setup
# ==========================================
fig = plt.figure(figsize=(10, 8)) # Made slightly wider to accommodate the stretched box
ax = fig.add_subplot(111, projection='3d')

def add_isosurface(ax, volume, level, color):
    """
    Extracts an isosurface from a 3D array and adds it to the matplotlib axis,
    safely handling non-uniform grid spacing and axis rotations.
    """
    # Safeguard against the ValueError
    v_min, v_max = volume.min(), volume.max()
    if not (v_min <= level <= v_max):
        auto_level = v_min + (v_max - v_min) * 0.75  
        print(f"Warning: Requested level {level} for {color} is outside data range [{v_min:.3f}, {v_max:.3f}].")
        print(f" -> Automatically adjusting level to {auto_level:.3f}")
        level = auto_level

    # Extract surface using marching cubes
    verts, faces, normals, values = marching_cubes(volume, level=level)

    # volume shape is [Nz, Ny, Nx]
    # verts[:, 0] -> Z-index, verts[:, 1] -> Y-index, verts[:, 2] -> X-index
    phys_z = np.interp(verts[:, 0], np.arange(Nz), z_vals)
    phys_y = np.interp(verts[:, 1], np.arange(Ny), y_vals)
    phys_x = np.interp(verts[:, 2], np.arange(Nx), x_vals)

    # Reorder vertices for Matplotlib plotting to match your requested axes labels:
    # Matplotlib X-axis = Physical Z (Spanwise)
    # Matplotlib Y-axis = Physical X (Streamwise)
    # Matplotlib Z-axis = Physical Y (Wall-normal)
    verts_xyz = np.zeros_like(verts)
    verts_xyz[:, 0] = phys_z 
    verts_xyz[:, 1] = phys_x 
    verts_xyz[:, 2] = phys_y 

    # Create the 3D polygon collection
    mesh = Poly3DCollection(verts_xyz[faces])
    mesh.set_facecolor(color)
    mesh.set_edgecolor('none')     
    mesh.set_alpha(0.8)            
    
    ax.add_collection3d(mesh)

# ==========================================
# 3. Add Surfaces and Configure Axes
# ==========================================
add_isosurface(ax, u, level=u_level_image, color='red')
add_isosurface(ax, v, level=v_level_image, color='deepskyblue')

# Set labels for X and Y only
ax.set_xlabel('z / h')
ax.set_ylabel('x / h')

# Remove the Z-axis ticks, values, and label
ax.set_zticks([])

# --- FIXING THE BOX PROPORTIONS ---
# 1. Force the axes limits to match your physical domain exactly
ax.set_xlim(z_vals.min(), z_vals.max())
ax.set_ylim(x_vals.min(), x_vals.max())
ax.set_zlim(y_vals.min(), y_vals.max())

# 2. Calculate the physical range of each plotted axis
range_plot_x = z_vals.max() - z_vals.min()
range_plot_y = x_vals.max() - x_vals.min()
range_plot_z = y_vals.max() - y_vals.min()

# 3. Apply the aspect ratio
ax.set_box_aspect((range_plot_x, range_plot_y, range_plot_z))
# ----------------------------------

# Adjust the viewing angle 
ax.view_init(elev=45, azim=70)

# Adjust the pane colors to be white with black borders
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')

plt.tight_layout()

# Save MUST come before show()
plt.savefig('3D_flow_field.png', dpi=300)  
plt.show()