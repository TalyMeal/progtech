'''Creacting index.csv file'''

import sys
import argparse
import cProfile
import pstats
import io
from pstats import SortKey

sys.path.insert(0,"..")

from staff.collector import Collector

pr = cProfile.Profile()
pr.enable()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Скрипт для получения таблицы всех файлов в директории",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--path',
                        '-p',
                        type=str,
                        default='/',
                        help="Путь для старта. Пример: /home/{USERNAME}/Downloads/")
    parser.add_argument('--index',
                        '-i',
                        type=str,
                        default='../data/index.csv',
                        help="Абсолютный путь для индекса файлов. Пример: /home/{USERNAME}/Documents/index.csv По умолчанию - ../data/index.csv")    
    args = parser.parse_args()

    cl = Collector(args.path, args.index)

    cl.collect()

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
