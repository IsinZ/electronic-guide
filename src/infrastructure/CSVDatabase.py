import csv # модуль для работы с csv-файлами.

from IDatabaseInterfaces import IDatabaseRM, IDatabaseGUI
from Data_types.Exhibit import Exhibit

# ПРИМЕЧАНИЕ: для корректной работы методов оформляйте
# строки в БД правильно.
# При записи любых данных в файлы БД вручную обязательно
# в конце сделать перевод строки на новую!

# path = 'infrastructure/Database/'
path = 'Database/'

# функция для проверки наличия такого объекта в БД,
# возвращает 1, если такого нет,
# возвращает -1, если такой есть.
def CheckExhibit(self, exhibit):
    print('CheckExhibit')
    exhibits = self.getAllExhibits()
    for ex in exhibits:
        if (ex.name == exhibit.name and ex.century == str(exhibit.century)):
            return -1
    return 1

class CSVDatabase(IDatabaseRM, IDatabaseGUI):
    # возвращает массив объектов exhibit.
    def getExhibitImages(self):
        print('getExhibitImages')
        with open(path + 'Exhibits.csv', 'r') as fExhibitsR:
            exhibit = []
            reader = csv.DictReader(fExhibitsR, delimiter = ',')
            # захожу в цикл по строкам файла Exibit.csv.
            for line in reader:
                exhibit.append(Exhibit(line['ex_id'], line['name'],
                                       line['century'], line['image_path'],
                                       line['info_path']))
        return exhibit
    
    # если объект добавлен, возвращает его id,
    # если такой объект уже был в БД, возвращает -1.
    def addExhibit(self, exhibit):
        print('addExhibit')
        # проверка наличия такого объекта в БД.
        if (CheckExhibit(self, exhibit) == -1):
            print('This exhibit already exists')
            return -1
        with open(path + 'Exhibits.csv', 'a') as fExhibitsW:
            fieldnames = ['ex_id', 'name', 'century', 'image_path',
                          'info_path']
            writer = csv.DictWriter(fExhibitsW, fieldnames = fieldnames,
                                    delimiter = ',')
            writer.writerow({'ex_id': exhibit.ex_id, 'name': exhibit.name,
                             'century': exhibit.century,
                             'image_path': exhibit.image_path,
                             'info_path': exhibit.info_path})
        return exhibit.ex_id
    
    # возвращает массив объектов exhibit.
    def getAllExhibits(self):
        print('getAllExhibits')
        with open(path + 'Exhibits.csv', 'r') as fExhibitsR:
            exhibit = []
            reader = csv.DictReader(fExhibitsR, delimiter = ',')
            # захожу в цикл по строкам файла Exibit.csv.
            for line in reader:
                exhibit.append(Exhibit(line['ex_id'], line['name'],
                                       line['century'], line['image_path'],
                                       line['info_path']))
        return exhibit
      
    # если объект с таким id найден, возвращает объект exhibit,
    # если такого объекта нет, возвращает -1
    def getExhibit(self, ex_id):
        print('getExhibit')
        with open(path + 'Exhibits.csv', 'r') as fExhibitsR:
            reader = csv.DictReader(fExhibitsR, delimiter = ',')
            # захожу в цикл по строкам файла Exibit.csv.
            for line in reader:
                if(str(ex_id) == line['ex_id']):
                    return Exhibit(line['ex_id'], line['name'],
                                   line['century'], line['image_path'],
                                   line['info_path'])
        # если не нашлось экспоната с таким id.
        print('There is no exhibit with this id')
        return -1
        
if __name__ == '__main__':
    """main"""
