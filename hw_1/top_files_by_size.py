# ВНИМАНИЕ - по умолчанию без переданного аргумента скрипт начинает обход с /

# Создается словарь - абсолютный путь до файла: размер файла, число элементов
# словаря равно переданному числу топ-результатов
# Скрипт рекурсивно обходит все директории с правами root, 
# начиная от указанной и включая ее.
# Для каждого файла в каждой директории проверяется размер - если файл больше,
# чем самый маленький файл в словаре - он заменяет его. В качестве элемента записывается
# абсолютный путь до файла: размер файла. В результате получаем в словаре топ самых
# больших файлов

# Танцы со словарем призваны избежать сохранения всех файлов в одном массиве - 
# очень много файлов в системе маленькие, и хранить их смысла не имеет. 

import os
from os.path import join, getsize, islink
import time
import argparse

# для удобства работы в консоли - минимальная справка
# арументы:
# путь, с которого начинается сканирование
# число - количество файлов наибольшего размера
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

# В функции создается словарь с числом элементов N = топ файлов по размеру
# В словаре ключ - абсолютный путь до файла, значение - размер файла в байтах
# Словарь инициализируется со значениями, равными 0
# Функция обходит директории и в каждой вызывает dict_update, в конце
# возвращает обновленный словарь.
def top_by_size(path_from: str, top: int) -> dict:

    top_files = {f'file_{k}':k for k in range(top)}

    for root, dirs, files in os.walk(path_from):
        dict_update(root, files, top_files)

    print_results(top_files)

# Отбор путей, не являющихся символическими ссылками
def symlink_filter(root: str, files: list) -> list:

    full_paths = list(filter(lambda x: not islink(x), [join(root, file) for file in files]))

    return full_paths

# Функция проверяет, есть ли внутри директории файлы размером больше, чем в словаре
# Если такие файлы находятся - заменяет ими файлы меньшего размера из словаря
def dict_update(root: str, files: list, top_files: dict) -> dict:

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

# Красиво выводится результат
def print_results(top_files: dict) -> print:
    padding = max([len(_.split('/')[-1]) for _ in top_files.keys()])
    top_files = dict(sorted(top_files.items(), key=lambda x:x[1], reverse=True))
    print()
    print(f"{f'Топ {len(top_files)} файлов по размеру в директории {args.path}' : ^{padding}}", end='\n\n')
    for i, (k, v) in enumerate(top_files.items(), 1):
        print(f'{str(i).rjust(len(str(args.top)))}. {k.split("/")[-1] : >{padding}} : {v} bytes')
    print()

# Измеряется время работы программы
def prog_exe_time(func: callable, *args: tuple[str, int]) -> float:
    start = time.time()
    func(*args)
    end = time.time()
    return round(end-start, 2)

result_time = prog_exe_time(top_by_size, args.path, args.top)

print(f"Время выполнения программы : {result_time} сек.")
