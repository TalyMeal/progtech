"""Скрипт считает число файлов, содержащихся в index.sqlite"""

import sqlite3


def f_count(args_index) -> int:
    """Считает число файлов"""

    con = sqlite3.connect(args_index)
    cur = con.cursor()
    cur.execute("SELECT COUNT(File_full_path) FROM index_files")
    files_count = cur.fetchone()[0]
    con.close()
    return files_count
