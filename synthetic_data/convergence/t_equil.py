from torsionfit.backends import sqlite_plus
from pymbar.timeseries import detectEquilibration
import numpy as np
import os
from fnmatch import fnmatch
import tqdm

def get_models(directory, pattern):
    models = []
    for path, subdir, files in os.walk(directory):
        for name in files:
            if fnmatch(name, pattern):
                file = os.path.join(os.getcwd(), path, name)
                model = sqlite_plus.load(file)
                models.append(model)
    return models

pattern = 'toy.db*'

models = get_models('discrete', pattern)
t_equil = np.zeros((len(models), 3))

for i, model in tqdm.tqdm(enumerate(models)):
    print(i)
    t_equil[i] = detectEquilibration(model.sigma[:])

np.save('discrete', t_equil)