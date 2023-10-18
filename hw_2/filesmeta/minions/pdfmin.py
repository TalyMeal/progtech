'''Minion get PDF metadata'''

import fitz

class PDFMinion():
    '''Minion get PDF metadata'''
    def __init__(self):
        self.columns = ['Format', 'Title', 'Author',
                        'Subject', 'Keywords', 'Creator',
                        'Producer', 'Encryption', 'Pages']
        self.ex = ['pdf']
        self._filedata = {}

    def get_meta_inf(self, file):
        '''get metadata'''
        with fitz.open(file) as pdf_file:

            self._filedata = {k.title():v for k, v in pdf_file.metadata.items() if k.title() in self.columns and v}
            self._filedata.update({'Pages':pdf_file.page_count})
        
        return self._filedata

