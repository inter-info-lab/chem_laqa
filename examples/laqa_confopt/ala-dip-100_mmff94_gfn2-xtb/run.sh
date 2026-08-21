#!/bin/bash

export OMP_NUM_THREADS=8
export OMP_STACKSIZE=2GB

. ~/miniforge3/etc/profile.d/conda.sh
conda activate py311-chemlaqa

laqaconfopt laqa_confopt_mmff94_gfn2-xtb.inp >& output.log
