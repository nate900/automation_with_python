from pathlib import Path
import os
import shutil

cwd = Path.cwd()

downloads = Path.home() / 'Downloads'

file_names = ['api_key.txt','update_oil.py','select_oil.py','oil_change.py','del_oil.py','weather.py']
moved_files = []

if not (cwd / 'new_files').is_dir():
    print('new_files dir does not exist\ncreating now')
    (cwd / 'new_files').mkdir()
else:
    print('new_files dir does exist')

for file in file_names:
    file_path = downloads/file
    dest_path = cwd / 'new_files'
    if os.path.exists(file_path):
        moved_files.append(file)
        print(f'file {file} is in {downloads}\nmoving now...')
        shutil.move(file_path, dest_path)

if len(moved_files) == 0:
    print('no files moved\ncheck your path to see they exist there')
else:
    print(f'this is the list of files that were moved: {moved_files}')
