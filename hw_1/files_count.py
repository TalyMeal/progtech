# ВНИМАНИЕ - по умолчанию без переданного аргумента скрипт начинает обход с /home/

import os
from os.path import join, getsize
import time
import argparse

# для удобства работы в консоли - минимальная справка
# арументы:
# путь, с которого начинается сканирование
parser = argparse.ArgumentParser(description="Скрипт для получения топа файлов по размеру",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--path', 
                    '-p',
                    type=str, 
                    default='/home/', 
                    help="Путь для старта. Пример: /home/{USERNAME}/Downloads/")
args = parser.parse_args()

# считается число файлов
def f_count(path_from: str) -> int:

    cnt = 0

    for root, dirs, files in os.walk(path_from):
        cnt += len(files)

    return cnt

# Измеряется время работы программы
def prog_exe_time(func: callable, *args: str) -> float:
    start = time.time()
    cnt = func(*args)
    end = time.time()
    return round(end-start, 2), cnt

result_time, cnt = prog_exe_time(f_count, args.path)

print(f'Число файлов в {args.path} - {cnt} штук')
print(f"Время выполнения программы : {result_time} сек.")
