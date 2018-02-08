import pandas as pd
from torsionfit.qmscan import fragment, utils

# Import FDA approved kinase inhibitors (As of Jan 2018)
kinase_inhibitors = pd.read_csv('../clinical-kinase-inhibitors.csv')

# Generate smi input file
smiles = []
for i, inhibitor in kinase_inhibitors.iterrows():
    smiles.append("{} {}".format(inhibitor['smiles'], inhibitor['inhibitor']))

# Write out file
out_dir = '/Users/chayastern/src/ChayaSt/torsionfit_examples/kinase_inhibitors/fragmentation/'
base_fname = 'kinase_inhibitors'
input_smi = utils.to_smi(smiles, out_dir, base_fname, return_fname=True)

# Generate nrotor_N.smi files of fragments. Have the option to generate pdf file of fragments for visualization.
fragment.generate_fragments(input_smi, out_dir, pdf=True)
