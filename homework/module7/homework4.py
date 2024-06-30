"""
Задание:
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.
"""
import os
import time

directory = 'C:\\Users\\Admin\\Desktop\\стикеры'

for root, dirs, files in os.walk(directory):  # обхода каталога directory
    print('-' * 25)
    print(root, dirs, files)
    print('↓' * 25)
    for file in files:
        full_file_path = os.path.join(root, file)  # формирование полного пути к файлам
        last_modified = os.path.getmtime(full_file_path)  # получения и отображения времени последнего изменения файла
        # от начала эпохи с 1 января 1970г
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(last_modified))  # норм время
        size_file = os.path.getsize(full_file_path)  # получения размера файла в байтах
        size_file_kb = size_file / 1024  # размер файла в кб
        parent_dir = os.path.dirname(full_file_path)
        print(f'Файл: {file} лежит по пути: {full_file_path}, последний раз был изменён: {formatted_time}'
              f', его размер {size_file_kb:.2f} kb, родительская директория: {parent_dir}')
