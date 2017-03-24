from torsionfit.toy_model import ToyModel
import torsionfit.backends.sqlite_plus as db
from pymc import MCMC
from parmed.topologyobjects import DihedralType, DihedralTypeList
from pymbar.timeseries import detectEquilibration
import numpy as np
try:
    import cPickle as pickle
except:
    import pickle as pickle


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run sampler on toy model')
    parser.add_argument('-a', '--nparray', type=str,
                        help='Name of file where numpy array is stored')
    parser.add_argument('-rj', '--reversible_jump', type=bool, default=True,
                        help="Flag if sampler should use reversible jump")
    parser.add_argument('-p', '--phase', type=bool, default=False,
                        help="Flag if phases should be sampled")
    parser.add_argument('-c', '--continuous', type=bool, default=False,
                        help="Flag if phase proposal distribution should be continuous")
    parser.add_argument('-n', '--n_increments', type=int, default=18,
                        help="")
    parser.add_argument('-i', '--init', type=str, default=None,
                        help="initial torsion parameters guess. If not specified will be randomly generated")
    parser.add_argument('-t', '--true', type=str, default=None,
                        help="True value of dihedral parameters. If not specified, will be randomly generated")
    parser.add_argument('-d', '--db_name', type=str, default='toy.db',
                        help='name of sqlite database to store samples')
    parser.add_argument('-r', '--repeats', type=int, default=10,
                        help='How many toy models to samples')
    parser.add_argument('-s', '--iterations', type=int, default=10000,
                        help='How many iterations to run')

    args = parser.parse_args()
    t_equil = np.zeros((args.repeats, 4))
    torsion_params = np.ones(shape=(args.repeats, 2, 6, 3))*np.nan
    if args.init is not None:
        args.init = args.init.split('_')
        args.init = DihedralType(per=int(args.init[0]), phi_k=float(args.init[1]), phase=float(args.init[2]))
    if args.true is not None:
        args.true = args.true.split('_')
        args.true = DihedralType(per=int(args.true[0]), phi_k=float(args.true[1]), phase=float(args.true[2]))
    for i in range(args.repeats):
        toy = ToyModel(true_value=args.true, initial_value=args.init, rj=args.reversible_jump, continuous=args.continuous,
                       n_increments=args.n_increments, sample_phase=args.phase)
        torsion_params[i] = toy.save_torsion_values()
        db_name = '{}_{}'.format(args.db_name, str(i))
        sampler = MCMC(toy.model.pymc_parameters, db=db, dbname=db_name)
        sampler.sample(iter=args.iterations)
        [t, g, N_ff] = detectEquilibration(sampler.trace('sigma')[:])
        t_equil[i, 0] = t
        t_equil[i, 1] = N_ff
        mean = np.mean(sampler.trace('sigma')[t:])
        var = np.var(sampler.trace('sigma')[t:])
        t_equil[i, 2] = mean
        t_equil[i, 3] = var
    np.save('t_equil_sigma', arr=t_equil)
    np.save('torsion_param', arr=torsion_params)

