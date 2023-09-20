# ВНИМАНИЕ - по умолчанию без переданного аргумента скрипт начинает обход с /

# Скрипт рекурсивно обходит все директории, начиная от указанной и включая ее.
# В каждой директории получает список битых символических ссылок и удаляет их

import os
from os.path import join, isdir, islink
import argparse
import time

# для удобства работы в консоли - минимальная справка
# единственный арумент - путь, с которого начинается сканирование
parser = argparse.ArgumentParser(description="Скрипт для рекурсивного удаления битых символических ссылок",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--path', 
                    '-p',
                    type=str, 
                    default='/', 
                    help="Путь для старта. Пример: /home/{USERNAME}/Downloads/")
args = parser.parse_args()

# Проверяет содержимое директории и для каждой из вложенных директорий
# вызывает rm_broken_symlinks_dir
# not islink(path) защищает от прохода по бесконечному кольцу ссылок на папки
def rm_broken_symlinks(path_from: str) -> None:

    for path in os.scandir(path_from):
        if isdir(path) and not islink(path):
            rm_broken_symlinks_dir(path_from, path)
        else:
            continue

# Удаляет битые символические ссылки в директории,
# затем вызывает rm_broken_symlinks
def rm_broken_symlinks_dir(path_from: str, path: str) -> None:

    full_path = join(path_from, path)
    os.system(f'sudo find "{full_path}" -xtype l -delete')
    rm_broken_symlinks(full_path)

# Измеряет время работы программы
def prog_exe_time(func: callable, *args) -> float:
    start = time.time()
    func(*args)
    end = time.time()
    return round(end-start, 2)

result_time = prog_exe_time(rm_broken_symlinks, args.path)

print(f"Время выполнения программы : {result_time} сек.")