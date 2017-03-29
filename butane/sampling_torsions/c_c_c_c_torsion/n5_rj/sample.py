import simtk.openmm as mm
from torsionfit.database import qmdatabase as ScanSet
import torsionfit.model as Model
from torsionfit.backends import sqlite_plus
from pymc import MCMC
from parmed.charmm import CharmmParameterSet
from torsionfit import parameters as par

param_to_opt=[('CG331', 'CG321', 'CG321', 'CG331')]
param = CharmmParameterSet('../../../../data/charmm_ff/top_all36_cgenff.rtf',
                           '../../../../data/charmm_ff/par_all36_cgenff.prm')
structure = '../../../structure/butane.psf'
scan = '../../../torsion_scans/MP2_torsion_scan/'

butane_scan = ScanSet.parse_psi4_out(scan, structure)
optimized = butane_scan.remove_nonoptimized()

# Start sampler with values from end of non-rj chain.
db = sqlite_plus.load('../n5/butane_n5_decouple_n.db')
par.add_missing(param_list=param_to_opt, param=param, sample_n5=True)
par.update_param_from_sample(param_list=param_to_opt, param=param, db=db, i=-1, rj=False, n_5=True, phase=False)

platform = mm.Platform.getPlatformByName('Reference')
model = Model.TorsionFitModel(param=param, frags=optimized, platform=platform,
                              param_to_opt=param_to_opt, rj=True, sample_n5=True)
sampler = MCMC(model.pymc_parameters, db=sqlite_plus, dbname='butane_from_no_rj.db', verbose=5)

sampler.sample(100000)
