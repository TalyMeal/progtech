'''
Minion get image metadata

get all supported formats:

from PIL import features
from io import StringIO


buffer = StringIO()
features.pilinfo(out=buffer)
res= []
for line in buffer.getvalue().splitlines():
    if 'Extensions: ' in line:
        [res.append(i.split('.')[-1]) for i in line.split(':')[-1].split(',')]

print(res)
'''

from PIL import Image

class ImgMinion:
    '''Minion get image metadata'''
    def __init__(self):

        self.columns = ['Img Mode', 'Img Format', 'Img Width',
                        'Img Height', 'Img Is animated', 
                        'Img Numer frames']        
        self.ex = ['blp', 'bmp', 'bufr', 'cur', 'dcx', 'dds', 'dib', 'eps', 'ps',
                   'fit', 'fits', 'flc', 'fli', 'fpx', 'ftc', 'ftu', 'gbr', 'gif', 
                   'grib', 'h5', 'hdf', 'icns', 'ico', 'im', 'iim', 'jfif', 'jpe', 
                   'jpeg', 'jpg', 'j2c', 'j2k', 'jp2', 'jpc', 'jpf', 'jpx', 'mic', 
                   'mpeg', 'mpg', 'msp', 'pcd', 'pcx', 'pxr', 'apng', 'png', 'pbm', 
                   'pgm', 'pnm', 'ppm', 'psd', 'bw', 'rgb', 'rgba', 'sgi', 'ras', 
                   'icb', 'tga', 'vda', 'vst', 'tif', 'tiff', 'webp', 'emf', 'wmf', 
                   'xbm', 'xpm']
        self._filedata = ()

    def get_meta_inf(self, file):
        '''get metadata'''
        try:
            with Image.open(file) as img:
                # атрибутов больше, выбраны основные, на которых не ломается метод (потом можно расширить)
                self._filedata = (img.mode, img.format, img.width,
                                   img.height, img.is_animated,
                                   img.n_frames)

            return dict(zip(self.columns, self._filedata))

        except:
            return dict(zip(self.columns, self._filedata*len(self.columns)))