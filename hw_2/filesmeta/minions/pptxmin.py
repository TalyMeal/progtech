'''Minion get pptx files metadata'''

from pptx import Presentation

class PptxMinion():
    '''Minion get pptx files metadata'''
    def __init__(self):
        self.columns = ['MS Office Author', 'MS Office Category', 'MS Office Comments',
                        'MS Office Content status', 'MS Office Identifier', 'MS Office Keywords',
                        'MS Office Language', 'MS Office Last modified by', 'MS Office Revision',
                        'MS Office Subject', 'MS Office Title', 'MS Office Version',
                        'MS Office Slides count']
        self.ex = ['pptx']
        self._metadata = ()

    def get_meta_inf(self, file):
        '''get metadata'''
        try:
            presentation = Presentation(file)

            self._metadata = (presentation.core_properties.author,
                                presentation.core_properties.category,
                                presentation.core_properties.comments,
                                presentation.core_properties.content_status,
                                presentation.core_properties.identifier,
                                presentation.core_properties.keywords,
                                presentation.core_properties.language,
                                presentation.core_properties.last_modified_by,
                                presentation.core_properties.revision,
                                presentation.core_properties.subject,
                                presentation.core_properties.title,
                                presentation.core_properties.version, 
                                len(presentation.slides))

            return dict(zip(self.columns, self._metadata))
    
        except Exception as e:
            print(e)
    