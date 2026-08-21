#!/bin/bash

export OMP_NUM_THREADS=8
export OMP_STACKSIZE=2GB

. ~/miniforge3/etc/profile.d/conda.sh
conda activate py311-chemlaqa

laqainitgeom initgeom_mmff94.inp >& output.log
