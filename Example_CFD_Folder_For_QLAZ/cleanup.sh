#!/usr/bin/env bash
set -euo pipefail

make -f Makefile_fenchurchstreet clean

rm -f Euvw.d newton.dat out* RUNNING shifts.dat trace.d arnoldi.dat nohup.out \
      end.h5 mean.h5 tke* Y.* spectra.h5 end_force.h5 corry.h5 \
      Euvw_ypm50_bcore.d Euvw_ypm50_tcore.d Euvw_all.d stop.now \
      eta_out* eta_end* pid.num newton_ct.dat
rm -f .channel.F.swo .channel.F.swp .MATLABDriveTag

mkdir -p flowfield
find flowfield -mindepth 1 -maxdepth 1 -exec rm -rf -- {} +
