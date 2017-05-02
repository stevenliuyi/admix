import numpy as np
import scipy.optimize as optimize
from raw_data_processing import read_raw_data, read_model

# return the number of populations in the model
def n_populations(model):
    if model == 'K7b':
        return 7
    elif model == 'K12b':
        return 12
    elif model == 'E11':
        return 11
    elif model == 'globe13':
        return 13
    elif model == 'globe10':
        return 10
    else:
        print("Model does not exist!")
        return None

# genotype matches
def genotype_matches(genome_data, snp, major_alleles, minor_alleles):
    g_major1 = [(genome_data.get(snp[i],'-')[0] == a) for (i,a) in enumerate(major_alleles)]
    g_major2 = [(genome_data.get(snp[i],'-')[-1] == a) for (i,a) in enumerate(major_alleles)]
    g_major = np.array(g_major1).astype(int) + np.array(g_major2).astype(int)

    g_minor1 = [(genome_data.get(snp[i],'-')[0] == a) for (i,a) in enumerate(minor_alleles)]
    g_minor2 = [(genome_data.get(snp[i],'-')[-1] == a) for (i,a) in enumerate(minor_alleles)]
    g_minor = np.array(g_minor1).astype(int) + np.array(g_minor2).astype(int)
    
    return g_major, g_minor

# log likelihood function
def likelihood(g_major, g_minor, frequency, admixture_fraction):
    l1 = np.dot(g_major, np.log(np.dot(frequency, admixture_fraction)))
    l2 = np.dot(g_minor, np.log(np.dot(1-frequency, admixture_fraction)))
    l = l1 + l2
    # add minus sign so we can minimize the function instead of maximize
    return -l

# obtain admixture fraction by applying the maximum likelihood estimation
def admix_fraction(model, raw_data_format, raw_data_file=None):
    genome_data = read_raw_data(raw_data_format, raw_data_file)
    snp, minor_alleles, major_alleles, frequency = read_model(model)
    g_major, g_minor = genotype_matches(genome_data, snp, major_alleles, minor_alleles)

    # set initial guess for optimization
    initial_guess = np.ones(n_populations(model)) / n_populations(model)

    # constraints of admixture fractions
    bounds = tuple((0,1) for i in range(n_populations(model)))
    constraints = ({'type':'eq', 'fun': lambda af: np.sum(af)-1})

    # MLE
    likelihood_func = lambda af: likelihood(g_major, g_minor, frequency, af)
    admix_frac = optimize.minimize(likelihood_func, initial_guess, bounds=bounds, constraints=constraints, tol=1e-3).x

    return admix_frac
