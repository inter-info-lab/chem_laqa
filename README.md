# LAQA confopt
Coformation search code and global geometry optimization code using Look Ahead based on Quadratic Approximation (LAQA) method

@Author: Michio Katouda (RIST) base on the LAQA code by Kei Terayama (Univ. Tokyo, RIKEN AIP, and Kyoto Univ.)
@e-mail: katouda@rist.or.jp

#  Requirements 
1. [Python] (https://www.anaconda.com/download/)
2. [rdkit]  (https://anaconda.org/rdkit/rdkit)
3. [xTB]    (https://anaconda.org/conda-forge/xtb)
#  Optional
4. [Gaussian 16] (https://gaussian.com/gaussian16/)

# Installation of pyton envriromntent for LAQA confopt
1. Install anaconda3 or miniconda3
2. Creaate python 3.7 virtual environment
   $ conda create -n py37-laqa python=3.7
   $ conda activate py37-laqa
   $ conda install -c rdkit rdkit
   $ conda install -c conda-forge xtb

# How to run LAQA confopt job

# Conformation optimization of Alanine dipeptide with GFN2-xTB
1. Move working dirctory
   $ cd ./examples/laqa_confopt/ala-dip-100_uff_gfn2-xtb
2. Set environmental variables for xTB code (bash or ksh cases).
   $ export OMP_NUM_THREADS=8
   $ export OMP_STACKSIZE=2GB
3. Run python script ForGetinput.py with input file laqa_confopt_uff_gfn2-xtb.inp
   $ python /path/to/laqa_optconf_py3/ForGetinput.py laqa_confopt_uff_gfn2-xtb.inp

# Conformation optimization of Alanine dipeptide with wB97XD/6-31G(d)
# (Note: Instalattion of Gaussian 16 and modification of input file laqa_confopt_uff_wb97xd-6-31gd.inp required)
1. Move working dirctory
   $ cd ./examples/laqa_confopt/ala-dip-100_uff_wb97xd
2. Run python script ForGetinput.py with input file laqa_confopt_uff_wb97xd-6-31gd.inp
   $ python /path/to/laqa_optconf_py3/ForGetinput.py laqa_confopt_uff_wb97xd-6-31gd.inp
