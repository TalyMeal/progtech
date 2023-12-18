import time
import sys
import os
sys.path.insert(0, "..")
from utils.top_extensions import extensions_count
from utils.files_count import f_count
from utils.top_files import top_by_size
from flask import Flask, render_template



app = Flask(__name__)

db_path = '../data/index.sqlite'


@app.route('/')
def index():
    mod_time = time.strftime(
        '%Y-%m-%d', time.localtime(os.path.getmtime(db_path)))
    files_count = f_count(db_path)
    return render_template('index.html', value1=mod_time, value2=files_count)


@app.route('/ext_stat')
def ext_stat():
    res = extensions_count(db_path, 10)
    return render_template('ext_stat.html', value1=res)


@app.route('/top_10_by_size')
def top_10_by_size():
    res = top_by_size(db_path, 10)
    return render_template('top_10_by_size.html', value1=res)


if __name__ == '__main__':
    app.run(debug=True)
