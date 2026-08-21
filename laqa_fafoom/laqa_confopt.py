# -*- coding: utf-8 -*-

"""
Global geometry optimization code using
Look Ahead based on Quadratic Approximation (LAQA) method

Coded on Feb 10 2021

@Author: Michio Katouda (RIST) base on the LAQA code
coded by Kei Terayama (Univ. Tokyo, RIKEN AIP, and Kyoto Univ.)
e-mail: katouda@rist.or.jp
"""

import sys
import os
import time
import datetime
import argparse

try:
    from qcforever import laqa_fafoom
except ImportError:
    HAS_QCFOREVER = False
    import laqa_fafoom
else:
    HAS_QCFOREVER = True


def main():

    #param_file = sys.argv[1]
    parser = argparse.ArgumentParser(
        description='Generate and search energetically favorable molecular conformations via LAQA optimization'
    )
    parser.add_argument("input", help="Input file")
    parser.add_argument(
        "-v", "--verbose", action='store_true',
        help="verbose mode"
    )
    args = parser.parse_args()
    #print(args)

    param_file = args.input
    if os.path.exists(param_file):

        t_laqaopt_bgn = time.time()
        print(f"\nStart LAQA conforation searh job at {datetime.datetime.now()}")

        laqa_fafoom.initgeom.LAQA_initgeom(param_file)
        laqa_fafoom.laqa_optgeom.LAQA_optgeom(param_file)

        t_laqaopt_end = time.time()
        print(f"\nFinish LAQA conforation searh job at {datetime.datetime.now()}")
        print(f"Wall time of LAQA conformation optimization job: {t_laqaopt_end - t_laqaopt_bgn:20.2f} sec.")
    else:
        print(f'{param_file} is not exists.')


if __name__ == "__main__":
    sys.exit(main())
