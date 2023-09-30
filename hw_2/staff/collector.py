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
        self._writer = callable
        self._dict_string = {}
        self._all_files_and_full_paths = []
        self._filter_files_and_full_paths = []
        self._file = str()
        self._dirpath = str()
        self._filenames = str()

    def _symlink_filter(self):
        """Отбор путей, не являющихся символическими ссылками"""
        self._all_files_and_full_paths = [
            (self._file, join(self._dirpath, self._file)) for self._file in self._filenames]
        self._filter_files_and_full_paths = list(
            filter(lambda x: not islink(x[1]), self._all_files_and_full_paths))

        return self._filter_files_and_full_paths

    def _scan_dir_generator(self):

        self._filenames = self._symlink_filter()

        for self._file in self._filenames:
            yield {'Name': self._file[0],
                   'Full_path': self._file[1],
                   'Size_bytes': getsize(self._file[1]),
                   'Create': datetime.fromtimestamp(getctime(self._file[1])).date(),
                   'Modifying': datetime.fromtimestamp(getmtime(self._file[1])).date()
                   }

    def _write_dir_data(self):
        if not os.path.exists('../data/index.csv'):
            with open('../data/index.csv', 'w', encoding='utf-8') as self._file:
                self._writer = csv.DictWriter(
                    self._file, fieldnames=self._headers)
                self._writer.writeheader()
        else:
            with open('../data/index.csv', 'a', encoding='utf-8') as self._file:
                self._writer = csv.DictWriter(
                    self._file, fieldnames=self._headers)
                for self._dict_string in self._scan_dir_generator():
                    self._writer.writerow(self._dict_string)

    def collect(self):
        """Colllect data from directories and make CSV file"""
        if os.path.exists('../data/index.csv'):
            os.remove("../data/index.csv")
        for self._dirpath, _, self._filenames in os.walk(self.path_from):
            self._write_dir_data()


# cl = Collector('/')

# import time
# def prog_exe_time(func: callable) -> (float, any):
#     """Возвращается время работы программы и результат работы функции"""
#     start = time.time()
#     func()
#     end = time.time()
#     return round(end-start, 2)

# result = prog_exe_time(cl.collect)
# print(f"Время выполнения программы : {result} сек.")
