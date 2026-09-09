# Master's Thesis: A Novel Self-Sustaining Process in Plane
Couette Flow

This repository contains my Master's Thesis as part of my Advanced Computational Methods for Aeronautics MSc, along with the simulation environments, source code, and post-processing scripts used for the CFD experiments in my Master's thesis. The simulations are built around the **Diablo** solver to simulate Generalised Quasilinear (GQL) approximations.

## 📂 Repository Structure

*   **`Report/`**: Contains the Master Thesis report.
    *   **`Figures/`**: Contains all the Figures in the thesis 
*   **`Example_CFD_Folder_For_QLAZ/`**: A working example directory demonstrating how an individual simulation experiment is set up and executed.
*   **`CHANNELF_Files/`**: Contains the modified Channel.F files corresponding to different experimental setups discussed in the thesis.
*   **`DataAnalysis/`**: Contains all the code used for post-processing the simulation data.
    *   **`Base_codes/`**: Fundamental scripts to extract general parameters and basic metrics from the simulation outputs.
    *   **`Advanced/`**: Specialised scripts designed to extract specific features from the flow fields.

## 📊 Simulation Outputs

When a basic simulation is successfully run, the engine generates several data files in both `.d` (data) and `.h5` (HDF5) formats:

| Output File | Description |
| :--- | :--- |
| `trace.d` | Time history of key scalar parameters, including the time step, bulk velocity, friction Reynolds number, and mean pressure gradient. |
| `mean.h5` | 1D wall-normal profiles of time-averaged physical flow statistics. |
| `out000n.h5` | Full 3D instantaneous flow field snapshots (where *n* denotes the snapshot sequence). |
| `spectra.h5` | The full spectral turbulent kinetic energy budget. |
| `Euvw_ypm50_*.d` | Time history of specific mode energies calculated within a volume near the centre of the channel (`_all`), or bounding it on top/bottom (`_tcore` / `_bcore`). |
