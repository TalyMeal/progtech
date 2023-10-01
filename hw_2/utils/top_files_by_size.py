"""Скрипт возвращает N самых больших по размеру файлов"""

import pandas as pd
import time
from datetime import datetime, date, timedelta
import os
from os.path import getctime


def top_by_size() :

    index = pd.read_csv('../data/index.csv', usecols=['Name', 'Size_bytes'], engine='pyarrow')
    index = index.sort_values(by=['Size_bytes'], ascending=False).head(10).set_index(pd.Index(range(1,11)))

    return index

def prog_exe_time(func):
    """Возвращается время работы программы и результат работы функции"""
    start = time.time()
    func_result = func()
    end = time.time()
    return round(end-start, 2), func_result

if __name__=='__main__':

    if not os.path.exists('../data/index.csv'):
        print('You need to create index.csv file')
        
    else:
        if (datetime.fromtimestamp(getctime('../data/index.csv')).date() - date.today()) > timedelta(days=2):
            print('Probably you need to update index.CSV file')

        result = prog_exe_time(top_by_size)

        print(result[1], end='\n\n')
        print(f"Время выполнения программы : {result[0]} сек.")

        
