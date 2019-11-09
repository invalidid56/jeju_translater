import os
import json
import sys

from collections import OrderedDict


def main():
    config_file = 'config.json'
    config = OrderedDict()

    if not os.path.exists(os.path.join(os.getcwd(), config_file)):
        print('Configuration not Detected, Creating...')
    else:
        print('Deleting Previous Configuration')
        os.remove(os.path.join(os.getcwd(), config_file))

    print('Input Blank if You Want to Edit Configuration Later.')

    ex_path = input('Input Path to Save Experiment Result and Temp Data: ') # TODO: make ~ to home directory
    config['EX_HOME'] = ex_path
    data_path = input('Input Path to Read Corpora: ')
    config['DATA_HOME'] = data_path

    with open(os.path.join(os.getcwd(), config_file), 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent='\t')


if __name__ == '__main__':
    main()