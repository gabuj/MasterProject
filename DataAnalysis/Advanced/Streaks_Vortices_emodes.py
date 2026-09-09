"""
This script visualizes streaks, streamwise vortices, and eigenmodes from spectral data obtained from the DIABLO simulations.
"""
import h5py
import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Advanced.get_parameters import *

# 1. Load the spectral data
fname="out0016"
folder="DataFiles/QLAZ_Re1428_ShortPeriod"
folder="DataFiles/NoEnergies/NoINSTABILITIES_MinAlpha"
folder="DataFiles/DNS_Re1000_ShortPeriod"

QLAZ=False
Nz_new=100

filename = f"{folder}/{fname}.h5"
x_pos=1


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

data_to_plot = u  # Change this to plot different variables
data_name="u"  # Change this to the name of the variable you're plotting


Ny, Nx, Nz = data_to_plot.shape[1], data_to_plot.shape[2], data_to_plot.shape[0]
x = np.arange(0, Nx)
y = get_phys_y(folder)
z= np.arange(0, Nz)

# Adjust Lx, Lz and the y-stretching to match your DNS setup
x = x*Lx / (Nx-1)  # streamwise
z = z*Lz / (Nz-1)  # spanwise


#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------

#take contour of <u(z,y)>_x TO SHOW STREAKS
u_stavg = np.mean(u, axis=2)
u_stavg = u[:,:, x_pos]

if QLAZ:
    z, u_stavg= expand_spanwise_field(u_stavg, Lz, Nz_new)

title=f"{fname}_streaks"
fig, ax = plt.subplots(figsize=(8, 6))
contour = ax.contour(z, y, u_stavg.T, levels=20, colors='black')
levels = contour.levels
contour_interval = levels[1] - levels[0]
print(f"Contour interval is: {contour_interval}")
# ax.set_title(title, fontsize=14)
ax.set_xlabel(f"z/h", fontsize=12)
ax.set_ylabel(f"y/h", fontsize=12)
plt.show()
plt.savefig(f"{title}.png", dpi=300)


#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------

#take vector field of <v(z,y)>_x TO SHOW STREAMWISE VORTICES
v_stavg = np.mean(v, axis=2)
w_stavg = np.mean(w, axis=2)
v_stavg = v[:,:, x_pos]
w_stavg = w[:,:, x_pos]
if QLAZ:
    z, v_stavg= expand_spanwise_field(v_stavg, Lz, Nz_new)
    z, w_stavg= expand_spanwise_field(w_stavg, Lz, Nz_new)

# DONT PLOT ALL GRIDPOINT VALUES
skip =4
skipy=skip
# 2. Subsample your coordinates and data by taking every 'skip'-th point.
# (Assuming z and y are 1D arrays, and w_stavg.T / v_stavg.T are 2D arrays)
z_sub = z[::skip]
y_sub = y[::skipy]
w_sub = w_stavg.T[::skipy, ::skip]
v_sub = v_stavg.T[::skipy, ::skip]

title=f"{fname}_vortices"
fig, ax = plt.subplots(figsize=(8, 6))
vectorfield = ax.quiver(z_sub, y_sub, w_sub, v_sub, color='black', pivot='mid')
# ax.set_title(title, fontsize=14)
ax.set_xlabel(f"z/h", fontsize=12)
ax.set_ylabel(f"y/h", fontsize=12)

#plot reference vector of magnitude 0.1
ax.quiverkey(vectorfield, X=0.9, Y=1.05, U=0.1, label='0.1', labelpos='E', coordinates='axes')

plt.show()
plt.savefig(f"{title}.png", dpi=300)





#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------

#take contour of u-<u(z,y)>_z TO SHOW EMODES
UMEAN=np.mean(u, axis=(0, 2))  # mean in x and z
u_fluc = u - UMEAN[np.newaxis, :, np.newaxis]  # subtract mean from u to get fluctuations
u_spavg=u_fluc[1,:,:] #take at middle of z-
title=f"eig"
fig, ax = plt.subplots(figsize=(8, 6))
contour = ax.contour(x, y, u_spavg, levels=20, colors='black')
# ax.set_title(title, fontsize=14)
ax.set_xlabel(f"x/h", fontsize=12)
ax.set_ylabel(f"y/h", fontsize=12)
plt.show()
plt.savefig(f"{title}.png", dpi=300)