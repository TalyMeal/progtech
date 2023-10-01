"""
Скрипт возвращает N наиболее часто встречающихся расширений файлов в директории.

ВНИМАНИЕ - по умолчанию скрипт начинает обход с /
"""
import os
import sys
import argparse
from datetime import datetime, date, timedelta
from os.path import getctime
import pandas as pd
from top_files import prog_exe_time
sys.path.insert(0,"..")
from staff.collector import Collector

def extensions_count(top):
    """Get top 10 extensions"""
    index = pd.read_csv('../data/index.csv', usecols=['Name'], engine='pyarrow')

    extensions = index["Name"].str.split(".", n = 1, expand = True).iloc[:,1:]

    extensions = extensions.value_counts()
    extensions = extensions.to_frame().reset_index().head(top).set_index(pd.Index(range(1,top+1)))
    extensions.columns = ['Extension', 'Count']

    return extensions

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
            print(f'All files are collected! Now you could start to use top_extensions function')
            
        else:
            with open('../fun/ysnp.txt', 'r', encoding='utf-8') as file:
                for row in file:
                    print(row, end='')
            print('\n')

    else:
        if (datetime.fromtimestamp(getctime('../data/index.csv')).date() - date.today()) > timedelta(days=2):
            print('Probably you need to update index.csv file')

        result = prog_exe_time(extensions_count, args.top)

        print(f"Top {args.top} extensions by count:", end='\n\n')
        print(result[1])
        print(f"Время выполнения программы : {result[0]} сек.")
