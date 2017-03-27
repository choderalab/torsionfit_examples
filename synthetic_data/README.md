# Synthetic data

This is a toy model of 4 carbon atoms with 0 charge.

## Background

The torsion functional form is: ![](torsion.png?raw=true)  

where the K is the force constant, n is the multiplicity (or label) and delta is the phase angle. 
When K is non-zero, the term contributes to the torsion energy. To preserve the symmerty of the 
function about chi=0 so that the molecule and its enantiomer have the same potential energy 
with the same K and delta, delta should be constrained to be either 0 or 180 ([Guvench et al.](https://www.ncbi.nlm.nih.gov/pubmed/18458967)).
However, changing the sign of K results in the same curve as changing delta from 
0 to 180. So we can either constrain K to only be positive, or we can eliminate the phase
altogether and allow K to also take on negative values. When phases are eliminate, 
the parameter dimensions are reduced by almost half. In principle, this should lead 
to faster sampling (when using Metropolis-Hasting) because there are less parameters to 
evaluate per iteration. 

To test this, I used a model (referred to as `discrete`) where the priors on the phases were discrete uniform
U{0, 180} and the priors on the Ks were U(0, 20), and another model (referred to as `eliminate`)
where the phase parameters were eliminated and the priors on the Ks were U(-20, 20). For completion, 
I also looked at using a continuous uniform prior on the phases (refereed to as `continuous`). 

To compare these models, I looked at how long it takes for the MCMC chains to converge. Since I was
using reversible jump to sample the labels, it wasn't practical to look at the slowest variable
since if the label for that term is off, the parameter wanders around randomly in phase space and
when the label turns back on, it's as if the chain restarts. Instead, I looked at how long it takes sigma, the nuisance 
parameter of the Gaussian error model, to equilibrate using `pymbar.timesereis.detectEquilibration`. 
This was repeated 500 times. Below is the distribution of t_equil for sigma when the true and starring values 
for all 500 repeats were the same:
![](convergence/t_equil.png?raw=true)

The distribution of t_equil for the continous model is longer than the discrete or eliminate model. 
This probably happens because with continuous phase, the phase space is much larger so it takes longer to 
transverse. 

When the true and starting values were randomized, the distributions of t_equil overlap more:
![](convergence/t_equil_rand.png?raw=true)

While the distribution of t_equl looks very similar for the eliminate and discrete model, the eliminate model 
has the advantage of having less parameters. 

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

* `convergence` - t_equil of sigma



            