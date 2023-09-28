"""
Скрипт число файлов, содержащихся в директории.

ВНИМАНИЕ - по умолчанию скрипт начинает обход с /
"""

import os
import argparse
from top_files_by_size import prog_exe_time


def f_count(path_from: str) -> int:
    """Считает число файлов"""
    cnt = 0

    for _, _, files in os.walk(path_from):
        cnt += len(files)

    return cnt


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Скрипт для получения числа файлов в директории",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--path',
                        '-p',
                        type=str,
                        default='/',
                        help="Путь для старта. Пример: /home/{USERNAME}/Downloads/")
    args = parser.parse_args()

    result = prog_exe_time(f_count, args.path)

    print(f'Число файлов в {args.path} - {result[1]} шт')
    print(f"Время выполнения программы : {result[0]} сек.")
