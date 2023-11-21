'''Minion get pptx files metadata'''

from pptx import Presentation

class PptxMinion():
    '''Minion get pptx files metadata'''
    def __init__(self):
        self.columns = ['MS_Office_Author', 'MS_Office_Category', 'MS_Office_Comments',
                        'MS_Office_Content_status', 'MS_Office_Identifier', 'MS_Office_Keywords',
                        'MS_Office_Language', 'MS_Office_Last_modified_by', 'MS_Office_Revision',
                        'MS_Office_Subject', 'MS_Office_Title', 'MS_Office_Version',
                        'MS_Office_Slides_count']
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
    