import torsionfit.backends.sqlite_plus as sqlite_plus
from pymc import MCMC
from parmed.charmm import CharmmParameterSet
from torsionfit.database import qmdatabase as ScanSet
import torsionfit.model as Model
try:
    import cPickle as pickle
except:
    import pickle as pickle


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run sampler on toy model')
    parser.add_argument('-rj', '--reversible_jump', type=lambda s: s.lower() in ['true', 't', 'yes', '1'],
                        help="Flag if sampler should use reversible jump")
    parser.add_argument('-i', '--init', type=lambda s: s.lower() in ['true', 't', 'yes', '1'],
                        help="initial torsion parameters guess. If not specified will be randomly generated")
    parser.add_argument('-d', '--db_name', type=str, default='butane.db',
                        help='name of sqlite database to store samples')
    parser.add_argument('-s', '--iterations', type=int, default=10,
                        help='How many iterations to run')

    args = parser.parse_args()
    print(args)

    param_to_opt=[('CG331', 'CG321', 'CG321', 'CG331')]
    param = CharmmParameterSet('../../../../../../data/charmm_ff/top_all36_cgenff.rtf',
                               '../../../../../../data/charmm_ff/par_all36_cgenff.prm')
    structure = '../../../../../structure/butane.psf'
    scan = '../../../../../torsion_scans/MP2_torsion_scan/'

    butane_scan = ScanSet.parse_psi4_out(scan, structure)
    optimized = butane_scan.remove_nonoptimized()

    model = Model.TorsionFitModel(param=param, frags=optimized,
                                  param_to_opt=param_to_opt, rj=True, sample_n5=True)
    sampler = MCMC(model.pymc_parameters, db=sqlite_plus, dbname=args.db_name, verbose=5)

    sampler.sample(args.iterations)


