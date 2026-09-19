# python-clib
> A small C library, compiled to a shared object and called from Python via `ctypes`, used to model a block sliding along a circular arc — its position, speed and acceleration — with the results plotted in matplotlib.

## What it does
* `clib.c` – three C functions: `get_y_block` (the block's position along the arc, from its geometry), `speed_block`, and `acceleration_of_the_block`
* `Makefile` – builds `clib.c` into `libclib.so`
* `clib_use.py` – prompts for the arc's geometry (chord length, radius, angle, height) and a time interval, calls the compiled C functions through `ctypes`, prints the resulting position/speed/acceleration, and saves three plots (`graph.png`, `graph1.png`, `graph2.png`)

## Setup
```
make
pip install -r requirements.txt
python clib_use.py
```
`libclib.so` and `clib.o` are compiled binaries already checked into the repo (built for Linux) — run `make` to rebuild them for your own machine.

## Status
**Archived** — not actively maintained.

Written in December 2019 as a coursework project to practice calling C code from Python via `ctypes`, applied to a mechanics calculation.
