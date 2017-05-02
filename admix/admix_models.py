# all models
def models():
    return ['K7b',
            'K12b',
            'E11',
            'globe13',
            'globe10',
            'world9',
            'Eurasia7',
            'Africa9',
            'weac2']

# population names for all models
def populations(model):
    if model == 'K7b':
        return [('South Asian','南亚'),
                ('West Asian','西亚'),
                ('Siberian','西伯利亚'),
                ('African','非洲'),
                ('Southern','地中海－中东'),
                ('Atlantic Baltic','大西洋波罗的海'),
                ('East Asian','东亚')]
    elif model == 'K12b':
        return [('Gedrosia','格德罗西亚'),
                ('Siberian','西伯利亚'),
                ('Northwest African','西北非'),
                ('Southeast Asian','东南亚'),
                ('Atlantic Med','大西洋地中海'),
                ('North European','北欧'),
                ('South Asian','南亚'),
                ('East African','东非'),
                ('Southwest Asian','西南亚'),
                ('East Asian','东亚'),
                ('Caucasus','高加索'),
                ('Sub Saharan','撒哈拉以南非洲')]
    elif model == 'E11':
        return [('African','非洲'),
                ('European','欧洲'),
                ('India','印度'),
                ('Malay','马来'),
                ('South Chinese Dai','傣族'),
                ('Southwest Chinese Yi','彝族'),
                ('East Chinese','华东'),
                ('Japanese','日本'),
                ('North Chinese Oroqen','鄂伦春'),
                ('Yakut','雅库特'),
                ('American','美洲')]
    elif model == 'globe13':
        return [('Siberian','西伯利亚'),
                ('Amerindian','美洲印第安'),
                ('West African','西非'),
                ('Palaeo African','旧非洲'),
                ('Southwest Asian','西南亚'),
                ('East Asian','东亚'),
                ('Mediterranean','地中海'),
                ('Australasian','澳大拉西亚'),
                ('Artic','北极'),
                ('West Asian','西亚'),
                ('North European','北欧'),
                ('South Asian','南亚'),
                ('East African','东非')]
    elif model == 'globe10':
        return [('Ameriandian','美洲印第安'),
                ('West Asian','西亚'),
                ('Australasian','澳大拉西亚'),
                ('Palaeo African','旧非洲'),
                ('Neo African','新非洲'),
                ('Siberian','西伯利亚'),
                ('Southern','地中海－中东'),
                ('East Asian','东亚'),
                ('Atlantic Baltic','大西洋波罗的海'),
                ('South Asian','南亚')]
    elif model == 'world9':
        return [('Amerindian','美洲印第安'),
                ('East Asian','东亚'),
                ('African','非洲'),
                ('Atlantic Baltic','大西洋波罗的海'),
                ('Australasian','澳大拉西亚'),
                ('Siberian','西伯利亚'),
                ('Caucasus Gedrosia','高加索－格德罗西亚'),
                ('Southern','地中海－中东'),
                ('South Asian','南亚')]
    elif model == 'Eurasia7':
        return [('Sub Saharan','撒哈拉以南非洲'),
                ('West Asian','西亚'),
                ('Atlantic Baltic','大西洋波罗的海'),
                ('East Asian','东亚'),
                ('Southern','地中海－中东'),
                ('South Asian','东亚'),
                ('Siberian','西伯利亚')]
    elif model == 'Africa9':
        return [('Europe','欧洲'),
                ('Northwest Africa','西北非'),
                ('Southwest Asia','西南亚'),
                ('East Africa','东非'),
                ('South Africa','南非'),
                ('Mbuti','姆布蒂人'),
                ('West Africa','西非'),
                ('Biaka','比亚卡人'),
                ('San','桑人')]
    elif model == 'weac2':
        return [('Palaeoafrican','旧非洲'),
                ('Atlantic Baltic','大西洋波罗的海'),
                ('Northeast Asian','东北亚'),
                ('Near East','近东'),
                ('Sub Saharan','撒哈拉以南非洲'),
                ('South Asian','南亚'),
                ('Southeast Asian','东南亚')]
    else:
        print('Model does not exist!')
        return None

# number of populations in all models
def n_populations(model):
    return len(populations(model))

# model alleles file names
def snp_file_name(model):
    return model + '.alleles'

# model frequency matrix file names
def frequency_file_name(model):
    return model + '.' + str(n_populations(model)) + '.F'
