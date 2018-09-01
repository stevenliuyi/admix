import sys, os
sys.path.append(os.path.dirname(__file__))
import argparse
from admix_fraction import admix_fraction
import admix_models
import numpy as np


def arguments():
    # argument parser
    parser = argparse.ArgumentParser()

    # raw genome data file
    parser.add_argument(
        '-f',
        '--file',
        nargs='?',
        default='',
        help='file name of the raw genome data')

    # specify models
    parser.add_argument(
        '-m',
        '--models',
        nargs='+',
        help=
        'set admixure models for calculation (default: all available models)')

    # specify raw data format
    parser.add_argument(
        '-v',
        '--vendor',
        default='23andme',
        help='set the DNA testing vendor (default: 23andme)')

    # save as a file (set the default file name when no argument provided)
    parser.add_argument(
        '-o',
        '--output',
        nargs='?',
        const='admixture_results.txt',
        help='save results as a file')

    # population description in Chinese
    parser.add_argument(
        '-z',
        '--zhongwen',
        action='store_true',
        help='display population names in Chinese')

    # tolerance of optimization
    parser.add_argument(
        '-t',
        '--tolerance',
        nargs='?',
        default='1e-3',
        help='set optimization tolerance')

    # sort admixture proportions
    parser.add_argument(
        '--sort', action='store_true', help='sort admixture proportions')

    # only display non-zero proportions
    parser.add_argument(
        '--ignore-zeros',
        action='store_true',
        help='only display non-zero proportions')

    return parser.parse_args()


# print out admixure analysis results
def admix_results(models,
                  output_filename,
                  zh,
                  tolerance,
                  sort,
                  ignore_zeros,
                  raw_data_format,
                  raw_data_file=None):
    # write results to a file
    if (output_filename is not None):
        f = open(output_filename, 'w')

    # convert tolerance to float
    try:
        tolerance = float(tolerance)
    except ValueError:
        print('Invalid tolerance!')
        exit()

    for model in models:
        result = model + '\n'
        admix_frac = np.array(
            admix_fraction(model, raw_data_format, raw_data_file, tolerance))
        populations = np.array(admix_models.populations(model))

        # perform a descending sort of the fractions
        if sort:
            idx = np.argsort(admix_frac)[::-1]
            admix_frac = admix_frac[idx]
            populations = populations[idx]

        for (i, frac) in enumerate(admix_frac):
            if ignore_zeros and frac < 1e-4: continue
            population_en, population_zh = populations[i]
            if zh == False:  # English
                population = population_en
            else:  # Chinese
                population = population_zh
            result += '{:s}: {:.2f}%'.format(population, 100 * frac) + '\n'
        result += '\n'

        # print out results
        print(result)

        # write results to file
        if (output_filename is not None):
            f.write(result)

    # close file
    if (output_filename is not None):
        print('Results are written to ' + output_filename)
        f.close()


def main():
    # get arguments
    args = arguments()

    # set models for calculation
    all_models = admix_models.models()
    if (args.models is None):
        print('\nNo model specified, all available models will be used.\n')
        models = all_models
    else:
        models = args.models
        for m in models:
            if not m in all_models:
                print('Cannot find model ' + m + '!')
                exit()
    print('\nAdmixture calculation models: ' + ','.join(models) + '\n')

    # raw data not set
    if args.file == '':
        args.file = os.path.join(
            os.path.dirname(__file__), 'data/demo_genome_23andme.txt')
        print('Raw data file not set, a demo 23andme data will be used.\n')
        # demo only provided for 23andme
        if args.vendor != '23andme':
            args.vendor = '23andme'
            print('Ignore the vendor argument (' + args.vendor +
                  ') since demo only provided for 23andme.\n')

    # beginning of calculation
    print('Calcuation is started...\n')
    admix_results(models, args.output, args.zhongwen, args.tolerance,
                  args.sort, args.ignore_zeros, args.vendor, args.file)


if __name__ == '__main__':
    main()
