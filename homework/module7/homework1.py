"""
Создайте в директории проекта текстовый файл с расширением txt
Добавьте в этот файл следующий текст
Создайте переменную с этим файлом
Распечатайте содержимое текстового файла в консоль
Закройте файл
"""
from pprint import pprint


file_name = 'poem.txt'
file = open(file_name, mode='rb')  # mode (режим): чтение бинарное
file_content = file.read()
file.close()
pprint(file_content)