import csv
import numpy as np
import os
import admix_models

# check if file exits
def check_file(file_name):
    if not os.path.isfile(file_name):
        print('Cannot find the file \'' + file_name + '\'!\n')
        exit()

# convert 23andme raw data
def twenty_three_and_me(data_file_name):
    check_file(data_file_name)
    processed_data = {}
    with open(data_file_name, 'r') as data:
        data = csv.reader(data, delimiter='\t')
        for row in data:
            # make sure the genotype is valid
            if len(row) == 4 and row[-1][-1] in ['A','T','G','C']:
                processed_data[row[0]] = row[-1]

    return processed_data

# convert AncestryDNA raw data
def ancestry(data_file_name):
    check_file(data_file_name)
    processed_data = {}
    with open(data_file_name, 'r') as data:
        data = csv.reader(data, delimiter='\t')
        for row in data:
            # make sure the genotype is valid
            if len(row) == 5 and row[-1] in ['A','T','G','C']:
                # combine alleles into genotype
                processed_data[row[0]] = ''.join(row[-2:])

    return processed_data

# convert the raw genome uata to a dict
def read_raw_data(data_format, data_file_name = None):
    if data_format == "23andme":
        if not data_file_name is None:
            return twenty_three_and_me(data_file_name)
        else:
            return twenty_three_and_me(os.path.join(os.path.dirname(__file__), "data/demo_genome_23andme.txt"))
    elif data_format == 'ancestry':
        if not data_file_name is None:
            return ancestry(data_file_name)
        else:
            print("Data file not set!")
            exit()
            return None
    else:
        print("Data format does not exist!")
        exit()
        return None

# convert alleles information of a model to a dict
def read_model(model):
    # obtain model file names
    snp_file_name = admix_models.snp_file_name(model)
    frequency_file_name = admix_models.frequency_file_name(model)

    # read SNPs
    snp = []
    minor_alleles = []
    major_alleles = []

    with open(os.path.join(os.path.dirname(__file__), 'data/' + snp_file_name), 'r') as snp_file:
        snp_file = csv.reader(snp_file, delimiter=' ')
        for row in snp_file:
            snp.append(row[0])
            minor_alleles.append(row[1])
            major_alleles.append(row[2])

    # read frequency matrix 
    frequency = []
    with open(os.path.join(os.path.dirname(__file__), 'data/' + frequency_file_name), 'r') as frequency_file:
        frequency_file = csv.reader(frequency_file, delimiter=' ')
        for row in frequency_file:
            frequency.append([float(f) for f in row])

    return np.array(snp), np.array(minor_alleles), np.array(major_alleles), np.array(frequency)
