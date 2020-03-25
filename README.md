# Processing Spectra

Here you will find two scripts that I have build to process and visualize the spectral centroid of mineral spectra.
We were interested in observing how the spectral centroid of our Mars stattelite data compared with mixtures of different laboratory spectra. 
Furthermore, we were interested in how the spectral centroid algorithm would perform for library spectra of minerals of known compositions (plotted in a ternary diagram)

Results of these scripts were published in Scheller & Ehlmann (2020), JGR. 
This directory includes the following python scripts: 

CentroidCalculations_LinearMixing_Visualization.py

MakeTernaryPlots.py
 
## CentroidCalculations_LinearMixing_Visualization

This script calculates the spectral centroid for a given wavelength range.
It also calculates linear mixtures of spectra and computes the centroid of the simulated linear mixture
Last, it provides some visualizations of these data.
I refer to Scheller & Ehlmann (2020), JGR for mathematical description and practical use of the spectral centroid algorithm.

Test data for script is found in the Data directory. 

Note that not all test data do not belong to the creator!

See directory for list of references for data.

## MakeTernaryPlots

This script can produce heat maps in a ternary (triangular) plot.
It works for visualization of data that has 2-3 positional coordinates and a data value.

You will need the package ternary in order to use this.
Install this package through anaconda: 

```bash
conda install python-ternary
```

All credit for ternary goes to github user marcharper.



 
