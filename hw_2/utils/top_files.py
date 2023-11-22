"""Скрипт возвращает N самых больших по размеру файлов"""
import sqlite3
import argparse
from help_functions import check_and_run

def top_by_size(args_index, top):
    """Get top files"""

    con = sqlite3.connect(args_index)
    cursor = con.cursor()

    # Запрос для расчета топ N расширений файлов
    query = f""" 
            SELECT File_name, CAST(File_size_bytes AS INTEGER) AS File_size_bytes
            FROM index_files
            ORDER BY File_size_bytes DESC
            LIMIT {top};
            """

    # Выполнение запроса
    cursor.execute(query)

    # Получение результатов
    results = cursor.fetchall()

    # Закрытие соединения с базой данных
    con.close()

    return [f'{x[0]}: {x[1]} байт' for x in results]

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

    check_and_run(args.index, args.question, args.path, top_by_size, [args.index, args.top])
