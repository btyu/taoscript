import os
import argparse
from multiprocessing.sharedctypes import Value


def read_file_list_set(file_list):
    path_list = set()
    with open(file_list, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            path_list.add(line)
    return path_list


def dump_file_list(file_list, save_path):
    dirname = os.path.dirname(save_path)
    if dirname != '':
        os.makedirs(dirname, exist_ok=True)
    with open(save_path, 'w') as f:
        for item in file_list:
            f.write(item + '\n')


def op_sets(s1, s2, op):
    if op == 'union':
        return s1 | s2
    elif op == 'intersection':
        return s1 & s2
    elif op == 'subtraction':
        return s1 - s2
    else:
        raise ValueError("invalid operation: %s" % op)


def intertwine_sets(s1_file, s2_file, op, save_path):
    s1 = read_file_list_set(s1_file)
    s2 = read_file_list_set(s2_file)
    r = op_sets(s1, s2, op)
    dump_file_list(r, save_path)


def add_args(parser):
    parser.add_argument('file_list_1', help='a file list that specify the files')
    parser.add_argument('op', choices=('union', 'intersection', 'subtraction'))
    parser.add_argument('file_list_2', help='a file list that specify the files')
    parser.add_argument('save_path', help='path to save the result list')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    add_args(parser)
    args = parser.parse_args()

    intertwine_sets(args.file_list_1, args.file_list_2, args.op, args.save_path)
