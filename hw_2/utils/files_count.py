"""Скрипт считает число файлов, содержащихся в index.csv"""

import argparse
import pandas as pd
from help_functions import check_and_run

def f_count(args_index) -> int:
    """Считает число файлов"""
    index = pd.read_csv(args_index, usecols=['Name'], engine='pyarrow')

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
    parser.add_argument('--index',
                        '-i',
                        type=str,
                        default='../data/index.csv',
                        help="Абсолютный путь для индекса файлов. Пример: /home/{USERNAME}/Documents/index.csv По умолчанию - ../data/index.csv")     
    args = parser.parse_args()

    check_and_run(args.index, args.question, args.path, f_count, [args.index])

    # if not os.path.exists(args.index):

    #     print('You need to create index.csv file or set file path')
    #     print('\n')

    #     if args.question is None:
    #         args.index = input('Which path do you want to set for index file? (default - ../data/index.csv) ') or '../data/index.csv'
    #         print('\n')

    #     if not os.path.exists(args.index):    
    #         print('You need to create index.csv file')

    #         if args.question is None:
    #             args.question = input('Do you want make index.csv? [y, n] ')
    #             print('\n')

    #         if args.question == 'y':
    #             args.path = input('Which path do you want to start? ')
    #             cl = Collector(args.path, args.index)
    #             print(f'Collecting files from {args.path}, wait...')
    #             cl.collect()
    #             print('All files are collected! Now you could start to use function')

    #         else:
    #             with open('../fun/ysnp.txt', 'r', encoding='utf-8') as file:
    #                 for row in file:
    #                     print(row, end='')
    #             print('\n')

    #     else:
    #         if datetime.fromtimestamp(getctime(args.index)).date() - date.today() > timedelta(days=2):
    #             print('Probably you need to update index.csv file')

    #         result = prog_exe_time(f_count, args.index)
    #         print(f'Число файлов - {result[1]} шт')
    #         print(f"Время выполнения программы : {result[0]} сек.")

    # else:
    #     if datetime.fromtimestamp(getctime(args.index)).date() - date.today() > timedelta(days=2):
    #         print('Probably you need to update index.csv file')

    #     result = prog_exe_time(f_count, args.index)
    #     print(f'Число файлов - {result[1]} шт')
    #     print(f"Время выполнения программы : {result[0]} сек.")
