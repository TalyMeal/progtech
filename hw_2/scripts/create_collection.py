import sys
import argparse

sys.path.insert(0,"..")

from staff.collector import Collector

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Скрипт для получения таблицы всех файлов в директории",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--path',
                        '-p',
                        type=str,
                        default='/',
                        help="Путь для старта. Пример: /home/{USERNAME}/Downloads/")
    args = parser.parse_args()

    cl = Collector(args.path)

    cl.collect()
