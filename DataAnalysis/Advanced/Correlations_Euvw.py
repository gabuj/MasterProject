"""
This script reads correlation data from text files and plots various autocorrelations and cross-correlations. 
The data is loaded from a specified folder, and the resulting plots are saved as PNG files.
"""

import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Advanced.get_parameters import calculate_normalized_correlation
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman", "Nimbus Roman No9 L", "DejaVu Serif"]

folder="DataFiles/QLAZ_Re1428"

#--------------------------------------------------------------------------------------
# AUTOCORRELATIONS   
 
tau, Cuu = np.loadtxt(f"{folder}/C_uu.d", skiprows=1, unpack=True)
tau, C00 = np.loadtxt(f"{folder}/C_00.d", skiprows=1, unpack=True)
tau, C11 = np.loadtxt(f"{folder}/C_11.d", skiprows=1, unpack=True)
# tau, C1m = np.loadtxt(f"{folder}/C_1m.d", skiprows=1, unpack=True)
tau, Cvv = np.loadtxt(f"{folder}/C_vv.d", skiprows=1, unpack=True)
tau, Cww = np.loadtxt(f"{folder}/C_ww.d", skiprows=1, unpack=True)
tau, Cxx = np.loadtxt(f"{folder}/C_xx.d", skiprows=1, unpack=True)


#--------------------------------------------------------------------------------------
# Cross-CORRELATIONS                        
tau, Cuv = np.loadtxt(f"{folder}/C_uv.d", skiprows=1, unpack=True)
tau, Cuw = np.loadtxt(f"{folder}/C_uw.d", skiprows=1, unpack=True)
tau, Cvw = np.loadtxt(f"{folder}/C_vw.d", skiprows=1, unpack=True)
tau, Cv0 = np.loadtxt(f"{folder}/C_v0.d", skiprows=1, unpack=True)
tau, Cw0 = np.loadtxt(f"{folder}/C_w0.d", skiprows=1, unpack=True)
tau, C01 = np.loadtxt(f"{folder}/C_01.d", skiprows=1, unpack=True)
# tau, C01m = np.loadtxt(f"{folder}/C_01m.d", skiprows=1, unpack=True)
tau, C1v = np.loadtxt(f"{folder}/C_1v.d", skiprows=1, unpack=True)
# tau, C1mv = np.loadtxt(f"{folder}/C_1mv.d", skiprows=1, unpack=True)
tau, C0u = np.loadtxt(f"{folder}/C_0u.d", skiprows=1, unpack=True)
tau, Cxv = np.loadtxt(f"{folder}/C_xv.d", skiprows=1, unpack=True)
tau, Cx1 = np.loadtxt(f"{folder}/C_x1.d", skiprows=1, unpack=True)
# tau, Cx1m = np.loadtxt(f"{folder}/C_x1m.d", skiprows=1, unpack=True)
tau, C0x = np.loadtxt(f"{folder}/C_0x.d", skiprows=1, unpack=True)



tau, C_Tt10 = np.loadtxt(f"{folder}/C_Tt10.d", skiprows=1, unpack=True)
tau, C_P10_10 = np.loadtxt(f"{folder}/C_P10_10.d", skiprows=1, unpack=True)
tau, C_P01_00 = np.loadtxt(f"{folder}/C_P01_00.d", skiprows=1, unpack=True)
tau, C_P11_11 = np.loadtxt(f"{folder}/C_P11_11.d", skiprows=1, unpack=True)


#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#                                      PLOTTING!

# title=f"correlations Euvw"
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(tau, Cuu, label="Cuu", color="black", linestyle="-", linewidth=2)
# ax.plot(tau, Cvv, label="Cvv", color="black", linestyle="--", linewidth=2)
# ax.plot(tau, Cuv, label="Cuv", color="black", linestyle="-.", linewidth=2)
# ax.plot(tau, Cvw, label="Cvw", color="black", linestyle=":", linewidth=2)
# ax.set_title(title, fontsize=14)
# ax.set_xlabel(f"$\\tau u_{{\\tau}} / h$", fontsize=12)
# plt.xlim(-4, 4)
# plt.ylim(-0.5, 1.5)
# ax.set_ylabel("Correlations", fontsize=12)
# ax.grid(True, which="both", linestyle=":", alpha=0.5)
# ax.legend(fontsize=11)
# plt.show()
# plt.savefig(f"{title}.png", dpi=300)


# #--------------------------------------------------------------------------------------

# title=f"correlations E10"
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(tau, C00, label="C00", color="black", linestyle="-", linewidth=2)
# ax.plot(tau, C11, label="C11", color="black", linestyle="--", linewidth=2)
# ax.plot(tau, C01, label="C01", color="black", linestyle="-.", linewidth=2)
# ax.set_title(title, fontsize=14)
# ax.set_xlabel(f"$\\tau u_{{\\tau}} / h$", fontsize=12)
# plt.xlim(-4, 4)
# plt.ylim(-0.5, 1.5)
# ax.set_ylabel("Correlations", fontsize=12)
# ax.grid(True, which="both", linestyle=":", alpha=0.5)
# ax.legend(fontsize=11)
# plt.show()
# plt.savefig(f"{title}.png", dpi=300)

# #--------------------------------------------------------------------------------------

# title=f"correlations streak generation"
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(tau, Cv0, label="Cv0", color="black", linestyle="-", linewidth=2)
# ax.plot(tau, Cw0, label="Cw0", color="black", linestyle="--", linewidth=2)
# ax.set_title(title, fontsize=14)
# ax.set_xlabel(f"$\\tau u_{{\\tau}} / h$", fontsize=12)
# plt.xlim(-4, 4)
# plt.ylim(-0.5, 1.5)
# ax.set_ylabel("Correlations", fontsize=12)
# ax.grid(True, which="both", linestyle=":", alpha=0.5)
# ax.legend(fontsize=11)
# plt.show()
# plt.savefig(f"{title}.png", dpi=300)


# #--------------------------------------------------------------------------------------

# title=f"correlations alpha generation"
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(tau, Cx1, label="Cx1", color="black", linestyle="-", linewidth=2)
# # ax.plot(tau, Cx1m, label="Cx1m", color="black", linestyle="--", linewidth=2)
# ax.plot(tau, C0x, label="C0x", color="black", linestyle="-.", linewidth=2)
# ax.plot(tau, Cxx, label="Cxx", color="black", linestyle=":", linewidth=2)
# ax.set_title(title, fontsize=14)
# ax.set_xlabel(f"$\\tau u_{{\\tau}} / h$", fontsize=12)
# plt.xlim(-4, 4)
# plt.ylim(-0.5, 1.5)
# ax.set_ylabel("Correlations", fontsize=12)
# ax.grid(True, which="both", linestyle=":", alpha=0.5)
# ax.legend(fontsize=11)
# plt.show()
# plt.savefig(f"{title}.png", dpi=300)


# #--------------------------------------------------------------------------------------

# title=f"correlations vortex generation"
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(tau, C1v, label="C1v", color="black", linestyle="-", linewidth=2)
# # ax.plot(tau, C1mv, label="C1mv", color="black", linestyle="--", linewidth=2)
# ax.plot(tau, Cxv, label="Cxv", color="black", linestyle="-.", linewidth=2)
# ax.plot(tau, Cvv, label="Cvv", color="black", linestyle=":", linewidth=2)
# ax.set_title(title, fontsize=14)
# ax.set_xlabel(f"$\\tau u_{{\\tau}} / h$", fontsize=12)
# plt.xlim(-4, 4)
# plt.ylim(-0.5, 1.5)
# ax.set_ylabel("Correlations", fontsize=12)
# ax.grid(True, which="both", linestyle=":", alpha=0.5)
# ax.legend(fontsize=11)
# plt.show()
# plt.savefig(f"{title}.png", dpi=300)


#--------------------------------------------------------------------------------------

title=f"correlations turbtrans"
fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(tau, C_Tt10, label="C_Tt10", color="black", linestyle="-", linewidth=2)
ax.plot(tau, C_P10_10, label="C_P10_10", color="black", linestyle="-", linewidth=2)

# ax.set_title(title, fontsize=14)
ax.set_xlabel(f"$\\tau u_{{\\tau}} / h$", fontsize=12)
plt.xlim(-4, 4)
plt.ylim(-0.5, 1.5)
ax.set_ylabel("Correlation", fontsize=12)
# ax.grid(True, which="both", linestyle=":", alpha=0.5)
# ax.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)

#--------------------------------------------------------------------------------------

title=f"correlations prod01"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(tau, C_P01_00, label="C_P01_00", color="black", linestyle="-", linewidth=2)

# ax.set_title(title, fontsize=14)
ax.set_xlabel(f"$\\tau u_{{\\tau}} / h$", fontsize=12)
plt.xlim(-4, 4)
plt.ylim(-0.5, 1.5)
ax.set_ylabel("Correlation", fontsize=12)
# ax.grid(True, which="both", linestyle=":", alpha=0.5)
# ax.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)