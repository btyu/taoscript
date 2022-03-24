import os
import argparse


def dump_file_list(file_list, save_path):
    dirname = os.path.dirname(save_path)
    if dirname != '':
        os.makedirs(dirname, exist_ok=True)
    with open(save_path, 'w') as f:
        for item in file_list:
            f.write(item + '\n')


def generate_file_list(dir, suffix=None, save_path=None):
    file_list = []
    for root_dir, _, files in os.walk(dir):
        for file_name in files:
            if suffix is not None:
                skip = True
                for sf in suffix:
                    if file_name.endswith(sf):
                        skip = False
                        break
                if skip:
                    continue
            
            file_path = os.path.join(root_dir, file_name).replace('\\', '/')
            file_path = os.path.relpath(file_path, dir)
            file_list.append(file_path)
    if save_path is not None:
        dump_file_list(file_list, save_path)
    return file_list


def add_args(parser):
    parser.add_argument('dir', help='file directory')
    parser.add_argument('save_path', help='path to save_path the file list')
    parser.add_argument('--suffix', nargs='+', help='suffices of the files to be collected')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    add_args(parser)
    args = parser.parse_args()

    generate_file_list(args.dir, suffix=args.suffix, save_path=args.save_path)
