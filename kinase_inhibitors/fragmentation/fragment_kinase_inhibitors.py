from openeye import oechem, oedepict
import pandas as pd
from openmoltools.openeye import get_charges, smiles_to_oemol
from torsionfit.qmscan import fragment


# Import FDA approved kinase inhibitors (As of Jan 2018)
kinase_inhibitors = pd.read_csv('../clinical-kinase-inhibitors.csv')

for i, inhibitor in kinase_inhibitors.iterrows():
    print('Fragmenting {}'.format(inhibitor['inhibitor']))
    mol = smiles_to_oemol(inhibitor['smiles'])
    charged, frags = fragment.generate_fragments(mol)
    oname = '{}.pdf'.format(inhibitor['inhibitor'])
    fragment.ToPdf(charged, oname, frags)