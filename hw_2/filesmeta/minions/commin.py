'''Minion get base metadata'''

from datetime import datetime
from os.path import getsize, getmtime, getctime

class CommonMinion():
    '''Minion get base metadata'''
    def __init__(self):
        self.columns = ['File name', 'File full path', 'File size bytes', 'File create', 'File modifying']
        self.ex = ['*']
        self._filedata = ()


    def get_meta_inf(self, file):
        '''get metadata'''
        try:
            self._filedata = (file.split('/')[-1],
                            file,
                            getsize(file),
                            datetime.fromtimestamp(getctime(file)).date(),
                            datetime.fromtimestamp(getmtime(file)).date())

            return dict(zip(self.columns, self._filedata))
        except Exception as e:
            print(e)

