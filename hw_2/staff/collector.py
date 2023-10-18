"""Make CSV with some data about all files in directory"""

# from datetime import datetime
import csv
import sys
import os
import logging
from os.path import join, islink
sys.path.insert(0,"..")
from filesmeta.gru import Gru

# как-то некрасиво - объявляя класс, подтягивать к нему другой, выполняющий какую-то работу.
# Лучше это все делать в create_collection.py, пока не нашел способ

# создали экземпляр Грю
gru = Gru()

# подтянули всех миньонов
gru.get_extensions()

class Collector:
    """Make CSV with some data about all files in directory"""
    def __init__(self, path_from='/', index_path='../data/index.csv'):
        self.path_from = path_from
        self.index_path = index_path
        self._headers = gru.clmns # список названий столбцов, который собирается при вызове get_extensions
        self._writer = callable
        self._dict_string = {}
        self._all_files_and_full_paths = []
        self._filter_files_and_full_paths = []
        self._file = str()
        self._dirpath = str()
        self._filenames = str()


    def _symlink_filter(self):
        """Get paths in directory excluding symbolic links"""

        self._all_files_and_full_paths = [join(self._dirpath, self._file) for self._file in self._filenames]

        return tuple(filter(lambda x: not islink(x), self._all_files_and_full_paths))


    def _scan_dir_generator(self):
        """Make a generator with paths inside the directory excluding symbolic links"""

        self._filenames = self._symlink_filter()

        for self._file in self._filenames:
            try:
                yield gru.gru_get_meta_inf(self._file)
                
            except Exception:
                logging.exception(f"Error get {self._file} data")
                continue


    def _write_dir_data(self):
        """Write files data in directory to CSV"""
        with open(self.index_path, 'a', encoding='utf-8') as self._file:
            self._writer = csv.DictWriter(self._file, fieldnames=self._headers)

            for self._dirpath, _, self._filenames in os.walk(self.path_from):
                for self._dict_string in self._scan_dir_generator():
                    self._writer.writerow(self._dict_string)


    def collect(self):
        """
        Collect data from directories and make CSV file
        Сreate file if not exist
        """
        if not os.path.exists(self.index_path):
            with open(self.index_path, 'w', encoding='utf-8') as self._file:
                self._writer = csv.DictWriter(self._file, fieldnames=self._headers)
                self._writer.writeheader()

        self._write_dir_data()
