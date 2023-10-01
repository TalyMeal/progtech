"""Make CSV with some data about all files in directory"""

from datetime import datetime
import csv
import os
from os.path import join, getsize, islink, getmtime, getctime

class Collector:
    """Make CSV with some data about all files in directory"""
    def __init__(self, path_from='/'):
        self.path_from = path_from
        self._headers = ('Name', 'Full_path', 'Size_bytes',
                         'Create', 'Modifying')
        self._writer = callable
        self._dict_string = {}
        self._all_files_and_full_paths = []
        self._filter_files_and_full_paths = []
        self._file = str()
        self._dirpath = str()
        self._filenames = str()

    def _symlink_filter(self):
        """Get paths in directory excluding symbolic links"""
        self._all_files_and_full_paths = [
            (self._file, join(self._dirpath, self._file)) for self._file in self._filenames]
        self._filter_files_and_full_paths = tuple(
            filter(lambda x: not islink(x[1]), self._all_files_and_full_paths))

        return self._filter_files_and_full_paths

    def _scan_dir_generator(self):
        """Make a generator with paths inside the directory excluding symbolic links"""
        self._filenames = self._symlink_filter()

        for self._file in self._filenames:
            try:
                yield {'Name': self._file[0],
                       'Full_path': self._file[1],
                       'Size_bytes': getsize(self._file[1]),
                       'Create': datetime.fromtimestamp(getctime(self._file[1])).date(),
                       'Modifying': datetime.fromtimestamp(getmtime(self._file[1])).date()
                       }
            except:
                continue

    def _write_dir_data(self):
        """Write files data in directory to CSV"""
        with open('../data/index.csv', 'a', encoding='utf-8') as self._file:
            self._writer = csv.DictWriter(self._file, fieldnames=self._headers)

            for self._dict_string in self._scan_dir_generator():
                self._writer.writerow(self._dict_string)

    def collect(self):
        """Collect data from directories and make CSV file
        Delete CSV is exist and create and write if not exist
        """
        if os.path.exists('../data/index.csv'):
            os.remove("../data/index.csv")

        if not os.path.exists('../data/index.csv'):
            with open('../data/index.csv', 'w', encoding='utf-8') as self._file:
                self._writer = csv.DictWriter(self._file, fieldnames=self._headers)
                self._writer.writeheader()        

        for self._dirpath, _, self._filenames in os.walk(self.path_from):                   
            self._write_dir_data()
