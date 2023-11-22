"""
Скрипт возвращает N наиболее часто встречающихся расширений файлов в директории.

ВНИМАНИЕ - по умолчанию скрипт начинает обход с /
"""
import argparse
import sqlite3
from help_functions import check_and_run

def extensions_count(args_index, top):
    """Get top N extensions"""

    con = sqlite3.connect(args_index)
    cursor = con.cursor()

    # Запрос для расчета топ N расширений файлов
    query = f"""
        SELECT SUBSTR(File_name, INSTR(File_name, '.')) AS extension, COUNT(*) AS count
        FROM index_files
        GROUP BY extension
        ORDER BY count DESC
        LIMIT {top};
    """

    # Выполнение запроса
    cursor.execute(query)

    # Получение результатов
    results = cursor.fetchall()

    # Закрытие соединения с базой данных
    con.close()

    return [f'{x[0]}: {x[1]} штук' for x in results]

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--question',
                        '-q',
                        type=str,
                        help="Вопрос - генерировать ли файл index.sqlite")
    parser.add_argument('--path',
                        '-p',
                        type=str,
                        default='/',
                        help="Путь для старта. Пример: /home/{USERNAME}/Downloads/")
    parser.add_argument('--index',
                        '-i',
                        type=str,
                        default='../data/index.sqlite',
                        help="Абсолютный путь для индекса файлов. Пример: /home/{USERNAME}/Documents/index.sqlite По умолчанию - ../data/index.sqlite")     
    parser.add_argument('--top',
                        '-t', 
                        type=int,
                        default=10,
                        help="Количество файлов для вывода. Пример: 3")
    args = parser.parse_args()

    check_and_run(args.index, args.question, args.path, extensions_count, [args.index, args.top])
