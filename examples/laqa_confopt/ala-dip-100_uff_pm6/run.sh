#!/bin/bash

export OMP_STACKSIZE=1GB

. ~/miniforge3/etc/profile.d/conda.sh
conda activate py311-chemlaqa

laqaconfopt laqa_confopt_uff_pm6.inp >& output.log
