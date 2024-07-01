# сделать генератор текста на основе статистики
# идея: подсчитать какие буквы наиболее часто стоят рядом
import zipfile
from pprint import pprint
from random import randint

# zip_file_name = '90202836.zip'
# zfile = zipfile.ZipFile(zip_file_name, 'r')  # чтение архива
# zfile.printdir() # просмотр содержимого zip
# for filename in zfile.namelist():  # вытащили из архива файл txt
#     zfile.extract(filename)

filename = '90202836.txt'

stat = {}
sequence = ''  # предыдущий символ
with open(filename, 'r', encoding='cp1251') as file:
    for line in file:
        line = line[:-1]  # не учитывается возврат коретки
        # print(line)
        for char in line:  # для каждого символа в строке
            if sequence in stat:  # обновляется статистика
                if char in stat[sequence]:
                    stat[sequence][char] += 1  # получаем статистику внутреннего словаря
                else:
                    stat[sequence][char] = 1  # если у символа нет статистики начинаем ее с 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence[1:] + char  # дает получить полную статистику символов до и после пробела
            # без этой строчки статистика работала до пробела
            # работает на 3 символа

pprint(stat)

totals = {}
stat_for_generate = {}  # словарик для генерации. словарь списков
for sequence, char_stst in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, count in char_stst.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    stat_for_generate[sequence].sort(reverse=True)

pprint(totals)
pprint(stat_for_generate)

N = 1000
printed = 0

sequence = '   '
spaces_printed = 0
while printed < N:
    char_stst = stat_for_generate[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stst:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    if char == ' ':  # счет количества пробелов при печати
        spaces_printed += 1
        if spaces_printed >= 10:  # если распечатали 10 пробелов, делаем возврат коретки
            print()
            spaces_printed = 0
    sequence = sequence[1:] + char
