from admix_fraction import admix_fraction

def model_populations(model):
    if (model == 'K7b'):
        return ['South Asian',
                'West Asian',
                'Siberian',
                'African',
                'Southern',
                'Atlantic Baltic',
                'East Asian']
    else:
        print('Model does not exist!')
        return None

def admix_results(models, raw_data_format, raw_data_file=None):
    for model in models:
        print('Model: ' + model)
        admix_frac = admix_fraction(model, raw_data_format, raw_data_file)
        populations = model_populations(model)
        for (i, frac) in enumerate(admix_frac):
            print('{:s}: {:.2f}%'.format(populations[i], 100*frac))

models = ['K7b']
raw_data_format = '23andme'

admix_results(models, raw_data_format)
