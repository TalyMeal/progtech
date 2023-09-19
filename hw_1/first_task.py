import os
from os.path import join, getsize

for root, dirs, files in os.walk('/home/furyseer/'):
    print(f'root: {root}')
    print(f'directories: {dirs}')
    os.system(f'find {root} -xtype l -delete')
    print(f'files: {files}')
    for file in files:
        print(f'size: {getsize(f"{root}/{file}")}')
