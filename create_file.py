import sys
from pathlib import Path

new_file = None
if len(sys.argv) > 1:
    new_file = Path(sys.argv[1])
else:
    print('please enter a file name')
    exit(1)

if new_file.is_file():
    print('file already exists!')
else:
    print('create new file...')
    with open(new_file, 'w', encoding='utf') as file:
        file.write('hello from the other side')