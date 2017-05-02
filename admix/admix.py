import argparse
from admix_fraction import admix_fraction
import admix_models

def arguments():
    # argument parser
    parser = argparse.ArgumentParser()
    
    # specify models
    parser.add_argument('-m', '--models',
                        nargs = '+',
                        help = 'specify admixure models to use (default: all available models)')

    return parser.parse_args()

# print out admixure analysis results
def admix_results(models, raw_data_format, raw_data_file=None):
    for model in models:
        print('Model: ' + model)
        admix_frac = admix_fraction(model, raw_data_format, raw_data_file)
        populations = admix_models.populations(model)
        for (i, frac) in enumerate(admix_frac):
            print('{:s}: {:.2f}%'.format(populations[i], 100*frac))
        print('\n')


# arguments
args = arguments()

# set models for calculation
all_models = admix_models.models()
if (args.models is None):
    models = all_models
else:
    models = args.models
    for m in models:
        if not m in all_models:
            print('Cannot find model ' + m + '!')
            exit()

raw_data_format = '23andme'

admix_results(models, raw_data_format)
