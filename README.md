# LAQA confopt
Coformation search code and global geometry optimization code using Look Ahead based on Quadratic Approximation (LAQA) method

@Author: Michio Katouda (RIST) base on the LAQA code by Kei Terayama (Univ. Tokyo, RIKEN AIP, and Kyoto Univ.)
@e-mail: katouda@rist.or.jp

#  Requirements
1. [Python] (https://www.anaconda.com/download/)
2. [rdkit]  (https://anaconda.org/conda-forge/rdkit)
3. [xTB]    (https://anaconda.org/conda-forge/xtb)
#  Optional
4. [Gaussian 16] (https://gaussian.com/gaussian16/)

# Installation of pyton envriromntent for LAQA confopt
1. Install miniforge3 (recommended), miniconda3, or anaconda3
2. Creaate python 3.11 virtual environment
```
$ conda create -n py311-chemlaqa python=3.11
$ conda activate py311-chemlaqa
$ conda install -c conda-forge rdkit xtb
```

# How to run LAQA confopt job

# Conformation optimization of Alanine dipeptide with GFN2-xTB
1. Move working dirctory
```
$ cd ./examples/laqa_confopt/ala-dip-100_uff_gfn2-xtb
```   

2. Set environmental variables for xTB code (bash or ksh cases).
```
$ export OMP_NUM_THREADS=8
$ export OMP_STACKSIZE=2GB
```

3. Run python script ForGetinput.py with input file laqa_confopt_uff_gfn2-xtb.inp
```
$ laqaconfopt laqa_confopt_uff_gfn2-xtb.inp
```

# Conformation optimization of Alanine dipeptide with wB97XD/6-31G(d)
 Note: Instalattion of Gaussian 16 and modification of Gaussian settings in input file laqa_confopt_uff_wb97xd-6-31gd.inp to match computing system which you employed.

1. Move working dirctory
```
$ cd ./examples/laqa_confopt/ala-dip-100_uff_wb97xd
```

2. Modify gauss_exedir, nprocs, memory keywords in input file laqa_confopt_uff_wb97xd-6-31gd.inp to match your computing environment
```
# Gaussian settings
energy_function = "g16"
# Path of Gaussian execute directory
gauss_exedir = "/path/to/gaussian16/c01/g16"
# Number of processors used in Gaussian job 
nprocs = 20
# Menirt size used in Gaussian job
memory = '128GB'
```

3. Run python script ForGetinput.py with input file laqa_confopt_uff_wb97xd-6-31gd.inp
```
$ laqaconfopt laqa_confopt_uff_wb97xd-6-31gd.inp
```
