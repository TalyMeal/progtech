"""
Скрипт возвращает N наиболее часто встречающихся расширений файлов в директории.

ВНИМАНИЕ - по умолчанию скрипт начинает обход с /
"""
import argparse
import pandas as pd
from help_functions import check_and_run

def extensions_count(args_index, top):
    """Get top 10 extensions"""
    index = pd.read_csv(args_index, usecols=['File name'], engine='pyarrow')

    extensions = index["File name"].str.split(".", n = -1, expand = False).str[-1]

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

    check_and_run(args.index, args.question, args.path, extensions_count, [args.index, args.top])
