'''Help functioons for other utils'''

import time
import os
import sys
from datetime import datetime, date, timedelta
from os.path import getctime
sys.path.insert(0,"..")
from staff.collector import Collector


def prog_exe_time(func, *arguments):
    """Возвращается время работы программы и результат работы функции"""
    start = time.time()
    func_result = func(*arguments)
    end = time.time()
    return round(end-start, 2), func_result


def check_and_run(args_index, args_question, args_path, func, arguments):
    '''Проверяет существование индекса по пути и запускает утилиту''' 
    
    if not os.path.exists(args_index):

        print('You need to create index file or set index file path')
        print('\n')

        if args_question is None:
            arguments[0] = args_index = input('Which path do you want to set for index file? (default - ../data/index.csv) ') or '../data/index.csv'
            print('\n')

        if not os.path.exists(args_index):    
            print('You need to create index file')

            if args_question is None:
                args_question = input('Do you want make index file? [y, n] ')
                print('\n')

            if args_question == 'y':
                args_path = input('Which path do you want to start? ')
                cl = Collector(args_path, args_index)
                print(f'Collecting files from {args_path}, wait...')
                cl.collect()
                print('All files are collected! Now you could start to use function')

            else:
                with open('../fun/ysnp.txt', 'r', encoding='utf-8') as file:
                    for row in file:
                        print(row, end='')
                print('\n')

        else:
            if datetime.fromtimestamp(getctime(args_index)).date() - date.today() > timedelta(days=2):
                print('Probably you need to update index file')

            result = prog_exe_time(func, *arguments)

            print("Result:", end='\n\n')
            print(result[1])
            print(f"Время выполнения программы : {result[0]} сек.")

    else:

        if datetime.fromtimestamp(getctime(args_index)).date() - date.today() > timedelta(days=2):
            print('Probably you need to update index file')

        result = prog_exe_time(func, *arguments)

        print("Result:", end='\n\n')
        print(result[1])
        print(f"Время выполнения программы : {result[0]} сек.")
