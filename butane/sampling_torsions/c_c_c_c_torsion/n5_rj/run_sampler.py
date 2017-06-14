import torsionfit.backends.sqlite_plus as sqlite_plus
from pymc import MCMC
from parmed.charmm import CharmmParameterSet
from torsionfit.database import qmdatabase as ScanSet
import torsionfit.model as Model
import torsionfit.parameters as par
try:
    import cPickle as pickle
except:
    import pickle as pickle


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run sampler on toy model')
    parser.add_argument('-rj', '--reversible_jump', type=lambda s: s.lower() in ['true', 't', 'yes', '1'],
                        help="Flag if sampler should use reversible jump")
    parser.add_argument('-s', '--init', type=lambda s: s.lower() in ['true', 't', 'yes', '1'],
                        help="initial torsion parameters guess. If not specified will be randomly generated")
    parser.add_argument('-d', '--db_name', type=str, default='butane.db',
                        help='name of sqlite database to store samples')
    parser.add_argument('-i', '--iterations', type=int, default=10000,
                        help='How many iterations to run')
    parser.add_argument('-r', '--repeats', type=int,
                        help='number of repeat')

    args = parser.parse_args()
    print(args)

    param_to_opt=[('CG331', 'CG321', 'CG321', 'CG331')]
    param = CharmmParameterSet('../../../../../../data/charmm_ff/top_all36_cgenff.rtf',
                               '../../../../../../data/charmm_ff/par_all36_cgenff.prm')
    structure = '../../../../../structure/butane.psf'
    scan = '../../../../../torsion_scans/MP2_torsion_scan/'

    # paramterize using end of non reversible jump
    # Start sampler with values from end of non-rj chain.
    path = '../../../n5/10000/random_{}_{}/random_{}_{}.sqlite'.format(args.iterations, args.repeats,  args.iterations,
                                                                       args.repeats)
    print(path)
    db = sqlite_plus.load(path)
    par.add_missing(param_list=param_to_opt, param=param, sample_n5=True)
    par.set_phase_0(param_list=param_to_opt, param=param)
    par.update_param_from_sample(param_list=param_to_opt, param=param, db=db, i=-1, rj=False, n_5=True, phase=False)
    print(param.dihedral_types[param_to_opt[0]])

    butane_scan = ScanSet.parse_psi4_out(scan, structure)
    optimized = butane_scan.remove_nonoptimized()

    model = Model.TorsionFitModel(param=param, frags=optimized, init_random=False,
                                  param_to_opt=param_to_opt, rj=True, sample_n5=True)
    sampler = MCMC(model.pymc_parameters, db=sqlite_plus, dbname=args.db_name, verbose=5)

    sampler.sample(args.iterations)


