"""Методы строк
Строки являются неизменяемым объектом
Строки можно складывать и умножать
Строки можно сравнивать.
Строки можно сравнивать также с помощью операторов > и <. Python сравнивает строки посимвольно. Чем дальше в алфавите буква - тем больше её значение."""

string = 'Hello world. How are you?'
print(len(string))  # 25 |
print(ord('A'))  # 65 | Возвращает числовое значение каждого символа в ascii code
print('world' in string)  # True | Проверяет есть ли подстрока в строке
"""Индексы строк
0 1 2 3 4 5 6 7 8 9 
H e l l o   w o r d
 -10 - 9 -8 -7 -6 -5 -4 -3 -2 -1"""
"""Cрезы"""
print(string[6])  # w
print(string[-4])  # y
print(string[0:4])  # Hell
print(string[6:-3])  # world. How are y
print(string[:-1])  # Hello world. How are you
print(string[::2])  # Hlowrd o r o?
print(string[::-1])  # ?uoy era woH .dlrow olleH
"""Методы"""
print(string.upper())  # HELLO WORLD. HOW ARE YOU?
print(string.lower())  # hello world. how are you?
print(string.title())  # Hello World. How Are You?
print(string.capitalize())  # Hello world. how are you?
print(string.swapcase())  # hELLO WORLD. hOW ARE YOU?
print(string.count('o', 3, 8))  # 2 | Количество букв "0" с 3 по 8 позицию == 2
print(string.index('w'))  # 6 | Индекс подстроки в строке
print(string.replace('l', 'x', 2))  # Hexxo world. How are you?
print(string.isalpha())  # False | строка состоит только из букв
print(string.isdigit())  # False | строка состоит только из цифр
print(string.rjust(33, '0'))  # 00000000Hello world. How are you? | Заполнитель справа. По умолчанию пробел
print(string.ljust(33, '!'))  # Hello world. How are you?!!!!!!!! | Заполнитель слева
print(string.split())  # ['Hello', 'world.', 'How', 'are', 'you?'] | Превращает строку в список по разделителю.  По умолчанию пробел
print('-'.join(['hello', 'word', '!!!']))  # hello-word-!!! |  Склеивает список  по разделителю
string = '   Hello word. How are you?    '
print(string.strip())  # Удаляет знаки пробела и переноса на новую строку
print(string.rstrip())  #  Удаляет знаки пробела и переноса только справа
print(string.lstrip())  #  Удаляет знаки пробела и переноса только слева
print(string.find('o', 5))  # 7 | Возвращает индекс первого слева вхождения строки. Возвращает -1 если ничего не нашёл
print(string.rfind('d'))  # 12 | Возвращает индекс первого справа вхождения строки. Возвращает -1 если ничего не нашёл
print(string.index('w'))  # 9 | Возвращает индекс первой найденной подстроки, аналогично методу .find . Но выдаст ошибку если ничего не найдёт
print(string.islower())  # Методы is*** проверяют состоит ли строка из следующих методов isupper, isdigit, isalpha, isalnum(строка состоит из букв и цифр), istitle,
print(string.ljust(40, '-'))  #    Hello word. How are you?    --------- | Метод  .ljust принимает один обязательный параметр width - ширину строки и один необязательный параметр fillchar - знак заполнителя (по умолчанию пробел) . Возвращает новую строку, в которой исходная строка S дополнена справа символами fillchar до указанной длины width. Если параметр width меньше длины строки, то будет возвращена исходная строка без изменений:
print(string.rjust(40, '0'))  # 000000000   Hello word. How are you?   | принимает один обязательный параметр width - ширину строки и один необязательный параметр fillchar - знак заполнителя (по умолчанию пробел) . Возвращает новую строку, в которой исходная строка S дополнена слева символами fillchar до указанной длины width. Если параметр width меньше длины строки, то будет возвращена исходная строка без изменений
print(string.center(40, '&'))  # &&&&   Hello word. How are you?    &&&&& | принимает один обязательный параметр width - ширину строки и один необязательный параметр fillchar - знак заполнителя (по умолчанию пробел) . Возвращает новую строку длины width, в которой исходная строка S находится в центре, а справа и слева от нее находятся символы fillchar . Если параметр width меньше длины строки, то будет возвращена исходная строка без изменений.
print(string.zfill(40))  # 000000000   Hello word. How are you?  | возвращает новую строку, в которой исходная строка S дополнена нулями слева так, чтобы длина новой строки стала равна width
print(string.strip())  # S.strip([chars]) Метод  .strip возвращает копию строки, удаляя как начальные, так и конечные символы (в зависимости от переданного строкового аргумента). Метод удаляет символы как слева, так и справа в зависимости от аргумента chars . Если аргумент chars не передан, то по умолчанию удаляться пробелы и символы переноса на новую строку \n. Символы в параметре chars рассматриваются не как последовательность, а как набор символов, которые необходимо удалить/
print(string.rstrip())  # S.rstrip([chars]) Метод  .rstrip возвращает копию строки, в которой справа удалены указанные символы (по умолчанию удаляются пробельные символы)
print(string.lstrip())  # S.lstrip([chars]) Метод  .lstrip возвращает копию строки, в которой слева удалены указанные символы (по умолчанию удаляются пробельные символы
print(string.partition('o'))  # S.rpartition(sep) Метод  .partition разбивает строку по указанному разделителю и возвращает кортеж из трех элементов: строка до разделителя, сам разделитель и строка после разделителя. Если разделитель не найден, то возвращается кортеж так же состоящий из трех элементов в котором первый элемент – это исходная строка S, а два других элемента – это пустые строки.
text = "Python is best"
print(text.partition('is '))  # ('Python ', 'is ', 'best')
print(text.partition('not '))  # ('Python is best', '', '')
s = "Python is best, isn't it"
print(s.partition('is'))  # ('Python ', 'is', " best, isn't it")

print(string.rpartition('o'))  # S.rpartition(sep) Метод  .rpartition разбивает строку по последнему встреченному разделителю sep и возвращает кортеж, который состоит из трех элементов: строки до разделителя, самого разделителя и строки после разделителя. Если разделитель в строке отсутствует, то кортеж будет состоять из: двух пустых строк и исходной строки
