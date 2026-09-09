"""
This script reads energy data from text files and plots the evolution of various energy components over time.
"""
import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Advanced.get_parameters import calculate_normalized_correlation
#interesting times: DNS: 970-1350 / 64-88 
# QLAZ: 970-1350

file="Euvw_ypm50"
folder="DataFiles/QLAZ_Re1428"
# folder="DataFiles/DNS_Re1000"
# folder="DataFiles/Fixed_Umean/FrozenU_withPert_fromAlpha"
# folder="DataFiles/NoEnergies/NoAlpha"

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman", "Nimbus Roman No9 L", "DejaVu Serif"]

Re_tau=63.0
nu=0.0007
u_tau=nu*Re_tau
dt=0.03
savestatsint=5

TOPENERGYSTREAK=0
TOPENERGYSTREAK_step= int(TOPENERGYSTREAK/(dt*savestatsint))

BOTENERGYSTREAK=0
BOTENERGYSTREAK_step= int(BOTENERGYSTREAK/(dt*savestatsint))




print("ARE YOU SURE RE_TAU= ", Re_tau)
print("ARE YOU SURE dt= ", dt)

t_step,t_phys,Euu_core,Evv_core,Eww_core, E00_core, E11_core, E10_core,_ =np.loadtxt(f"{folder}/{file}_all.d", unpack=True)

E00=E00_core
E11=E11_core
E10=E10_core
# E1m=E1m_bot+E1m_core+E1m_top
Euu=Euu_core
Evv=Evv_core
Eww=Eww_core


#-------------------------------------------------------------------

title=f"evolution_energies_no"
fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(t_phys, E00, label="E0", color="black", linestyle="-", linewidth=2)
ax.plot(t_phys, E10, label="Ex", color="black", linestyle="--", linewidth=2)
# ax.plot(t_phys, E11, label="E1", color="black", linestyle="-.", linewidth=2)
# ax.plot(t_phys, Evv, label="Ev", color="black", linestyle=":", linewidth=2)

ax.set_xlim(0,2000)
# ax.set_ylim(-0.0006, 0.0125)
ax.set_xlabel(f"$tU_{{w}} / h$", fontsize=12)
ax.set_ylabel("Energies", fontsize=12)
#ax.grid(True, which="both", linestyle=":", alpha=0.5)

plt.show()
plt.savefig(f"{title}.png", dpi=300)

#-------------------------------------------------------------------


title=f"alpha instability energies"
fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(t_phys, E00, label="E0", color="black", linestyle="-", linewidth=2)
ax.plot(t_phys, E10, label="Ex", color="black", linestyle="--", linewidth=2)
ax.plot(t_phys, E11, label="E1", color="black", linestyle="-.", linewidth=2)
# ax.plot(t_phys, Evv, label="Ev", color="black", linestyle=":", linewidth=2)

ax.set_xlim(0,300)
# ax.set_ylim(1e-3, 1e23)
ax.set_xlabel(f"$tU_{{w}} / h$", fontsize=12)
ax.set_ylabel("Energies", fontsize=12)
#ax.grid(True, which="both", linestyle=":", alpha=0.5)

plt.show()
# plt.savefig(f"{title}.png", dpi=300)

#-------------------------------------------------------------------

title=f"all energies"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t_phys, E00, label="E0", color="black", linestyle="-", linewidth=2)
ax.plot(t_phys, E10, label="Ex", color="black", linestyle="--", linewidth=2)
ax.plot(t_phys, E11, label="E1", color="black", linestyle="-.", linewidth=2)
ax.plot(t_phys, Eww, label="Ew", color="black", linestyle=":", linewidth=2)

# ax.set_xlim(0,300)
# ax.set_ylim(1e-3, 1e23)
ax.set_xlabel(f"$tU_{{w}} / h$", fontsize=12)
ax.set_ylabel("Energies", fontsize=12)
#ax.grid(True, which="both", linestyle=":", alpha=0.5)

plt.show()
# plt.savefig(f"{title}.png", dpi=300)






#-------------------------------------------------------------------

title=f"linear instability energies"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t_phys, E00, label="E0", color="black", linestyle="-", linewidth=2)
# ax.plot(t_phys, E10, label="Ex", color="black", linestyle="--", linewidth=2)
ax.plot(t_phys, E11, label="E1", color="black", linestyle="-.", linewidth=2)
ax.plot(t_phys, Evv, label="Ev", color="black", linestyle=":", linewidth=2)

ax.set_yscale("log")
ax.set_xlim(0,300)
ax.set_ylim(5e-7, 1e20)
ax.set_xlabel(f"$tU_{{w}} / h$", fontsize=12)
ax.set_ylabel("Energies", fontsize=12)
#ax.grid(True, which="both", linestyle=":", alpha=0.5)

# # --- Inset Plot (Zoomed in for x between 0 and 50) ---
# # The list [x0, y0, width, height] sets the position and size of the inset
# # Coordinates are relative to the main axes (from 0.0 to 1.0)
# axins = ax.inset_axes([0.05, 0.55, 0.4, 0.4]) 

# # Re-plot the exact same data on the inset
# axins.plot(t_phys, E00, color="black", linestyle="-", linewidth=2)
# axins.plot(t_phys, E11, color="black", linestyle="-.", linewidth=2)
# axins.plot(t_phys, Evv, color="black", linestyle=":", linewidth=2)

# # Set the limits and scale for the zoomed-in portion
# axins.set_xlim(0, 50)
# axins.set_ylim(5e-7, 1e-2)
# axins.set_yscale("log")

# axins.set_xticks([])
# axins.set_yticks([])

# # This draws the cool connecting lines from the zoomed area to the inset box
# ax.indicate_inset_zoom(axins, edgecolor="black")

plt.show()
# plt.savefig(f"{title}.png", dpi=300)
