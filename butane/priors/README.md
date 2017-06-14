### Prior on Force constant K.

When a uniform prior is used on K, multiplicty bitstrings have very slow mixing. 
This happens because when a term is turned off, the K is decoupled from the
likelihood and it samples the prior. When the term is then turned on, the value
of K is too large to be accepted. When a Gaussian prior with a mu of zero
is used, the mixing of the multiplicity term is dependent on tau. When tau is 
too small, mixing is poor. It improves with increasing tau. However, when tau is 
too big, the sampler ends up just sampling the prior since a very large tau 
introduces strong bias. 

[This](https://github.com/ChayaSt/torsionfit_examples/blob/butane/butane/priors/gaussian/deviance.pdf) is a plot of the mean and std of the deviance over 40 runs. As tau
gets bigger, the deviance decreases.

When tau is a nuisance parameter with a Jefferey prior, the mixing of multiplicity terms is 
good too, however, there are several runs where the sampler converges to a more complex
model. When the initial tau is large (to allow easier mixing in the beginning of the MCMC chain),
more runs converge to a less complex model.

[This](https://github.com/ChayaSt/torsionfit_examples/blob/butane/butane/priors/gaussian/deviance_nuisance.pdf) figure plots the deviance over 40 runs with tau as a nuisance parameter. 
When the initial value is large, the variance is smaller. 

[This](https://github.com/ChayaSt/torsionfit_examples/blob/butane/butane/priors/gaussian/multiplicity_mode_tau_nuisance.pdf) figure is a histogram of the modes of the multiplicity bitstring
from all 40 runs. 32 adn 64 are equivalent models, but 32 is less complex (it does not have an n=6 with K=0). 
When the initial value of tau is large, more of the runs converge to bitstring 32. 
