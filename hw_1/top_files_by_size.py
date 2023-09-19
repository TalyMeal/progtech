import os
from os.path import join, getsize
import argparse
import time

# для удобства работы в консоли - минимальная справка
# единственный арумент - путь, с которого начинается сканирование
parser = argparse.ArgumentParser(description="Скрипт для получения топа файлов по размеру",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--path', 
                    type=str, 
                    default='/', 
                    help="Путь для старта. Пример: /home/{USERNAME}/Downloads/")
parser.add_argument('--top', 
                    type=int, 
                    default=10, 
                    help="Количество файлов для вывода. Пример: 3")
args = parser.parse_args()
config = vars(args)
print(config)

def top_files_by_size(path_from: str, top: int) -> dict:

    top_files = {f'file_{k}':k for k in range(top)}

    for root, dirs, files in os.walk(path_from):

        for file in files:

            full_path = join(root, file)
            val_with_min_key = min(top_files, key=top_files.get)

            if top_files[val_with_min_key] < getsize(full_path):

                del top_files[val_with_min_key]

                top_files[full_path] = getsize(full_path)

    top_files = dict(sorted(top_files.items(), key=lambda x:x[1], reverse=True))
    [print(k.split('/')[-1], v) for k, v in top_files.items()]

start = time.time()
top_files_by_size(args.path, args.top)
end = time.time()

print(f"Время выполнения программы : {round(end-start, 2)} сек.")
