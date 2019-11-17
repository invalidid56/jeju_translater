import os
import json

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

    ex_path = input('Input Path to Save Experiment Result and Temp Data: ').replace('~', os.path.expanduser('~'))
    # TODO: excep. if not LINUX?
    config['EX_HOME'] = ex_path
    data_path = input('Input Path to Read Corpora: ').replace('~', os.path.expanduser('~'))
    config['DATA_HOME'] = data_path

    gpu = int(input('Input Number of GPUs to Use(if none, 0): '))
    config['GPU'] = gpu

    batch_size = int(input('Input Size of Minibatch to Use(if none, 0): '))
    config['BATCH'] = batch_size

    eval_step = int(input('Input Step to Evaluate(if none, 0): '))
    config['EVAL'] = eval_step
    train_step = int(input('Input Whole Step to Train(if none, 0): '))
    config['TRAIN'] = train_step

    with open(os.path.join(os.getcwd(), config_file), 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent='\t')


if __name__ == '__main__':
    main()
