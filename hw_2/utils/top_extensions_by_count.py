"""
Скрипт возвращает N наиболее часто встречающихся расширений файлов в директории.

ВНИМАНИЕ - по умолчанию скрипт начинает обход с /
"""

import os
from os.path import join, islink
import argparse
from collections import defaultdict
from top_files_by_size import prog_exe_time


def count_ext(path_from: str, top: int) -> dict:
    """Подсчитывает и печатает N наиболее часто встречающихся расширений файлов в директории"""
    extensions = defaultdict(int)

    for root, _, files in os.walk(path_from):
        dict_update(root, files, extensions)

    print_results(extensions, path_from, top)


def symlink_filter(root: str, files: list) -> list:
    """Фильтрует пути, не являющиеся символическими ссылками"""
    full_paths = list(filter(lambda x: not islink(
        x), [join(root, file) for file in files]))

    return full_paths


def dict_update(root: str, files: list, extensions: dict) -> dict:
    """Считает число встретившихся в конкретной директории расширений"""
    paths = symlink_filter(root, files)

    for path in paths:
        try:
            extension = path.split('.')[-1]
            extensions[extension] += 1
        except:
            continue

    return extensions


def print_results(extensions: dict, path: str, top: int) -> print:
    """Красиво выводит результат"""
    padding = 10
    extensions = dict(
        sorted(extensions.items(), key=lambda x: x[1], reverse=True))
    print()
    print(f"{f'Топ {top} расширений по числу файлов в директории {path}' : ^{padding}}", end='\n\n')
    for i, (k, v) in enumerate(extensions.items(), 1):
        if i <= top:
            print(
                f'{str(i).rjust(len(str(top)))}. {k.split("/")[-1] : >10} : {v} files')
    print()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Скрипт для получения топ-N расширений",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
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

    result = prog_exe_time(count_ext, args.path, args.top)

    print(f"Время выполнения программы : {result[0]} сек.")
