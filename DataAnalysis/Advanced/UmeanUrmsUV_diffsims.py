"""
This script compares the mean and RMS velocity profiles, as well as the Reynolds stress, from different simulation datasets (DNS, QLAZ, and QLAX). It reads the data from text files, plots the profiles for each dataset, and saves the figures
"""
import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Advanced.get_parameters import *
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman", "Nimbus Roman No9 L", "DejaVu Serif"]

folder_DNS="DataFiles/DNS_Re1000"
folder_QLAZ="DataFiles/QLAZ_Re1428"
folder_QLAX="DataFiles/QLAX_Re1000"


fname = "mean.h5"
filename_QLAZ = f"{folder_QLAZ}/{fname}"
filename_QLAX = f"{folder_QLAX}/{fname}"
filename_DNS = f"{folder_DNS}/{fname}"

Re_tau=65.3
nu=0.001
u_tau=nu*Re_tau

y_phys_QLAZ, u_mean_QLAZ = np.loadtxt(f"{folder_QLAZ}/u_mean.d", skiprows=1, unpack=True)
y_phys_QLAZ, u_rms_QLAZ = np.loadtxt(f"{folder_QLAZ}/u_rms.d", skiprows=1, unpack=True)
y_phys_QLAZ, v_rms_QLAZ = np.loadtxt(f"{folder_QLAZ}/v_rms.d", skiprows=1, unpack=True)
y_phys_QLAZ, w_rms_QLAZ = np.loadtxt(f"{folder_QLAZ}/w_rms.d", skiprows=1, unpack=True)
y_phys_QLAZ, uv_QLAZ = np.loadtxt(f"{folder_QLAZ}/uv.d", skiprows=1, unpack=True)

y_phys_DNS, u_mean_DNS = np.loadtxt(f"{folder_DNS}/u_mean.d", skiprows=1, unpack=True)
y_phys_DNS, u_rms_DNS = np.loadtxt(f"{folder_DNS}/u_rms.d", skiprows=1, unpack=True)
y_phys_DNS, v_rms_DNS = np.loadtxt(f"{folder_DNS}/v_rms.d", skiprows=1, unpack=True)
y_phys_DNS, w_rms_DNS = np.loadtxt(f"{folder_DNS}/w_rms.d", skiprows=1, unpack=True)
y_phys_DNS, uv_DNS = np.loadtxt(f"{folder_DNS}/uv.d", skiprows=1, unpack=True)

y_phys_QLAX, u_mean_QLAX = np.loadtxt(f"{folder_QLAX}/u_mean.d", skiprows=1, unpack=True)
y_phys_QLAX, u_rms_QLAX = np.loadtxt(f"{folder_QLAX}/u_rms.d", skiprows=1, unpack=True)
y_phys_QLAX, v_rms_QLAX = np.loadtxt(f"{folder_QLAX}/v_rms.d", skiprows=1, unpack=True)
y_phys_QLAX, w_rms_QLAX = np.loadtxt(f"{folder_QLAX}/w_rms.d", skiprows=1, unpack=True)
y_phys_QLAX, uv_QLAX = np.loadtxt(f"{folder_QLAX}/uv.d", skiprows=1, unpack=True)


data_name=f"$<U>_{{x,z,t}}$"
title=f"umean_comparison"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot( y_phys_QLAZ,u_mean_QLAZ, label=f"QLAZ", color="black", linewidth=2, linestyle='solid')
plt.plot( y_phys_DNS,u_mean_DNS, label=f"DNS", color="black", linewidth=2, linestyle='dotted')
plt.plot( y_phys_QLAX,u_mean_QLAX, label=f"QLAX", color="black", linewidth=2, linestyle='dashed')
# ax.set_title(title, fontsize=14)
ax.set_xlabel("y/h", fontsize=12)
ax.set_ylabel('U', fontsize=12)
# plt.grid(True, which="both", linestyle=":", alpha=0.5)
# plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)

#---------------------------------------------------------------------------
#Urms

data_name=f"$<u_{{rms}}>_{{x,z,t}}$"

title=f"urms_comparison"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_phys_QLAZ,u_rms_QLAZ, label=f"QLAZ", color="black", linewidth=2, linestyle='solid')
plt.plot(y_phys_DNS,u_rms_DNS, label=f"DNS", color="black", linewidth=2, linestyle='dotted')
plt.plot(y_phys_QLAX,u_rms_QLAX, label=f"QLAX", color="black", linewidth=2, linestyle='dashed')
# ax.set_title(title, fontsize=14)
ax.set_xlabel("y/h", fontsize=12)
ax.set_ylabel(r'$u_{rms}$', fontsize=12)
# plt.grid(True, which="both", linestyle=":", alpha=0.5)
# plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)


#---------------------------------------------------------------------------
#Vrms

data_name=f"$<v_{{rms}}>_{{x,z,t}}$"

title=f"vrms_comparison"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_phys_QLAZ,v_rms_QLAZ, label=f"QLAZ", color="black", linewidth=2, linestyle='solid')
plt.plot(y_phys_DNS,v_rms_DNS, label=f"DNS", color="black", linewidth=2, linestyle='dotted')
plt.plot(y_phys_QLAX,v_rms_QLAX, label=f"QLAX", color="black", linewidth=2, linestyle='dashed')
# ax.set_title(title, fontsize=14)
ax.set_xlabel("y/h", fontsize=12)
ax.set_ylabel(r'$v_{rms}$', fontsize=12)
# plt.grid(True, which="both", linestyle=":", alpha=0.5)
# plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)


#---------------------------------------------------------------------------
#Wrms

data_name=f"$<w_{{rms}}>_{{x,z,t}}$"

title=f"wrms_comparison"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_phys_QLAZ,w_rms_QLAZ, label=f"QLAZ", color="black", linewidth=2, linestyle='solid')
plt.plot(y_phys_DNS,w_rms_DNS, label=f"DNS", color="black", linewidth=2, linestyle='dotted')
plt.plot(y_phys_QLAX,w_rms_QLAX, label=f"QLAX", color="black", linewidth=2, linestyle='dashed')
# ax.set_title(title, fontsize=14)
ax.set_xlabel("y/h", fontsize=12)
ax.set_ylabel(r'$w_{rms}$', fontsize=12)
# plt.grid(True, which="both", linestyle=":", alpha=0.5)
# plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)




#---------------------------------------------------------------------------
#<uv>

data_name=f"$-<u'v'>_{{x,z,t}}$"

title=f"uv_comparison"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_phys_QLAZ, uv_QLAZ, label=f"QLAZ", color="black", linewidth=2, linestyle='solid')
plt.plot(y_phys_DNS, uv_DNS, label=f"DNS", color="black", linewidth=2, linestyle='dotted')
plt.plot(y_phys_QLAX, uv_QLAX, label=f"QLAX", color="black", linewidth=2, linestyle='dashed')
# ax.set_title(title, fontsize=14)
ax.set_xlabel("y/h", fontsize=12)
ax.set_ylabel(r"$-\overline{u'v'}$", fontsize=12)
# plt.grid(True, which="both", linestyle=":", alpha=0.5)
# plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)


#---------------------------------------------------------------------------
#Wrms

data_name=f"$<w_{{rms}}>_{{x,z,t}}$"

title=f"rms_comparison"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_phys_QLAZ,u_rms_QLAZ, label=f"QLAZ", color="black", linewidth=2, linestyle='solid')
plt.plot(y_phys_DNS,u_rms_DNS, label=f"DNS", color="black", linewidth=2, linestyle='dotted')
plt.plot(y_phys_QLAX,u_rms_QLAX, label=f"QLAX", color="black", linewidth=2, linestyle='dashed')

plt.plot(y_phys_QLAZ,v_rms_QLAZ, label=f"QLAZ", color="black", linewidth=2, linestyle='solid')
plt.plot(y_phys_DNS,v_rms_DNS, label=f"DNS", color="black", linewidth=2, linestyle='dotted')
plt.plot(y_phys_QLAX,v_rms_QLAX, label=f"QLAX", color="black", linewidth=2, linestyle='dashed')

plt.plot(y_phys_QLAZ,w_rms_QLAZ, label=f"QLAZ", color="black", linewidth=2, linestyle='solid')
plt.plot(y_phys_DNS,w_rms_DNS, label=f"DNS", color="black", linewidth=2, linestyle='dotted')
plt.plot(y_phys_QLAX,w_rms_QLAX, label=f"QLAX", color="black", linewidth=2, linestyle='dashed')
# ax.set_title(title, fontsize=14)
ax.set_xlabel("y/h", fontsize=12)
ax.set_ylabel(r'$w_{rms}$', fontsize=12)
# plt.grid(True, which="both", linestyle=":", alpha=0.5)
# plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)
