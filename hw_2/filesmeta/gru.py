'''Gru is dispatcher for minions'''

import os
import importlib

class Gru():
    '''work with minions'''
    def __init__(self):
        self._listdir = '../filesmeta/minions'
        self.minoins_pkg_path = 'filesmeta.minions'
        self._module = callable
        self._minions_ex = {}
        self._meta_inf = {}
        self._res = {}
        self._file_list = []
        self.clmns = []
        self._ex = str()
        self._f = str()
        self._file_name = str()
        self._name = str()


    def _update_minions(self):
        '''automatically get or update all minion classes'''
        # Получаем список .py файлов, которые содержат классы миньонов
        self._file_list = ['.'.join([self.minoins_pkg_path, self._f])
                           for self._f in os.listdir(self._listdir)
                           if self._f.endswith('.py')]

        # Импортируем модули из полученного списка файлов и в каждом модуле получаем классы миньонов
        for self._file_name in self._file_list:

            self._module = importlib.import_module(self._file_name[:-3], package=None)

            for self._name in dir(self._module):
                if 'Minion' in self._name:
                    # получаем ЭКЗЕМПЛЯР класса, к методам которого можно обращаться
                    yield getattr(self._module, self._name)()


    def get_extensions(self):
        '''create dictionary extension: minion'''
        for mnm in self._update_minions():
            # собираем названия столбцов из миньона, если столбца еще нет в списке
            self.clmns.extend(list(filter(lambda x: x not in self.clmns, mnm.columns)))
            # собираем словарь {расширение: миньон}
            self._minions_ex.update({ex:mnm for ex in mnm.ex})

    def gru_get_meta_inf(self, filename):
        '''get meta information'''
        # нужно при каждом вызове gru_get_meta_inf затирать self._meta_inf - пока лучше не придумал
        self._meta_inf = {}
        # получаем базовую информацию по файлу
        self._meta_inf.update(self._minions_ex['*'].get_meta_inf(filename))

        # узнаем расширение файла
        self._ex = filename.split(".")[-1]

        # если расширение известно - вызываем соответствующего миньона
        if self._ex in self._minions_ex:
            self._res = self._minions_ex[self._ex].get_meta_inf(filename)
            self._meta_inf.update(self._res)

        return self._meta_inf
