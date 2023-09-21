# ВНИМАНИЕ - по умолчанию без переданного аргумента скрипт начинает обход с /

import os
from top_files_by_size import prog_exe_time
import argparse

# для удобства работы в консоли - минимальная справка
# арументы:
# путь, с которого начинается сканирование
parser = argparse.ArgumentParser(description="Скрипт для получения топа файлов по размеру",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--path', 
                    '-p',
                    type=str, 
                    default='/', 
                    help="Путь для старта. Пример: /home/{USERNAME}/Downloads/")
args = parser.parse_args()

# считается число файлов
def f_count(path_from: str) -> int:

    cnt = 0

    for root, dirs, files in os.walk(path_from):
        cnt += len(files)

    return cnt

result_time, cnt = prog_exe_time(f_count, args.path)

print(f'Число файлов в {args.path} - {cnt} штук')
print(f"Время выполнения программы : {result_time} сек.")