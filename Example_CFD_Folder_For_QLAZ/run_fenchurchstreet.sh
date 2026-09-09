#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if ! type module >/dev/null 2>&1; then
    . /etc/profile.d/modules.sh
fi

. ./mod_load_fenchurchstreet.sh

HDF5_HOME="${HDF5_HOME:-$HOME/diablo_libraries/hdf5}"
H5PFC="$HDF5_HOME/bin/h5pfc"

if [[ ! -x "$H5PFC" ]]; then
    echo "HDF5 compiler wrapper not found: $H5PFC" >&2
    echo "Copy diablo_libraries to ~/diablo_libraries or set HDF5_HOME." >&2
    exit 1
fi

if [[ ! -w "$H5PFC" ]]; then
    echo "HDF5 compiler wrapper is not writable: $H5PFC" >&2
    echo "Copy diablo_libraries as your own user so this script can update its prefix." >&2
    exit 1
fi

# HDF5 compiler wrappers record their install prefix. If this library was
# copied from another account, point the wrapper at the current user's copy.
sed -i \
    -e "s|^prefix=.*|prefix=\"$HDF5_HOME\"|" \
    -e 's|^exec_prefix=.*|exec_prefix="${prefix}"|' \
    -e 's|^libdir=.*|libdir="${exec_prefix}/lib"|' \
    -e 's|^includedir=.*|includedir="${prefix}/include"|' \
    -e 's|^fmoddir=.*|fmoddir="${includedir}"|' \
    "$H5PFC"

export HDF5_HOME
make -f Makefile_fenchurchstreet

setsid /apps/intel/mpi/2021.11/bin/mpiexec -np 16 ./diablo > nohup.out 2>&1 < /dev/null & echo $! > pid.num
