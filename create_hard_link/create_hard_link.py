import os
import argparse


def __hard_link_dirs(src_dir, tgt_dir):
    # assume that src_dir is a directory, and tgt_dir does not exist.
    for root_dir, _, files in os.walk(src_dir):
        relative_root_dir = os.path.relpath(root_dir, src_dir)
        target_root_dir = os.path.join(tgt_dir, relative_root_dir)
        os.makedirs(target_root_dir, exist_ok=True)
        for file_name in files:
            file_path = os.path.join(root_dir, file_name)
            relative_file_path = os.path.relpath(file_path, src_dir)
            target_file_path = os.path.join(tgt_dir, relative_file_path)
            os.link(file_path, target_file_path)
    return 0


def create_hard_link(src, tgt):
    try:
        assert os.path.exists(src), "Source %s does not exist." % src
        assert not os.path.exists(tgt), "Target %s exists." % tgt
        if os.path.isdir(src):
            return __hard_link_dirs(src, tgt)
        elif os.path.isfile(src):
            target_dirname = os.path.dirname(tgt)
            if target_dirname == '':
                pass
            else:
                os.makedirs(target_dirname, exist_ok=True)
            os.link(src, tgt)
            return 0
        else:
            raise ValueError
    except:
        return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('tgt')

    args = parser.parse_args()

    return create_hard_link(args.src, args.tgt)


if __name__ == '__main__':
    main()
