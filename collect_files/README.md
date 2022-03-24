# collect_files
Collect files given in a file list from a source directory, and save them into a target directory.

## Usage

```python
python collect_files.py file_list.txt src_dir tgt_dir [--keep-dirs] [--no-progress-bar]
```

Copy files given in the `file_list.txt` (located in `src_dir`) to `tgt_dir`.

`--keep-dirs`: Keep the relative directory path with respect to `src_dir` for the copied files in `tgt_dir`.

`--no-progress-bar`: disable tqdm progress bar. 