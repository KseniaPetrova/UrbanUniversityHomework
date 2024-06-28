from pprint import pprint
# Файл - это упорядоченная совокупность байтов, которая хранится на диске
# и/или занимает отдельную область внешней памяти

# Файл можно открыть для чтения и прочитать в память содержимое

# Имя файла может быть с путем по файловой системе,
# если путь не указан - то ищется в рабочей директории скрипта
# Начиная работать с файлами, мы касаемся окружения пайтона - операционной системы.
# И тут возможны ошибки ОС: файл не найден, у пользователя нет доступа к файлу и т.п.

# Если режим будет 'rb' - двоичное чтение.
file_name = 'byron.txt'
file = open(file_name, mode='rb')  # mode (режим): чтение бинарное
file_content = file.read()
file.close()
pprint(file_content)
# pprint(file_content.decode('utf8'))  # декодер для файлов с русским текстом


# Если режим будет 'r' то  автоматически перекодируется из UTF8, но можно указать кодировку
file_name = 'pushkin.txt'
file = open(file_name, mode='r')  # mode (режим): чтение символьное
# file = open(file_name, mode='r', encoding='utf8')  # декодер для файлов с русским текстом
file_content = file.read()
file.close()
pprint(file_content)


# но можно указать кодировку
file_name = 'pushkin_cp1251.txt'
file = open(file_name, mode='r', encoding='cp1251')  # mode (режим): чтение символьное
file_content = file.read()
file.close()
pprint(file_content)
# Если файла на диске нет - будет ошибка

# А что с записью? тоже все просто. Если файл уже был он обновится до нуля
file_name = 'out.txt'  # Если такого файла нет он создастся
file = open(file_name, mode='w', encoding='utf8')  # mode (режим): запись символьная, кодировка по умолчанию utf8
file_content = 'hello, мир!'  # в файл запишется строка
file.write(file_content)
file.close()

# бинарный режим записи требует байтов поэтому кодировка не указывается
file_name = 'out.txt'
file = open(file_name, mode='wb')  # mode (режим): запись бинарная
file_content = b'hello'  # используется запись байтами
file.write(file_content)
file.close()
# Если файла на диске нет - он будет создан, пустой


# режим добавления в конец
file_name = 'out.txt'
file = open(file_name, mode='a', encoding='utf8')  # mode (режим): запись в конец
file_content = 'hello, мир! '
file.write(file_content)
file.close()
# Если файла на диске нет - он будет создан, пустой

# режим чтение с записью. Прочитает файл и запишет в конец строку. Состояние файла сохранится
file_name = 'byron.txt'
file = open(file_name, mode='r+', encoding='utf8')  # mode (режим): чтение с записью
file_content = file.read()
file.write('\n appended line!')
file.close()
pprint(file_content)
# Если файла на диске нет - будет ошибка

# режим запись с чтением. Файл открывается, читается и удаляется содержимое, потом в него можно что-то записать
file_name = 'out.txt'
file = open(file_name, mode='w+')  # mode (режим): запись с чтением
file_content = file.read()
file.write('\n appended line!')
file.close()
pprint(file_content)
# Если файла на диске нет - создастся пустой, если есть - обнулится



