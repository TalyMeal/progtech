"""
Скрипт возвращает N наиболее часто встречающихся расширений файлов в директории.

ВНИМАНИЕ - по умолчанию скрипт начинает обход с /
"""
import sqlite3

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
