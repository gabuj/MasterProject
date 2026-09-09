#!/usr/bin/env bash
set -euo pipefail

if [[ ! -s pid.num ]]; then
    echo "No pid.num found. Simulation is not running from this directory."
    exit 1
fi

pid=$(tail -n 1 pid.num)

if ps -p "$pid" >/dev/null 2>&1; then
    echo "Simulation is running: PID $pid"
    pwdx "$pid" || true
else
    echo "Simulation is not running: PID $pid is not active."
fi

if [[ -f nohup.out ]]; then
    tail -100 nohup.out
fi

if [[ -f newton_ct.dat ]]; then
    tail newton_ct.dat
fi
