## Generate conformers for QM torsion scan

For molecules with <= 2 rotors, generate conformers with specific torsion angle intervals.
If 1 rotor, generate 1D torsion scan (24 conformers if use 15 degree interval) 
For 2 rotors, generate 2D torsion scan (24^2 if using 15 degreee interval)

### Manifest
* `generate_1d_scan.py` - script to generate 1D torsion scans
* `1D_scan/` - `generate_1d_scan.py` output files
The files in `1D_scan/` are organized as follows:
* `1D_scan/`
    * `1rotor_n/` where n is the index of the fragment
        * `1rotor_n.png` - png image of fragment with atoms labeled by indices (index origin = 0)
        * `m_m_m_m/` indices of torsion atoms (index origin = 1)
            * `a/` torsion angle
                * `1rotor_n_m_m_m_m_a.pdb` - pdb file of input coordinates for QM geometry optimization. 
        
