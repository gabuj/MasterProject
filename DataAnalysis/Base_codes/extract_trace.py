import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Base_codes.get_parameters import calculate_normalized_correlation

folder="DataFiles/QLAZ_Re1428"
fname = "trace.d"
filename = f"{folder}/{fname}"

nu = 0.0007
h = 1
dt=0.03
savestatsint=5
Time_window=0
window= int(Time_window/(dt*savestatsint))

t_step,t_phys,taubot,tautop,ubulk, dpdx=np.loadtxt(filename, unpack=True)
title="RE_tau bottom"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t_phys, taubot, label="RE_tau", color="blue", linewidth=2)
#plot line where window is set
ax.axvline(x=t_phys[-window], color="red", linestyle="--", label=f"Window Start (t={t_phys[-window]:.2f})")
# ax.set_xlim(0,1000)
ax.set_title(title, fontsize=14)
ax.set_xlabel("Time", fontsize=12)
ax.set_ylabel("RE_tau", fontsize=12)
ax.grid(True, which="both", linestyle=":", alpha=0.5)
ax.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)

title="RE_tau top"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t_phys, tautop, label="RE_tau", color="blue", linewidth=2)
#plot line where window is set
ax.axvline(x=t_phys[-window], color="red", linestyle="--", label=f"Window Start (t={t_phys[-window]:.2f})")
ax.set_title(title, fontsize=14)
ax.set_xlabel("Time", fontsize=12)
ax.set_ylabel("RE_tau", fontsize=12)
ax.grid(True, which="both", linestyle=":", alpha=0.5)
ax.legend(fontsize=11)
plt.show()
# plt.savefig(f"{title}.png", dpi=300)

title="ubulk"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t_phys, ubulk, label="ubulk", color="blue", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("Time", fontsize=12)
ax.set_ylabel("ubulk", fontsize=12)
ax.grid(True, which="both", linestyle=":", alpha=0.5)
ax.legend(fontsize=11)
plt.show()
# plt.savefig(f"{title}.png", dpi=300)

title="dpdx"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t_phys, dpdx, label="dpdx", color="blue", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("Time", fontsize=12)
ax.set_ylabel("dpdx", fontsize=12)
ax.grid(True, which="both", linestyle=":", alpha=0.5)
ax.legend(fontsize=11)
plt.show()
# plt.savefig(f"{title}.png", dpi=300)



Re_tau_top = np.array(tautop)
Re_tau_bot = np.array(taubot)

avg_Re_tau_top=np.mean(Re_tau_top[-window:])
avg_Re_tau_bot=np.mean(Re_tau_bot[-window:])

print(f"average Re_tau_top: {avg_Re_tau_top}")
print(f"average Re_tau_bot: {avg_Re_tau_bot}")





#get dt
dt=np.diff(t_phys)/np.diff(t_step)[0]
title="dt"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t_step[:-1], dt, label="dt", color="blue", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel("Time step", fontsize=12)
ax.set_ylabel("dt", fontsize=12)
ax.grid(True, which="both", linestyle=":", alpha=0.5)
ax.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)

exit()











#---------------------------------------------------------------------------------------
#CORRELATION
tau, CRe_tau_top = calculate_normalized_correlation(Re_tau_top, t_phys)

#plot
title=f"Correlation of RE_tau_top"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(tau, CRe_tau_top, label=f"C_RE_tau_top", color="blue", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel(f"$\\tau$", fontsize=12)
# plt.xlim(-1000, 1000)
ax.set_ylabel("Correlation", fontsize=12)
ax.grid(True, which="both", linestyle=":", alpha=0.5)
ax.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)

#save data in folder
np.savetxt(f"{folder}/C_Re_tau_top.d", np.column_stack((tau, CRe_tau_top)), header="tau C_Re_tau_top", comments="")