### Synthetic data

This is a toy model of 4 carbon atoms with 0 charge.

### Manifest
* `toy.pdb` - pdb file of toy system
* `toy.psf` - psf file for toy system
* `gen_psf.tcl` - tcl scripte to generate psf file with vmd psfgen
* `toy.str` - self containted str file for toy model so there's no need to load entire cgenff
* `Toy_model_MLE.ipynb` - ipython notebook of MLE of parameters for toy model.

Several different conditions to fit the torsion parameters of the toy model were compared. A representative result for each are in the following
folders:
* `discrete_rj/` - Labels (multiplicities) are on and phases discrete (0,1) with 1 representing 180.
* `discrete/` - Labels are off and phases are discrete (0,1) with 1 representing 180.
* `continuous_rj/` - Labels are on and phases are continuous between 0 and 180.
* `continuous/` - Labels are off and phases are continuous between 0 and 180.
* `eliminate_rj/` - Labels are on. Force constants (Ks) can take on negative values and sampling of phases is eliminated.
all phases are set to 0. A negative K value is equivalent to a phase angle of 180.
* `eliminate/` - Labels are off. Force constants as above.

The torsion functional form is: ![](torsion.png?raw=true)                                              
            
            