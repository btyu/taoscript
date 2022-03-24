import os
import argparse
from tqdm import tqdm
import shutil


def read_file_list(file_list):
    path_list = []
    with open(file_list, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            path_list.append(line)
    return path_list


def copy_files(file_list, src_dir, tgt_dir, keep_dirs=False, no_progress_bar=False):
    file_list = read_file_list(file_list)
    file_path_iter = file_list
    if not no_progress_bar:
        file_path_iter = tqdm(file_path_iter)
    for file_name in file_path_iter:
        src_file_path = os.path.join(src_dir, file_name)
        if keep_dirs:
            dst_file_path = os.path.join(tgt_dir, file_name)
        else:
            file_base_name = os.path.basename(file_name)
            dst_file_path = os.path.join(tgt_dir, file_base_name)
        dst_dir = os.path.dirname(dst_file_path)
        os.makedirs(dst_dir, exist_ok=True)
        shutil.copy(src_file_path, dst_file_path)


def add_args(parser):
    parser.add_argument('file_list', help='a file list that specify the files to be collected using their relative paths wrt src_dir')
    parser.add_argument('src_dir', help='source directory')
    parser.add_argument('tgt_dir', help='target directory')
    parser.add_argument('--keep-dirs', action='store_true', help='keep the relative directory path wrt src_dir for the copied files in tgt_dir')
    parser.add_argument('--no-progress-bar', action='store_true', help='disable tqdm progress bar')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    add_args(parser)
    args = parser.parse_args()

    copy_files(args.file_list, args.src_dir, args.tgt_dir, keep_dirs=args.keep_dirs, no_progress_bar=args.no_progress_bar)
