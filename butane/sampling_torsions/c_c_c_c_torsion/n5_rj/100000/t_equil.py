from pymbar.timeseries import detectEquilibration
import tqdm
import numpy as np
from torsionfit.backends import sqlite_plus
from collections import OrderedDict

# load database
dbs = OrderedDict()
for i in range(1, 24):
    dbs['db_{}'.format(i)] = sqlite_plus.load('random_100000_{}/random_100000_{}.sqlite'.format(i, i))

t_sigma = np.zeros((23, 3))
for i, db in tqdm.tqdm(enumerate(dbs)):
    [t, g, Neff] = detectEquilibration(dbs[db].sigma[:])
    t_sigma[i, 0] = t
    t_sigma[i, 1] = g
    t_sigma[i, 2] = Neff

np.save('t_sigma', t_sigma)

t_dev = np.zeros((23, 3))
for i, db in tqdm.tqdm(enumerate(dbs)):
    [t, g, Neff] = detectEquilibration(dbs[db].deviance[:])
    t_dev[i, 0] = t
    t_dev[i, 1] = g
    t_dev[i, 2] = Neff

np.save('t_dev', t_dev)