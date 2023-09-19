# ВНИМАНИЕ - по умолчанию без переданного аргумента скрипт начинает обход с /

# Скрипт рекурсивно обходит все директории с правами root, 
# начиная от указанной и включая ее.
# В каждой диектории получает список битых символических ссылок и удаляет их

import os
from os.path import join
import argparse
import time

# для удобства работы в консоли - минимальная справка
# единственный арумент - путь, с которого начинается сканирование
parser = argparse.ArgumentParser(description="Скрипт для рекурсивного удаления битых символических ссылок",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--path', 
                    type=str, 
                    default='/', 
                    help="Путь для старта. Пример: /home/{USERNAME}/Downloads/")
args = parser.parse_args()
config = vars(args)
print(config)

def rm_broken_symlinks(path_from: str) -> None:

    for path in os.scandir(path_from):

        if path.is_dir():
            full_path = join(path_from, path)
            print(full_path)
            os.system(f'sudo find "{full_path}" -xtype l -delete')
            rm_broken_symlinks(full_path)
        else:
            continue

start = time.time()
rm_broken_symlinks(args.path)
end = time.time()

print(f"Время выполнения программы : {round(end-start, 2)} сек.")