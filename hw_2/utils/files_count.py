"""Скрипт считает число файлов, содержащихся в index.sqlite"""

import argparse
import pandas as pd
from help_functions import check_and_run

def f_count(args_index) -> int:
    """Считает число файлов"""
    index = pd.read_csv(args_index, usecols=['File_name'], engine='pyarrow')

    return len(index.index)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--question',
                        '-q',
                        type=str,
                        help="Вопрос - генерировать ли файл index.sqlite")
    parser.add_argument('--path',
                        '-p',
                        type=str,
                        default='/',
                        help="Путь для старта. Пример: /home/{USERNAME}/Downloads/")
    parser.add_argument('--index',
                        '-i',
                        type=str,
                        default='../data/index.sqlite',
                        help="Абсолютный путь для индекса файлов. Пример: /home/{USERNAME}/Documents/index.sqlite По умолчанию - ../data/index.sqlite")     
    args = parser.parse_args()

    check_and_run(args.index, args.question, args.path, f_count, [args.index])
