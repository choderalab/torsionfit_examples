## Fragmenting Kinase Inhibitors

The fragmentation scheme in `torsionfit` uses the following algorithm.

For every rotatable bond:
* Grow out one bond in every direction
* If the atom in part of a ring, keep the ring
* If the atom is part of a functional group that we do not want to fragment, keep the functional group 
   the list is given in a yaml file in [`torsionfit/qmscan/fgroup_smarts.yml`](https://github.com/ChayaSt/torsionfit/blob/fragment/torsionfit/qmscan/fgroup_smarts.yml)
* For substituents on ring keep:
    - Non rotatable substituents
    - keep functional groups or rings that are ortho to the rotatable bond
* After growing out one bond, check the Wiberg bond order of the next bond. 
If it is more than a give threshold, continue to the next bond (recursively)
 
## Manifest
* `fragment_kinase_inhibitors.py` - script for fragmenting molecules. 
