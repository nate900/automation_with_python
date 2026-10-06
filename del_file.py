import os
import sys
from pathlib import Path
import shutil
# variables
file_name = ''


# get file name from command line argurments
if len(sys.argv) > 1:
    file_name = sys.argv[1] # only accept the argument directly after the py command
    if file_name.casefold() == 'file'.casefold():
        with open('file_name.txt', 'r', encoding='utf') as file:
            file_names = file.readlines()
            for file_name in file_names:
                file_name = file_name.strip()
                if os.path.exists(file_name):
                    # test to see if it is a dir
                    file_name_path = Path(file_name)
                    if file_name_path.is_dir():
                        # this is a directory
                        shutil.rmtree(file_name_path)
                        print(f'directory deleted at {file_name_path}')
                    else:
                        os.unlink(file_name)
                        print(f'deleted file "{file_name}"')
                else:
                    print(f'file at {file_name} does not exist\nno file deleted\ncheck your file name')
else:
    print('enter a file name you want to delete in the cwd')
    exit(1)

