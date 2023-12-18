'''Minion get docx files metadata'''

import docx

class DocxMinion():
    '''Minion get docx files metadata'''
    def __init__(self):
        self.columns = ['MS_Office_Author', 'MS_Office_Category', 'MS_Office_Comments',
                        'MS_Office_Content_status', 'MS_Office_Identifier', 'MS_Office_Keywords',
                        'MS_Office_Language', 'MS_Office_Last_modified_by', 'MS_Office_Revision',
                        'MS_Office_Subject', 'MS_Office_Title', 'MS_Office_Version']
        self.ex = ['docx']
        self._metadata = ()

    def get_meta_inf(self, file):
        '''get metadata'''
        try:
            doc = docx.Document(file)

            self._metadata = (doc.core_properties.author,
                                doc.core_properties.category,
                                doc.core_properties.comments,
                                doc.core_properties.content_status,
                                doc.core_properties.identifier,
                                doc.core_properties.keywords,
                                doc.core_properties.language,
                                doc.core_properties.last_modified_by,
                                doc.core_properties.revision,
                                doc.core_properties.subject,
                                doc.core_properties.title,
                                doc.core_properties.version)

            return dict(zip(self.columns, self._metadata))
        
        except Exception as e:
            print(e)

