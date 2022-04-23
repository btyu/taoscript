import os
import math
import argparse
from multiprocessing.sharedctypes import Value


def read_file_list(file_list):
    path_list = list()
    with open(file_list, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            path_list.append(line)
    return path_list


def dump_file_list(file_list, save_path):
    dirname = os.path.dirname(save_path)
    if dirname != '':
        os.makedirs(dirname, exist_ok=True)
    with open(save_path, 'w') as f:
        for item in file_list:
            f.write(item + '\n')


def split_list(file_path, split, save_path, verbose=False):
    assert split > 0
    item_list = read_file_list(file_path)
    num_items = len(item_list)
    each_num = num_items // split
    if each_num * split < num_items:
        each_num += 1
    batch = []
    for idx in range(split - 1):
        batch.append(item_list[idx * each_num : (idx + 1) * each_num])
    last_group = item_list[(split - 1) * each_num:]
    batch.append(last_group)
    last_num = len(last_group)
    
    if verbose:
        print('Split %d items into %d groups, with each group containing %d items' % (num_items, split, each_num), end='')
        if last_num != each_num:
            print(', except for the last containing %d items' % last_num)
        else:
            print()
    
    for idx in range(split):
        dump_file_list(batch[idx], save_path + '_%d.txt' % idx)


def add_args(parser):
    parser.add_argument('file_list', help='a file list that specify the files')
    parser.add_argument('split', type=int)
    parser.add_argument('save_path', help='path to save the result lists')
    parser.add_argument('--verbose', action='store_true')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    add_args(parser)
    args = parser.parse_args()

    split_list(args.file_list, args.split, args.save_path, verbose=args.verbose)
