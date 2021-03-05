#!/bin/bash
#PJM -L "rscunit=cl"
#PJM -L "rscgrp=cl-debug"
#PJM -L "node=1"
#PJM -L "elapse=1:00:00"
#PJM -j

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
conda_base=/home/z43901k/miniconda3
__conda_setup="$("$conda_base/bin/conda" 'shell.bash' 'hook' 2> /dev/null)"

if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "$conda_base/etc/profile.d/conda.sh" ]; then
        . "$conda_base/etc/profile.d/conda.sh"
    else
        export PATH="$conda_base/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

module load gaussian16/c01
conda activate py37-upack
python /home/z43901k/data/develop/laqa-py3/laqa_confopt.py laqa_confopt_uff_pm6.inp
conda deactivate
