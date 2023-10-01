"""Скрипт считает число файлов, содержащихся в index.csv"""

import pandas as pd
from datetime import datetime, date, timedelta
import os
from os.path import getctime
from top_files_by_size import prog_exe_time


def f_count() -> int:
    """Считает число файлов"""

    index = pd.read_csv('../data/index.csv', usecols=['Name'], engine='pyarrow')

    return len(index.index)


if __name__ == '__main__':

    if not os.path.exists('../data/index.csv'):
        print('You need to create index.csv file')
        
    else:
        if (datetime.fromtimestamp(getctime('../data/index.csv')).date() - date.today()) > timedelta(days=2):
            print('Probably you need to update index.CSV file')

        result = prog_exe_time(f_count)
        
        print(f'Число файлов - {result[1]} шт')
        print(f"Время выполнения программы : {result[0]} сек.")
