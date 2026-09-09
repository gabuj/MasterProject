Each experiment is run in a folder with all necessary files to run the diablo simulations. An example is the "Example_CFD_Folder_For_QLAZ"

The engine of all different simulations in my thesis are based on the basic Channel.F file that simulates GQL.
The different experiments explained in the thesis are set up by adding part to the basic Channel.F file, as seen in the different Channel_X.F files in the CHANNELF_Files folder.

The outputs of the basic simualtions are: 
- trace.d: file containing the time history of some scalars, including time step, bulk velocity, friction Reynolds number, and mean pressure gradient.
- mean.h5: file containing 1D wall-normal profiles of time-averaged physical flow statistics. 
- out000n.h5: files containing full 3D instantaneous flow field snapshots. 
- spectra.h5: file containing the full spectral turbulent kinetic energy (TKE) budget. 
- Euvw_ypm50_all/_bcore/_tcore.d: file containing the time history of specific mode energies calculated within a volume near the centre of the channel or on top/under it.

All code used for post-processing is found in the DataAnalysis folder, which includes a Base_codes folder, 
with basic code to extract paramters from the simulation outputs,
and an Advanced folder, with code to extract more specific features