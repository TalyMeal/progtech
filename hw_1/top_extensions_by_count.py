# ВНИМАНИЕ - по умолчанию без переданного аргумента скрипт начинает обход с /

import os
from os.path import join, islink
import argparse
from top_files_by_size import prog_exe_time

# для удобства работы в консоли - минимальная справка
# единственный арумент - путь, с которого начинается сканирование
parser = argparse.ArgumentParser(description="Скрипт для получения топа расширений по числу файлов",
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

# Функция обходит все директории, начиная от указанной, и в каждой
# с помощью dict_update подсчитывает и сохраняет количество расширений в словарь.
# При завершении возвращает полученный словарь
def count_ext(path_from: str, top: int) -> dict:

    extensions = dict()

    for root, dirs, files in os.walk(path_from):
        dict_update(root, files, extensions)

    print_results(extensions)

# Отбор путей, не являющихся символическими ссылками
def symlink_filter(root: str, files: list) -> list:

    full_paths = list(filter(lambda x: not islink(x), [join(root, file) for file in files]))

    return full_paths

# Получает словарь с именами расширениями и их числом и список файлов директории
# Для каждого файла пробует получить расширение через точку и добавить его в словарь или
# увеличить число найденных файлов с данным расширением.
# При завершении возвращает обновленный словарь
def dict_update(root: str, files: list, extensions: dict) -> dict:

    paths = symlink_filter(root, files)

    for path in paths:
        try:
            extension = path.split('.')[-1]

            if extension in extensions.keys():
                extensions[extension] += 1
            else:
                extensions[extension] = 1     
        except:
            continue     

    return extensions

# Красиво выводим результат
def print_results(extensions: dict) -> print:
    padding = 10
    extensions = dict(sorted(extensions.items(), key=lambda x:x[1], reverse=True))
    print()
    print(f"{f'Топ {args.top} расширений по числу файлов в директории {args.path}' : ^{padding}}", end='\n\n')
    for i, (k, v) in enumerate(extensions.items(), 1):
        if i <= args.top:
            print(f'{str(i).rjust(len(str(args.top)))}. {k.split("/")[-1] : >10} : {v} files')
    print()

result_time = prog_exe_time(count_ext, args.path, args.top)

print(f"Время выполнения программы : {result_time[0]} сек.")