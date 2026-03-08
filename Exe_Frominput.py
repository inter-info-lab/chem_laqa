import sys
from laqa_fafoom.laqa_confopt import LAQA_confopt_main

if __name__ == '__main__':

    param_file = sys.argv[1]
    LAQA_confopt_main(param_file)
