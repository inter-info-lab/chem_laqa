import sys
import os
import time
import datetime

from structure import MoleculeDescription, Structure
from run_utilities import detect_energy_function, optimize, check_for_kill, \
    relax_info, find_linked_params
from utilities import file2dict, set_default

import random
import numpy as np


def LAQA_initgeom(param_file):

    t_init_bgn = time.time()
    print("\nStart 3D structure initialization job at ",
          datetime.datetime.now(), '\n')

    # Decide for restart or a simple run: NYI
    #opt = simple_or_restart()

    # Build a dictionary from Initial Geometry settings of the parameter file.

    params = file2dict(param_file, ['Initial geometry'])

    dict_default = {'popsize': 100, 'max_iter': 30,
                    'iter_limit_conv': 20, 'energy_diff_conv': 0.001,
                    'cnt_max': 500, 'seed': None,
                    'energy_function': 'ff',
                    'force_field': 'uff', 'optsteps': 1000,
                    'energy_tol': 1.0-6, 'force_tol': 1.0e-4,
                    'xtb_call': 'xtb', 'gfn': '2',
                    'gauss_exedir': '~/bin/g16', 'gauss_scrdir': os.getcwd(),
                    'qcmethod': 'pm6', 'solvmethod': None, 'solvent': 'water',
                    'charge': 0, 'mult': 1,
                    'nprocs': 1, 'memory': '2GB',
                    'sdf_out': 'initial_structures.sdf', 'printlevel': 0}

    # Set defaults for parameters not defined in the parameter file.

    params = set_default(params, dict_default)
    print("params: ", params)
    energy_function = detect_energy_function(params)
    popsize = params['popsize']
    cnt_max = params['cnt_max']
    seed = params['seed']
    printlevel = params['printlevel']
    print("energy_function: " , energy_function)
    print("popsize:", popsize, "cnt_max: ", cnt_max, "seed ", seed)

    random.seed(seed)
    np.random.seed(seed=seed)

    # Set up template molecule.

    mol = MoleculeDescription(param_file)

    print("SMILES: ", mol.smiles)
    print("distance_cutoff_1: ", mol.distance_cutoff_1)
    print("distance_cutoff_2: ", mol.distance_cutoff_2)

    # Assign the permanent attributes to the molecule.

    mol.get_parameters()
    mol.create_template_sdf()
    if printlevel > 0:
        print(mol.template_sdf_string)

    # Check for potential degree of freedom related parameters.

    linked_params = find_linked_params(mol, params)
    print("Number of atoms: ", mol.atoms)
    print("Number of bonds: ", mol.bonds)

    for dof in mol.dof_names:
        print("Number of identified " + str(dof) + ": " +
              str(len(getattr(mol, dof))))
        print("Identified  " + str(dof) + ": " + str(getattr(mol, dof)))

    print("\n___Initialization of 3D structures ___\n")
    cnt = 0
    population, blacklist = [], []
    while len(population) < popsize and cnt < cnt_max:

        # Generate sensible and unique 3D structures.

        print("\n----- New trial: {:6} -----\n".format(cnt+1))
        str3d = Structure(mol)
        str3d.generate_structure()

        if not str3d.is_geometry_valid():
            print("Geometry of " + str(str3d) + " is invalid.")
        else:
            if str3d not in blacklist:

                # Perform the local optimization

                name = "initial_%d" % (len(population))
                optimize(str3d, energy_function, params, name)
                check_for_kill()
                str3d.send_to_blacklist(blacklist)
                population.append(str3d)
                print("Geometry of {} is added to the population, energy: {:.5f}"
                      .format(str(str3d), str3d.energy))
                relax_info(str3d)
            else:
                print("Geomerty of " + str(str3d) + " is fine, but already known.")
                      
        cnt += 1

    if cnt == cnt_max:
        print("\nThe allowed number of trials for building the "
              "population has been exceeded.")
    print("\n___Initialization of 3D structure completed___\n")
    print("Total number of population (vaid structures): ", len(population))

    print("\nInitial population before sorting:\nID    Energy [eV]")
    for i in range(len(population)):
        print("{:5} {:20.6f}".format(population[i].index, population[i].energy))

    population_sorted = sorted(population, key=lambda x:x.energy)

    print("\nInitial population after sorting:\nID    Energy [eV]")
          
    for i in range(len(population_sorted)):
        print("{:5} {:20.6f}".format(population[i].index, population[i].energy))
    #print("\nBlacklist: " + ', '.join([str(v) for v in blacklist]))

    t_init_end = time.time()
    print("\nFinish 3D structure initialization job at ",\
          datetime.datetime.now())
    print("Wall time of initialization job:                 {:20.2f} sec."\
          .format(t_init_end - t_init_bgn))


if __name__ == '__main__':

    param_file = sys.argv[1]
    LAQA_initgeom(param_file)
