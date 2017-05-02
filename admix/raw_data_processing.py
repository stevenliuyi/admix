import csv
import numpy as np

# convert 23andme raw data
def twenty_three_and_me(data_file_name):
    processed_data = {}
    with open(data_file_name, 'r') as data:
        data = csv.reader(data, delimiter='\t')
        for row in data:
            # make sure the genotype is valid
            if len(row) == 4 and row[-1][-1] in ['A','T','G','C']:
                processed_data[row[0]] = row[-1]

    return processed_data

# convert the raw genome uata to a dict
def read_raw_data(data_format, data_file_name = None):
    if data_format == "23andme":
        if not data_file_name is None:
            return twenty_three_and_me(data_file_name)
        else:
            return twenty_three_and_me("../data/demo_genome_23andme.txt")
    else:
        print("Data format does not exist!")
        return {}

# convert alleles information of a model to a dict
def read_model(model):
    if model == 'K7b':
        snp_file_name = 'K7b.alleles'
        frequency_file_name = 'K7b.7.F'
    elif model == 'K12b':
        snp_file_name = 'K12b.alleles'
        frequency_file_name = 'K12b.12.F'
    elif model == 'E11':
        snp_file_name = 'E11.alleles'
        frequency_file_name = 'E11.11.F'
    elif model == 'globe13':
        snp_file_name = 'globe13.alleles'
        frequency_file_name = 'globe13.13.F'
    elif model == 'globe10':
        snp_file_name = 'globe10.alleles'
        frequency_file_name = 'globe10.10.F'
    else:
        print("Model does not exist!")

    # read SNPs
    snp = []
    minor_alleles = []
    major_alleles = []
    with open('../data/' + snp_file_name, 'r') as snp_file:
        snp_file = csv.reader(snp_file, delimiter=' ')
        for row in snp_file:
            snp.append(row[0])
            minor_alleles.append(row[1])
            major_alleles.append(row[2])

    # read frequency matrix 
    frequency = []
    with open('../data/' + frequency_file_name, 'r') as frequency_file:
        frequency_file = csv.reader(frequency_file, delimiter=' ')
        for row in frequency_file:
            frequency.append([float(f) for f in row])

    return np.array(snp), np.array(minor_alleles), np.array(major_alleles), np.array(frequency)
