"""Скрипт возвращает N самых больших по размеру файлов"""

import os
import sys
import time
import argparse
import pandas as pd
from datetime import datetime, date, timedelta
from os.path import getctime
sys.path.insert(0,"..")
from staff.collector import Collector

def top_by_size(top):
    """Get top 10 files"""
    index = pd.read_csv('../data/index.csv', usecols=['Name', 'Size_bytes'], engine='pyarrow')
    index = index.sort_values(by=['Size_bytes'], ascending=False).head(top).set_index(pd.Index(range(1,top+1)))

    return index

def prog_exe_time(func, *arguments):
    """Возвращается время работы программы и результат работы функции"""
    start = time.time()
    func_result = func(*arguments)
    end = time.time()
    return round(end-start, 2), func_result

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--question', 
                        '-q',
                        type=str,
                        help="Вопрос - генерировать ли файл index.csv")
    parser.add_argument('--path',
                        '-p',
                        type=str,
                        default='/',
                        help="Путь для старта. Пример: /home/{USERNAME}/Downloads/")
    parser.add_argument('--top',
                        '-t', 
                        type=int,
                        default=10,
                        help="Количество файлов для вывода. Пример: 3")        
    args = parser.parse_args()

    if not os.path.exists('../data/index.csv'):
        print('You need to create index.csv file')

        if args.question is None:
            args.question = input('Do you want make index.csv? [y, n] ')  
            print('\n')  

        if args.question == 'y':
            args.path = input('Which path do you want to start? ')
            cl = Collector(args.path)
            print(f'Collecting files from {args.path}, wait...')
            cl.collect()
            print('All files are collected! Now you could start to use top_files_by_size function')
            
        else:
            with open('../fun/ysnp.txt', 'r') as file:
                for row in file:
                    print(row, end='')
            print('\n')

    else:
        if (datetime.fromtimestamp(getctime('../data/index.csv')).date() - date.today()) > timedelta(days=2):
            print('Probably you need to update index.csv file')

        result = prog_exe_time(top_by_size, args.top)

        print(f"Top {args.top} files by size:")
        print(result[1], end='\n\n')
        print(f"Время выполнения программы : {result[0]} сек.")
