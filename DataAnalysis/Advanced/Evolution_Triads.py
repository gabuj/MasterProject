"""
This script reads data from text files and plots the evolution of various triad components over time.
"""
import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Advanced.get_parameters import calculate_normalized_correlation
#interesting times: DNS: 970-1350 / 64-88 
# QLAZ: 970-1350

file="Triad_10_trace"
folder="DataFiles/Fixed_Umean/FrozenU_withPert_fromAlpha"
folder="DataFiles/NoEnergies/NoStreaks2_MinAlpha"
folder="DataFiles/QLAZ_Re1428_ShortPeriod"


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

t_step,t_phys,Tt_sim,Tt_si,Tt_i21,Tt_im21m,Prod_10,Prod_11,Prod_1m1,Prod_01 =np.loadtxt(f"{folder}/{file}.d", unpack=True)

Streaks_triads=Tt_sim+Tt_si
higher_triads=Tt_i21+Tt_im21m
#-------------------------------------------------------------------

title=f"triads energies"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t_phys, Tt_sim, label="Tt_sim", color="black", linestyle="-", linewidth=2)
ax.plot(t_phys, Tt_si, label="Tt_si", color="black", linestyle="--", linewidth=2)
ax.plot(t_phys, Tt_i21, label="Tt_i21", color="black", linestyle="-.", linewidth=2)
ax.plot(t_phys, Tt_im21m, label="Tt_im21m", color="black", linestyle=":", linewidth=2)

# ax.set_xlim(0,300)
# ax.set_ylim(1e-3, 1e23)
ax.set_xlabel(f"$tU_{{w}} / h$", fontsize=12)
ax.set_ylabel("Energies", fontsize=12)
plt.legend()

#ax.grid(True, which="both", linestyle=":", alpha=0.5)

plt.show()
# plt.savefig(f"{title}.png", dpi=300)

#-------------------------------------------------------------------


file="Euvw_ypm50"
t_step,t_phys_e,Euu_core,Evv_core,Eww_core, E00_core, E11_core, E10_core,_ =np.loadtxt(f"{folder}/{file}_all.d", unpack=True)

Prod_01=Prod_01/np.max(Prod_01)
E00_core=E00_core/np.max(E00_core)
title=f"production energies"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t_phys, Prod_11, label="Prod_11", color="black", linestyle="-", linewidth=2)
# ax.plot(t_phys, Prod_10, label="Prod_10", color="black", linestyle="--", linewidth=2)
# ax.plot(t_phys, Prod_11, label="Prod_11", color="black", linestyle=":", linewidth=2)
# ax.plot(t_phys, Prod_1m1, label="Prod_1m1", color="black", linestyle="-.", linewidth=2)
# ax.plot(t_phys_e, E00_core, label="strak energy", color="black", linestyle=":", linewidth=2)

# ax.set_yscale("log")
ax.set_xlim(0,300)
# ax.set_ylim(1e-3, 1e23)
ax.set_xlabel(f"$tU_{{w}} / h$", fontsize=12)
ax.set_ylabel("Energies", fontsize=12)
# plt.legend()
#ax.grid(True, which="both", linestyle=":", alpha=0.5)

plt.show()
plt.savefig(f"{title}.png", dpi=300)

#-------------------------------------------------------------------



#-------------------------------------------------------------------
turb_transp=Streaks_triads+higher_triads
turb_transp=turb_transp/np.max(turb_transp)
Prod_10=Prod_10/np.max(Prod_10)
E10_core=E10_core/np.max(E10_core)
title=f"10 energies"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t_phys, Prod_11, label="Prod_10", color="black", linestyle="-", linewidth=2)
# ax.plot(t_phys, higher_triads, label="higher_triads", color="black", linestyle="--", linewidth=2)
# ax.plot(t_phys, Prod_10, label="Prod_10", color="black", linestyle=":", linewidth=2)
ax.plot(t_phys_e, E10_core, label="E10_core", color="black", linestyle="--", linewidth=2)

ax.set_xlim(0,300)
# ax.set_ylim(1e-3, 1e23)
ax.set_xlabel(f"$tU_{{w}} / h$", fontsize=12)
ax.set_ylabel(f"$\hat{{T}}_{{turb}}, \hat{{P}}$", fontsize=12)
# plt.legend()

##ax.grid(True, which="both", linestyle=":", alpha=0.5)

plt.show()
# plt.savefig(f"{title}.png", dpi=300)

#-------------------------------------------------------------------
