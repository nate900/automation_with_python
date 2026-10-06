from pathlib import Path
import sys
# create a new folder given the input
new_folder = None
if len(sys.argv) > 1:
    new_folder = Path(sys.argv[1])
else:
    print('enter the folder name you want to create in your current dir')
    exit(1)


# test to see if dir already exists
if new_folder.is_dir():
    print('folder already exists!')
else:
    print('creating new folder now...')
    new_folder.mkdir()