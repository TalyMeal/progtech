"""Make CSV with some data about all files in directory"""

import csv
import os
import logging
import sqlite3
from os.path import join, islink


def _to_db(f):
    def wrapper(self):
        con = sqlite3.connect(self.index_path)
        cur = con.cursor()
        names = ", ".join(self._headers)
        for rec in f(self):
            names = ", ".join(rec.keys())
            values = list(rec.values())
            try:
                cur.execute(f"INSERT INTO index_files ({names}) VALUES ({', '.join('?' * len(rec))})", values)
            except Exception as e:
                print(e)
                print(names)
                print(values)
        con.commit()
        con.close()
    return wrapper


class Collector:
    """Make CSV with some data about all files in directory"""
    def __init__(self, gru, path_from='/', index_path='../data/index.sqlite'):
        self.path_from = path_from
        self.index_path = index_path
        self._gru = gru
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

    @_to_db
    def _scan_dir_generator(self):
        """Make a generator with paths inside the directory excluding symbolic links"""

        self._filenames = self._symlink_filter()

        for self._file in self._filenames:
            
            try:
                yield self._gru.gru_get_meta_inf(self._file)
                
            except Exception:
                logging.exception(f"Error get {self._file} data")
                continue


    def _write_dir_data(self):
        """Write files data in directory to CSV"""
        for self._dirpath, _, self._filenames in os.walk(self.path_from):
            self._scan_dir_generator()


    def collect(self):
        """
        Collect data from directories and make CSV file
        Сreate file if not exist
        """
        if not os.path.exists(self.index_path):
            con = sqlite3.connect(self.index_path)
            cur = con.cursor()           
            cur.execute(f"CREATE TABLE index_files({', '.join(self._headers)})")
            con.commit()
            con.close()

        #     with open(self.index_path, 'w', encoding='utf-8') as self._file:
        #         self._writer = csv.DictWriter(self._file, fieldnames=self._headers)
        #         self._writer.writeheader()

        self._write_dir_data()
