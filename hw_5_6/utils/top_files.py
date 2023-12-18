"""Скрипт возвращает N самых больших по размеру файлов"""
import sqlite3


def top_by_size(args_index, top):
    """Get top files"""

    con = sqlite3.connect(args_index)
    cursor = con.cursor()

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
