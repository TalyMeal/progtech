'''Minion get base metadata'''

from datetime import datetime
from os.path import getsize, getmtime, getctime

class CommonMinion():
    '''Minion get base metadata'''
    def __init__(self):
        self.columns = ['Name', 'Full_path', 'Size_bytes', 'Create', 'Modifying']
        self.ex = ['*']
        self._filedata = []


    def get_meta_inf(self, file):
        '''get metadata'''
        self._filedata = [file.split('/')[-1],
                          file,
                          getsize(file),
                          datetime.fromtimestamp(getctime(file)).date(),
                          datetime.fromtimestamp(getmtime(file)).date()]

        return dict(zip(self.columns, self._filedata))    
