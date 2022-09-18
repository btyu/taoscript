# create_hard_link
Create hard link for a file or a directory.

## Usage

```python
python create_hard_link.py src tgt
```

Create a hard link `tgt` for `src`. The source can be a directory, in which case the script creates the target directory and a hard link for each file in the source directory.
