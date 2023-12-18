import tkinter as tk
from tkinter import ttk
import os
import sys
import time
sys.path.insert(0, "..")
from utils.top_files import top_by_size
from utils.files_count import f_count
from utils.top_extensions import extensions_count

db_path = '../data/index.sqlite'


def update_main_frame():
    mod_time = time.strftime(
        '%Y-%m-%d', time.localtime(os.path.getmtime(db_path)))
    files_count = f_count(db_path)
    main_label.config(
        text=f"Дата обновления базы: {mod_time}\nЧисло файлов в базе: {files_count}")


def update_ext_stat():
    res = extensions_count(db_path, 10)
    update_listbox(res)


def update_top_10_by_size():
    res = top_by_size(db_path, 10)
    update_listbox(res)


def update_listbox(data):
    listbox.delete(0, tk.END)
    for item in data:
        listbox.insert(tk.END, item)


root = tk.Tk()
root.title("STAKAN Main Page")

root.minsize(400, 300)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Меню СТАКАНа", menu=file_menu)
file_menu.add_command(label="Статистика по расширениям", command=update_ext_stat)
file_menu.add_command(label="Статистика ТОП-10 по размеру", command=update_top_10_by_size)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20, fill='both', expand=True)

main_label = ttk.Label(main_frame, text="")
main_label.pack()

listbox_frame = ttk.Frame(root)
listbox_frame.pack(padx=20, pady=20, fill='both', expand=True)

listbox = tk.Listbox(listbox_frame, height=15, width=30)
listbox.pack(side=tk.LEFT, fill='both', expand=True)

update_main_frame()

root.mainloop()
