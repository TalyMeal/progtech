"""
Скрипт возвращает N самых больших по размеру файлов, содержащихся в директории.

ВНИМАНИЕ - по умолчанию скрипт начинает обход с /
"""

import os
from os.path import join, getsize, islink
import time
import argparse

def top_by_size(path_from: str, top: int) -> dict:
    """
    В функции создается словарь с числом элементов N = топ файлов по размеру

    В словаре ключ - абсолютный путь до файла, значение - размер файла в байтах

    Словарь инициализируется со значениями, равными 0

    Функция обходит директории и в каждой вызывает dict_update, в конце
    возвращает обновленный словарь.
    """    
    top_files = {f'file_{k}':k for k in range(top)}

    for root, dirs, files in os.walk(path_from):
        dict_update(root, files, top_files)

    print_results(top_files, path_from, top)

def symlink_filter(root: str, files: list) -> list:
    """Отбор путей, не являющихся символическими ссылками"""
    full_paths = list(filter(lambda x: not islink(x), [join(root, file) for file in files]))

    return full_paths

def dict_update(root: str, files: list, top_files: dict) -> dict:
    """
    Функция проверяет, есть ли внутри директории файлы размером больше, чем в словаре

    Если такие файлы находятся - заменяет ими файлы меньшего размера из словаря
    """
    paths = symlink_filter(root, files)

    for path in paths:

        try:
            val_with_min_key = min(top_files, key=top_files.get)

            if top_files[val_with_min_key] < getsize(path):
                del top_files[val_with_min_key]
                top_files[path] = getsize(path)
        except:
            continue

    return top_files

def print_results(top_files: dict, path: str, top: int) -> print:
    """Красиво выводится результат"""
    padding = max([len(_.split('/')[-1]) for _ in top_files.keys()])
    top_files = dict(sorted(top_files.items(), key=lambda x:x[1], reverse=True))
    print()
    print(f"{f'Топ {len(top_files)} файлов по размеру в директории {path}' : ^{padding}}", end='\n\n')
    for i, (k, v) in enumerate(top_files.items(), 1):
        print(f'{str(i).rjust(len(str(top)))}. {k.split("/")[-1] : >{padding}} : {v} bytes')
    print()

def prog_exe_time(func: callable, *args: tuple[str, int]) -> (float, any):
    """Возвращается время работы программы и результат работы функции"""
    start = time.time()
    result = func(*args)
    end = time.time()
    return round(end-start, 2), result

if __name__=='__main__':

    parser = argparse.ArgumentParser(description="Скрипт для получения топа файлов по размеру",
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

    result = prog_exe_time(top_by_size, args.path, args.top)
    
    print(f"Время выполнения программы : {result[0]} сек.")
