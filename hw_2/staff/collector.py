"""Make CSV with some data about all files in directory"""

from datetime import datetime
import csv
import os
from os.path import join, getsize, islink, getmtime, getctime

class Collector:
    """Make CSV with some data about all files in directory"""

    def __init__(self, path_from: str = '/'):
        self.path_from = path_from
        self._headers = ('Name', 'Full_path', 'Size_bytes',
                         'Create', 'Modifying')
        self.full_paths = []
        self._file = str()
        self._dirpath = str()
        self._filenames = str()

    def _symlink_filter(self):
        """Отбор путей, не являющихся символическими ссылками"""
        self.full_paths = list(filter(lambda x: not islink(
            x), [join(self._dirpath, self._file) for self._file in self._filenames]))

        return self.full_paths

    def _scan_dir(self):

        self._filenames = self._symlink_filter()

        for self._file in self._filenames:
            yield {'Name': self._file.split('/')[-1],
                   'Full_path': self._file,
                   'Size_bytes': getsize(self._file),
                   'Create': datetime.fromtimestamp(getctime(self._file)).date(),
                   'Modifying': datetime.fromtimestamp(getmtime(self._file)).date()
                   }

    def collect(self):
        """Colllect data from directories and make CSV file"""
        for self._dirpath, _, self._filenames in os.walk(self.path_from):
            with open('foo.csv', 'a') as self.f:
                self.writer = csv.DictWriter(self.f, fieldnames=self._headers)
                self.writer.writeheader()
                for self.i in self._scan_dir():
                    self.writer.writerow(self.i)


cl = Collector('/home/furyseer/Загрузки/')

cl.collect()
