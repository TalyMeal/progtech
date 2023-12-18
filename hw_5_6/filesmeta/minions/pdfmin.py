'''Minion get PDF_metadata'''

import fitz

class PDFMinion():
    '''Minion get PDF_metadata'''
    def __init__(self):
        self.columns = ['PDF_format', 'PDF_title', 'PDF_author',
                        'PDF_subject', 'PDF_keywords', 'PDF_creator',
                        'PDF_producer', 'PDF_encryption', 'PDF_pages']
        self.ex = ['pdf']
        self._filedata = ()

    def get_meta_inf(self, file):
        '''get metadata'''
        try:
            with fitz.open(file) as pdf_file:

                self._filedata = (pdf_file.metadata['format'],
                                  pdf_file.metadata['title'],
                                  pdf_file.metadata['author'],
                                  pdf_file.metadata['subject'],
                                  pdf_file.metadata['keywords'],
                                  pdf_file.metadata['creator'],
                                  pdf_file.metadata['producer'],
                                  pdf_file.metadata['encryption'],
                                  pdf_file.page_count)
            
            return dict(zip(self.columns, self._filedata))
        
        except Exception as e:
            print(e)

