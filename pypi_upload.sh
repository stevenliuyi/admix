#!/bin/bash

# only inlude five models due to file size limit
mv admix/data admix/data_backup
mkdir admix/data
cp admix/data_backup/E11* admix/data/
cp admix/data_backup/K12b* admix/data/
cp admix/data_backup/K7b* admix/data/
cp admix/data_backup/globe13* admix/data/
cp admix/data_backup/world9* admix/data/
cp admix/data_backup/demo_genome_23andme.txt admix/data/

# create source distribution
python setup.py sdist

# upload package
twine upload dist/*

# recover original data folder
rm -rf admix/data
mv admix/data_backup admix/data
