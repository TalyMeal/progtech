'''Minion get xlsx files metadata'''

from openpyxl import load_workbook

class XlsxMinion():
    '''Minion get xlsx files metadata'''
    def __init__(self):
        self.columns = ['MS Office Category', 'MS Office Contentstatus', 'MS Office Creator',
                        'MS Office Description', 'MS Office Identifier', 'MS Office Keywords',
                        'MS Office Language', 'MS Office Last modified by', 'MS Office Revision',
                        'MS Office Subject', 'MS Office Title', 'MS Office Version',
                        'MS Office Sheet Count']
        self.ex = ['xlsx', 'xlsm', 'xltx', 'xltm']
        self._metadata = ()

    def get_meta_inf(self, file):
        '''get metadata'''
        try:
            workbook = load_workbook(file)

            self._metadata = (workbook.properties.category,
                                workbook.properties.contentStatus,
                                workbook.properties.creator,
                                workbook.properties.description,
                                workbook.properties.identifier,
                                workbook.properties.keywords,
                                workbook.properties.language,
                                workbook.properties.last_modified_by,
                                workbook.properties.revision,
                                workbook.properties.subject,
                                workbook.properties.title,
                                workbook.properties.version, 
                                len(workbook.sheetnames))

            return dict(zip(self.columns, self._metadata))
        
        except Exception as e:
            print(e)