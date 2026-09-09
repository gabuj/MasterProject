"""
This script reads correlation data from text files and calculates normalized correlations.
The data is loaded from a specified folder, and the resulting correlations are saved as text files.
"""

import numpy as np
import matplotlib.pyplot as plt
from AnalysisCode.Advanced.get_parameters import calculate_normalized_correlation

file="Euvw_ypm50"
folder="DataFiles/QLAZ_Re1428"
# folder="DataFiles/DNS_Re1000"
savefolder=folder

Re_tau=63.0
nu=0.0007
u_tau=nu*Re_tau
dt=0.03
print("ARE YOU SURE RE_TAU= ", Re_tau)
print("ARE YOU SURE dt= ", dt)

t_step,t_phys,Euu_core,Evv_core,Eww_core, E00_core, E11_core, E10_core,_ =np.loadtxt(f"{folder}/{file}_all.d", unpack=True)
file="Triad_10_trace"
t_step,t_phys,Tt_sim,Tt_si,Tt_i21,Tt_im21m,Prod_10,Prod_11,Prod_1m1,Prod_01 =np.loadtxt(f"{folder}/{file}.d", unpack=True)
Turb_trans=Tt_sim+Tt_si+Tt_i21+Tt_im21m
E00=E00_core
E11=E11_core
E10=E10_core
Euu=Euu_core
Evv=Evv_core
Eww=Eww_core


#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#                         CORRELATION!


# #--------------------------------------------------------------------------------------
# # AUTOCORRELATIONS                        
# tau, Cuu = calculate_normalized_correlation(Euu, t_phys, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau, C00 = calculate_normalized_correlation(E00, t_phys, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau, C11 = calculate_normalized_correlation(E11, t_phys, normalize_time_by_u_tau=True, u_tau=u_tau)
# # tau, C1m = calculate_normalized_correlation(E1m, t_phys, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau, Cvv = calculate_normalized_correlation(Evv, t_phys, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau, Cww = calculate_normalized_correlation(Eww, t_phys, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau, Cxx = calculate_normalized_correlation(E10, t_phys, normalize_time_by_u_tau=True, u_tau=u_tau)

# #save data in folder
# np.savetxt(f"{savefolder}/C_uu.d", np.column_stack((tau, Cuu)), header="tau C_uu", comments="")
# np.savetxt(f"{savefolder}/C_00.d", np.column_stack((tau, C00)), header="tau C_00", comments="")
# np.savetxt(f"{savefolder}/C_11.d", np.column_stack((tau, C11)), header="tau C_11", comments="")
# # np.savetxt(f"{savefolder}/C_1m.d", np.column_stack((tau, C1m)), header="tau C_1m", comments="")
# np.savetxt(f"{savefolder}/C_vv.d", np.column_stack((tau, Cvv)), header="tau C_vv", comments="")
# np.savetxt(f"{savefolder}/C_ww.d", np.column_stack((tau, Cww)), header="tau C_ww", comments="")
# np.savetxt(f"{savefolder}/C_xx.d", np.column_stack((tau, Cxx)), header="tau C_xx", comments="")
# #--------------------------------------------------------------------------------------
# # Cross-CORRELATIONS                        
# tau, Cuv = calculate_normalized_correlation(Euu, t_phys, Evv, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau, Cuw = calculate_normalized_correlation(Euu, t_phys, Eww, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau, Cvw = calculate_normalized_correlation(Evv, t_phys, Eww, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau, Cv0 = calculate_normalized_correlation(Evv, t_phys, E00, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau, Cw0 = calculate_normalized_correlation(Eww, t_phys, E00, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau, C01 = calculate_normalized_correlation(E00, t_phys, E11, normalize_time_by_u_tau=True, u_tau=u_tau)
# # tau, C01m = calculate_normalized_correlation(E00, t_phys, E1m, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau, C1v = calculate_normalized_correlation(E11, t_phys, Evv, normalize_time_by_u_tau=True, u_tau=u_tau)
# # tau, C1mv = calculate_normalized_correlation(E1m, t_phys, Evv, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau,C0u = calculate_normalized_correlation(E00, t_phys, Euu, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau,Cxv = calculate_normalized_correlation(E10, t_phys, Evv, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau,Cx1 = calculate_normalized_correlation(E10, t_phys, E11, normalize_time_by_u_tau=True, u_tau=u_tau)
# # tau,Cx1m = calculate_normalized_correlation(E10, t_phys, E1m, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau,C0x = calculate_normalized_correlation(E00, t_phys, E10, normalize_time_by_u_tau=True, u_tau=u_tau)



#--------------------------------------------------------------------------------------
#Correlations alpha,0 to triads

# tau,C1Tsim = calculate_normalized_correlation(E11, t_phys, Tt_sim, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau,C1Tsi = calculate_normalized_correlation(E11, t_phys, Tt_si, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau,C1Ti21 = calculate_normalized_correlation(E11, t_phys, Tt_i21, normalize_time_by_u_tau=True, u_tau=u_tau)
# tau,C1Tim21m = calculate_normalized_correlation(E11, t_phys, Tt_im21m, normalize_time_by_u_tau=True, u_tau=u_tau)
tau,C1prod10 = calculate_normalized_correlation(E11, t_phys, Prod_10, normalize_time_by_u_tau=True, u_tau=u_tau)
tau,C00prod01 = calculate_normalized_correlation(E00, t_phys, Prod_01, normalize_time_by_u_tau=True, u_tau=u_tau)
tau,CTt10= calculate_normalized_correlation(Turb_trans, t_phys, E10, normalize_time_by_u_tau=True, u_tau=u_tau)
tau,CP10_10= calculate_normalized_correlation(Prod_10, t_phys, E10, normalize_time_by_u_tau=True, u_tau=u_tau)
tau,CP01_00= calculate_normalized_correlation(Prod_01, t_phys, E00, normalize_time_by_u_tau=True, u_tau=u_tau)
tau,CP11_11= calculate_normalized_correlation(Prod_11, t_phys, E11, normalize_time_by_u_tau=True, u_tau=u_tau)









# #save data in folder
# np.savetxt(f"{savefolder}/C_uv.d", np.column_stack((tau, Cuv)), header="tau C_uv", comments="")
# np.savetxt(f"{savefolder}/C_uw.d", np.column_stack((tau, Cuw)), header="tau C_uw", comments="")
# np.savetxt(f"{savefolder}/C_vw.d", np.column_stack((tau, Cvw)), header="tau C_vw", comments="")
# np.savetxt(f"{savefolder}/C_v0.d", np.column_stack((tau, Cv0)), header="tau C_v0", comments="")
# np.savetxt(f"{savefolder}/C_w0.d", np.column_stack((tau, Cw0)), header="tau C_w0", comments="")
# np.savetxt(f"{savefolder}/C_01.d", np.column_stack((tau, C01)), header="tau C_01", comments="")
# # np.savetxt(f"{savefolder}/C_01m.d", np.column_stack((tau, C01m)), header="tau C_01m", comments="")
# np.savetxt(f"{savefolder}/C_1v.d", np.column_stack((tau, C1v)), header="tau C_1v", comments="")
# # np.savetxt(f"{savefolder}/C_1mv.d", np.column_stack((tau, C1mv)), header="tau C_1mv", comments="")
# np.savetxt(f"{savefolder}/C_0u.d", np.column_stack((tau, C0u)), header="tau C_0u", comments="")
# np.savetxt(f"{savefolder}/C_xv.d", np.column_stack((tau, Cxv)), header="tau C_xv", comments="")
# np.savetxt(f"{savefolder}/C_x1.d", np.column_stack((tau, Cx1)), header="tau C_x1", comments="")
# # np.savetxt(f"{savefolder}/C_x1m.d", np.column_stack((tau, Cx1m)), header="tau C_x1m", comments="")
# np.savetxt(f"{savefolder}/C_0x.d", np.column_stack((tau, C0x)), header="tau C_0x", comments="")
np.savetxt(f"{savefolder}/C_1Tsim.d", np.column_stack((tau, C1Tsim)), header="tau C_1Tsim", comments="")
np.savetxt(f"{savefolder}/C_1Tsi.d", np.column_stack((tau, C1Tsi)), header="tau C_1Tsi", comments="")
np.savetxt(f"{savefolder}/C_1Ti21.d", np.column_stack((tau, C1Ti21)), header="tau C_1Ti21", comments="")
np.savetxt(f"{savefolder}/C_1Tim21m.d", np.column_stack((tau, C1Tim21m)), header="tau C_1Tim21m", comments="")
np.savetxt(f"{savefolder}/C_1prod10.d", np.column_stack((tau, C1prod10)), header="tau C_1prod10", comments="")
np.savetxt(f"{savefolder}/C_00prod01.d", np.column_stack((tau, C00prod01)), header="tau C_00prod01", comments="")
np.savetxt(f"{savefolder}/C_Tt10.d", np.column_stack((tau, CTt10)), header="tau C_Tt10", comments="")  
np.savetxt(f"{savefolder}/C_P10_10.d", np.column_stack((tau, CP10_10)), header="tau C_P10_10", comments="")
np.savetxt(f"{savefolder}/C_P01_00.d", np.column_stack((tau, CP01_00)), header="tau C_P01_00", comments="")
np.savetxt(f"{savefolder}/C_P11_11.d", np.column_stack((tau, CP11_11)), header="tau C_P11_11", comments="")