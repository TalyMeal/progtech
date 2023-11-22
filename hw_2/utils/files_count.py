"""Скрипт считает число файлов, содержащихся в index.sqlite"""

import argparse
from help_functions import check_and_run
import sqlite3

def f_count(args_index) -> int:
    """Считает число файлов"""

    con = sqlite3.connect(args_index)
    cur = con.cursor()
    cur.execute("SELECT COUNT(File_full_path) FROM index_files")
    files_count = cur.fetchone()[0]
    con.close()
    return f"{files_count} файлов"

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
