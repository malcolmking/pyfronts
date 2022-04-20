# pyfronts
A python module to detect fronts in xarray data


This repository contains a python3 file ('fronts.py') to be used as a module to automatically detect cold, warm and stationary fronts on a range of gridded datasets, and a script that is an example of how the module can be used ('test_front.py'). The module currently relies on inputs being in xarray format.

 

This code is based on the detection method described in Berry et al. (2011), which itself was based on Hewson (1998). Note that results are more spurious towards the poles, and ideally the code should only be used between 70N and 70S.

 

The module itself has the following dependencies:

- xarray
- numpy
- scipy
- geopy
 

The example script has an additional dependency on matplotlib and cartopy for the generation of a plot.

 

Full usage documentation is yet to be created. This code has been tested and is confirmed as working on the linux system of NCI's Gadi supercomputer, as well as a local workstation running Windows 10.
