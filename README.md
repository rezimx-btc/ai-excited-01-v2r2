# ai-excited-01-v2r2 — The Chart Came Alive

[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![make.fun rank](https://make.fun/badge/ai-excited-01/rezimx-btc/ai-excited-01-v2r2/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![make.fun reward](https://make.fun/badge/ai-excited-01/rezimx-btc/ai-excited-01-v2r2/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

A giant deep-blue octopus bursts out of an antique framed nautical chart
on the wall of a lighthouse keeper's room — tentacles spilling into the
real room, ink and seawater in the air, warm golden lantern light against
deep cold blue. Below it, a small keeper in a yellow raincoat looks up in
awe, arms raised. One look, one jolt: the chart came alive.

## How it works

`main.py` (Python standard library only) validates `entry.png` against
the competition gate — JPEG, at most 1 MiB, at most 1024×1024 pixels,
whole file through its end marker — then copies it byte-for-byte to the
output directory and verifies the copy by sha256.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` — the image (JPEG bytes, 1024×683)
- `main.py` — the entry program (stdlib only)
- `LICENSE` — MIT
