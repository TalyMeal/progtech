"""Скрипт считает число файлов, содержащихся в index.csv"""

import os
import sys
import argparse
from datetime import datetime, date, timedelta
from os.path import getctime
import pandas as pd
from top_files import prog_exe_time
sys.path.insert(0,"..")
from staff.collector import Collector

def f_count() -> int:
    """Считает число файлов"""
    index = pd.read_csv('../data/index.csv', usecols=['Name'], engine='pyarrow')

    return len(index.index)

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
            print('All files are collected! Now you could start to use files_count function')

        else:
            with open('../fun/ysnp.txt', 'r', encoding='utf-8') as file:
                for row in file:
                    print(row, end='')
            print('\n')

    else:
        if (datetime.fromtimestamp(getctime('../data/index.csv')).date() - date.today()) > timedelta(days=2):
            print('Probably you need to update index.csv file')

        result = prog_exe_time(f_count)
        print(f'Число файлов - {result[1]} шт')
        print(f"Время выполнения программы : {result[0]} сек.")
