import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Base_codes.get_parameters import calculate_normalized_correlation
#peak energy at 5610

file="Euvw_ypm50"
folder="DataFiles/DNS_Re1000_ShortPeriod"
folder="DataFiles/QLAZ_Re1428_ShortPeriod"
Re_tau=63.0
nu=0.0007
u_tau=nu*Re_tau
dt=0.03

t_step,t_phys,Euu_core,Evv_core,Eww_core, E00_core, E11_core, E10_core =np.loadtxt(f"{folder}/{file}_all.d", unpack=True)

# E00=E00_bot+E00_core+E00_top
# E11=E11_bot+E11_core+E11_top
# E10=E10_bot+E10_core+E10_top
# E1m=E1m_bot+E1m_core+E1m_top
# Euu=Euu_bot+Euu_core+Euu_top
# Evv=Evv_bot+Evv_core+Evv_top
# Eww=Eww_bot+Eww_core+Eww_top

E00=E00_core
E11=E11_core
E10=E10_core
# E1m=E1m_core
Euu=Euu_core
Evv=Evv_core
Eww=Eww_core

savestatsint=5
outcheck=18
totOuts=100
totTimeSteps=25000
Time_checkpoint=outcheck*totTimeSteps*dt/totOuts
checkpoint= int(Time_checkpoint/(dt*savestatsint))

data_to_plot = E10  # Change this to plot different variables
data_name="E10"  # Change this to the name of the variable you're plotting

auto=True
data_to_plot2= E00
data_name2="E0"



title=f"Evolution of energies"
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t_phys, data_to_plot, label=data_name, linestyle="-",color="black", linewidth=2)
# ax.plot(t_phys, E10, label=f"E10", linestyle="--", color="black", linewidth=2)
ax.set_xlim(0, 500)
ax.set_title(title, fontsize=14)
ax.set_xlabel("t*Uw/h", fontsize=12)
ax.axvline(x=t_phys[checkpoint], color="black", linestyle="--", label=f"t={t_phys[checkpoint]:.2f})")
ax.set_ylabel('energies', fontsize=12)
ax.grid(True, which="both", linestyle=":", alpha=0.5)
ax.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)

exit()

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#                         CORRELATION!

if auto==True:
    tau, correlation = calculate_normalized_correlation(data_to_plot, t_phys, normalize_time_by_u_tau=True, u_tau=u_tau)
    data_name2= ""
    title=f"{data_name} autocorrelation Profile"
    label=f"C_{data_name}"


else:
    tau, correlation = calculate_normalized_correlation(data_to_plot, t_phys, data_to_plot2, normalize_time_by_u_tau=True, u_tau=u_tau)
    title=f"{data_name}, {data_name2} cross-correlation Profile"
    label=f"C_{data_name}_{data_name2}"





fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(tau, correlation, label=label, color="black", linewidth=2)
ax.set_title(title, fontsize=14)
ax.set_xlabel(f"$\\tau u_{{\\tau}} / h$", fontsize=12)
plt.xlim(-4, 4)
plt.ylim(-0.5, 1.5)
ax.set_ylabel("Correlation", fontsize=12)
# ax.grid(True, which="both", linestyle=":", alpha=0.5)
ax.legend(fontsize=11)
plt.show()
plt.savefig(f"{title}.png", dpi=300)

#save data in folder
np.savetxt(f"{folder}/C_{data_name}_{data_name2}.d", np.column_stack((tau, correlation)), header="tau C_{data_name}_{data_name2}", comments="")