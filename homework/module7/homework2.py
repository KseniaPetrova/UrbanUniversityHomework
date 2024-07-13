"""
Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), которая принимает аргументы
file_name - название файла для записи, strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
а значением - записываемая строка. Для получения номера байта начала строки используйте
метод tell() перед записью.
Пример полученного словаря:
{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
Где:
1, 2 - номера записанных строк.
0, 16 - номера байт, на которых началась запись строк.
'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
"""


def custom_write(file_name, strings: list):
    strings_positions: dict = {}
    file = open(file=file_name, mode='a', encoding='utf8')
    for num_str, string in enumerate(strings, start=1):  # enumerate используется для перечисления
        # элементов последовательности (список, кортеж, строка и т.д.) с добавлением индекса каждого элемента.
        num_bb_str = file.tell()
        file.write(f'{string} \n')
        strings_positions[num_str, num_bb_str] = string
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# Использование range вместо enumerate
"""def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, len(strings) + 1):
            start_position = file.tell()
            file.write(strings[i-1] + '\n')
            strings_positions[(i, start_position)] = strings[i-1]
    return strings_positions
"""