"""Скрипт возвращает N самых больших по размеру файлов"""

import argparse
import pandas as pd
from help_functions import check_and_run

def top_by_size(args_index, top):
    """Get top files"""
    index = pd.read_csv(args_index, usecols=['File name', 'File size bytes'], engine='pyarrow')
    index = index.sort_values(by=['File size bytes'], ascending=False).head(top).set_index(pd.Index(range(1,top+1)))

    return index

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
    parser.add_argument('--top',
                        '-t', 
                        type=int,
                        default=10,
                        help="Количество файлов для вывода. Пример: 3")
    args = parser.parse_args()

    check_and_run(args.index, args.question, args.path, top_by_size, [args.index, args.top])
