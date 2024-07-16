import os

print(f'Текущая директория: {os.getcwd()}')
# os.mkdir("example")  # создаст папку example в текущей директории
# if os.path.exists('example'):  # exists - принимает путь и если он существует возвращает True
#     os.chdir('example')  # изменяем текущую деректорию на example
# else:  # если текущй директории example нет
#     os.mkdir('example')  # создаем директорию example
#     os.chdir('example')  # меняем своё положение на эту директорию
# print(f'Текущая директория: {os.getcwd()}')
# os.makedirs('first\\second')  # создаст папку в папке
print(f'Список директорий и файлов: {os.listdir()}')  # список директорий и файлов в текущей диреткории. не показывает вложженность
#********
for i in os.walk('.'):   # '.' - текущая директория. walk - обход текущей дир
    print(i)
#********
file = [f for f in os.listdir() if os.path.isfile(f)]  # отсортирует файлы
dirs = [d for d in os.listdir() if os.path.isdir(d)]  # отсортирует директории
print(f'Отсортированные файлы {file}')
print(f'Отсортированные директории {dirs}')
#**********
os.startfile(file[3])  # dividing numbers откроется
print(os.stat(file[3]))  # выведет информацию о файле
print(os.stat(file[3]).st_size)  # выведет размер файла
#****
# os.system('pip install lib')  # работает как терминал. можно установить библиотеку







