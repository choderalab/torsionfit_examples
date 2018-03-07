from torsionfit.qmscan import torsion_scan, utils
from openeye import oechem
import os

# Read all fragments with 1 rotor
mollist = utils.to_oemol('../fragmentation/nrotor_1.smi')

os.mkdir('1D_scan')
for i, mol in enumerate(mollist):
    base_name = '1rotor_{}'.format(str(i))
    path = '/Users/chayastern/src/ChayaSt/torsionfit_examples/kinase_inhibitors/torsion_scan/1D_scan/{}'.format(base_name)
    print(mol.GetTitle())
    os.mkdir(path)
    utils.png_atoms_labeled(oechem.OEMolToSmiles(mol), path + '/' + base_name + '.png')
    torsion_scan.generate_torsions(mol, output_path=path, interval=15, base_name=base_name)
