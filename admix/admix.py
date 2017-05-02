from admix_fraction import admix_fraction

def model_populations(model):
    if model == 'K7b':
        return ['South Asian',
                'West Asian',
                'Siberian',
                'African',
                'Southern',
                'Atlantic Baltic',
                'East Asian']
    elif model == 'K12b':
        return ['Gedrosia',
                'Siberian',
                'Northwest African',
                'Southeast Asian',
                'Atlantic Med',
                'North European',
                'South Asian',
                'East African',
                'Southwest Asian',
                'East Asian',
                'Caucasus',
                'Sub Saharan']
    elif model == 'E11':
        return ['African',
                'European',
                'India',
                'Malay',
                'South Chinese Dai',
                'Southwest Chinese Yi',
                'East Chinese',
                'Japanese',
                'North Chinese Oroqen',
                'Yakut',
                'American']
    elif model == 'globe13':
        return ['Siberian',
                'Amerindian',
                'West African',
                'Palaeo African',
                'Southwest Asian',
                'East Asian',
                'Mediterranean',
                'Australasian',
                'Artic',
                'West Asian',
                'North European',
                'South Asian',
                'East African']
    elif model == 'globe10':
        return ['Ameriandian',
                'West Asian',
                'Australasian',
                'Palaeo African',
                'Neo African',
                'Siberian',
                'Southern',
                'East Asian',
                'Atlantic Baltic',
                'South Asian']
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
        print('\n')

models = ['K7b', 'K12b', 'E11', 'globe13', 'globe10']
raw_data_format = '23andme'

admix_results(models, raw_data_format)
