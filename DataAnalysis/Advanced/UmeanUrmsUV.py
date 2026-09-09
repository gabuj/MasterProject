"""
This script visualizes the mean and RMS velocity profiles, as well as the Reynolds stress, from the DIABLO simulation. It reads the data from text files, plots the profiles, and saves the figures for further analysis.
"""
import h5py
import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Advanced.get_parameters import *

folder="DataFiles/QLAZ_Re1428"

NoYPLUS=True

fname = "mean.h5"
filename = f"{folder}/{fname}"

Re_tau=65.3
nu=0.001
u_tau=nu*Re_tau

y_phys, u_mean = np.loadtxt(f"{folder}/u_mean.d", skiprows=1, unpack=True)
y_phys, u_rms = np.loadtxt(f"{folder}/u_rms.d", skiprows=1, unpack=True)
y_phys, v_rms = np.loadtxt(f"{folder}/v_rms.d", skiprows=1, unpack=True)
y_phys, w_rms = np.loadtxt(f"{folder}/w_rms.d", skiprows=1, unpack=True)
y_phys, uv = np.loadtxt(f"{folder}/uv.d", skiprows=1, unpack=True)


data_to_plot=u_mean
data_name=f"$<U>_{{x,z,t}}$"
title=f"{data_name}"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot( y_phys,data_to_plot, label=f"{data_name}", marker= 'x', color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y_h", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)

#---------------------------------------------------------------------------
#Urms

data_to_plot=u_rms
data_name=f"$<u_{{rms}}>_{{x,z,t}}$"

title=f"{data_name}"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_phys,data_to_plot, label=f"{data_name}", marker= 'x', color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y_h", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)


#---------------------------------------------------------------------------
#Vrms

data_to_plot=v_rms
data_name=f"$<v_{{rms}}>_{{x,z,t}}$"

title=f"{data_name}"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_phys,data_to_plot, label=f"{data_name}", marker= 'x', color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y_h", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
# plt.savefig(f"{title}.png", dpi=300)


#---------------------------------------------------------------------------
#Wrms

data_to_plot=w_rms
data_name=f"$<w_{{rms}}>_{{x,z,t}}$"

title=f"{data_name}"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_phys,data_to_plot, label=f"{data_name}", marker= 'x', color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y_h", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
# plt.savefig(f"{title}.png", dpi=300)




#---------------------------------------------------------------------------
#<uv>

data_to_plot= - uv
data_name=f"$-<u'v'>_{{x,z,t}}$"

title=f"{data_name}"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_phys,data_to_plot, label=f"{data_name}", marker= 'x', color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y_h", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
# plt.savefig(f"{title}.png", dpi=300)







if NoYPLUS==True:
    exit()
#---------------------------------------------------------------------------
#SAME BUT Y+
delta= nu/u_tau
y_plus=y_phys/delta

#y_plus from the wall
y_plus=y_plus-np.min(y_plus)
#---------------------------------------------------------------------------
#U+

data_to_plot=u_mean / u_tau
data_name=f"$<U^+>_{{x,z,t}}$"
title=f"{data_name} averaged over last {Time_window} Uw_h as a function of y+"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot( y_plus,data_to_plot, label=f"{data_name}", marker= 'x', color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y+", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)


#---------------------------------------------------------------------------
#Urms

data_to_plot=u_rms / u_tau
data_name=f"$<u_{{rms}}^+>_{{x,z,t}}$"

title=f"{data_name} averaged over last {Time_window} Uw_h as a function of y+"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_plus,data_to_plot, label=f"{data_name}", marker= 'x', color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y+", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)


#---------------------------------------------------------------------------
#Vrms

data_to_plot=v_rms / u_tau
data_name=f"$<v_{{rms}}^+>_{{x,z,t}}$"

title=f"{data_name} averaged over last {Time_window} Uw_h as a function of y+"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_plus,data_to_plot, label=f"{data_name}", marker= 'x', color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y+", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)


#---------------------------------------------------------------------------
#<uv>

data_to_plot= - uv / u_tau**2
data_name=f"$<-<u'v'>_{{x,z,t}}^+>_{{x,z,t}}$"

title=f"{data_name} averaged over last {Time_window} Uw_h as a function of y+"
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(y_plus,data_to_plot, label=f"{data_name}", marker= 'x', color="red", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("y+", fontsize=12)
ax.set_ylabel(data_name, fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)