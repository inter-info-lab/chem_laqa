import sys
from laqa_fafoom.laqa_confopt import LAQA_confopt_main

if __name__ == '__main__':

  #  input_smiles="Cn1c2cc([C@H](CC(=O)NNC(=O)[C@@H]3C[C@@H]3C)nc3cccnc23)c2ccccc21"
  #  input_smiles="O=C(c1ccc(NC(=O)Nc2ccc(N3CCCC3)cc2)cc1)c1ccco1"
    input_smiles="c23cc1ccccc1cc2cccc3"
    LAQA_confopt_main("None", input_smiles)
