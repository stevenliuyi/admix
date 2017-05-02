from admix_fraction import admix_fraction
import admix_models

def admix_results(models, raw_data_format, raw_data_file=None):
    for model in models:
        print('Model: ' + model)
        admix_frac = admix_fraction(model, raw_data_format, raw_data_file)
        populations = admix_models.populations(model)
        for (i, frac) in enumerate(admix_frac):
            print('{:s}: {:.2f}%'.format(populations[i], 100*frac))
        print('\n')

models = ['K7b', 'K12b', 'E11', 'globe13', 'globe10', 'world9', 'Eurasia7', 'Africa9', 'weac2']
raw_data_format = '23andme'

admix_results(models, raw_data_format)
