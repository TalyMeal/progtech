"""Скрипт считает число файлов, содержащихся в index.csv"""

import argparse
import pandas as pd
from help_functions import check_and_run

def f_count(args_index) -> int:
    """Считает число файлов"""
    index = pd.read_csv(args_index, usecols=['File name'], engine='pyarrow')

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
