#!/bin/bash

### This script is a series of 'hadd' commands to aggregate root files of a specific sample
### Make sure to run this script from the directory where the files being added exist

echo -e "Adding TTToSemiLeptonic files together \n"
hadd nanogen_ALL_histograms.root nanogen_123_*_histograms.root 

echo -e "Done adding TTToSemiLeptonic files together \n"
echo -e "\n"
echo "Congrats, all the root files have been aggregated. Good luck with the plots!"
