"""
Задание "Раз, два, три, четыре, пять .... Это не всё?":
Все ученики урбана, без исключения, — очень умные ребята. Настолько умные, что иногда по утру сами путаются в том, что
намудрили вчера вечером.
Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже после сна,
его код остался рабочим и выглядел следующим образом:

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по разному.

Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких структур
он не нашёл.

Помогите сокурснику осуществить его задумку.

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Входные данные (применение функции):
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


Выходные данные (консоль):
99


Примечания (рекомендации):
Весь подсчёт должен выполняться одним вызовом функции.
Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
Для определения типа данного используйте функцию isinstance.
"""

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

test1 = {'cube': 7, 'drum': 8, 4: [1, 2, 3]}


def calculate_structure_sum(*args):
    sum_list = []
    for item in args:
        if isinstance(item, (list, tuple, set)):
            for sub_item in item:
                sum_list.append(calculate_structure_sum(sub_item))
        if isinstance(item, dict):
            for sub_item in item:
                sum_list.append(calculate_structure_sum(item.get(sub_item)))  # в конец листа добавляется, полученное(.get) из словаря(item) значение по ключу(sub_item)
                sum_list.append(calculate_structure_sum(sub_item))
        if isinstance(item, str):
            sum_list.append(len(item))
        if isinstance(item, int):
            sum_list.append(item)
    return sum(sum_list)


res = calculate_structure_sum(data_structure)
res2 = calculate_structure_sum(test1)
print(res)
print(res2)

'''
Ниже рассуждения о решении
'''
# list1 = [1, 2, 3]
# dict2 = {'a': 4, 'b': 5}
# tuple3 = (6, {'cube': 7, 'drum': 8})
# str4 = 'Hello'
# tuple5 = ((), [{(2, 'Urban', ('Urban2', 35))}])

# sum_ = 0

# for i in list1:
#     if type(i) is int:
#         sum_ += i
#     if isinstance(i, str):
#         sum_ += len(i)
# print(sum_)

# for i in dict2:
#     if isinstance(i, str):
#         key = len(i)
#         sum_ += key
#     if isinstance(i, int):
#         sum_ += i
#     value = dict2.get(i)
#     if isinstance(value, str):
#         value = len(value)
#         sum_ += value
#     if isinstance(value, int):
#         sum_ += value
# print('dict2', sum_)
# sum_ = 0
# tuple3 = (6, {'cube': 7, 'drum': 8})
# for i in tuple3:
#     if type(i) is int:
#         sum_ += i
#     if isinstance(i, str):
#         sum_ += len(i)
#     if isinstance(i, dict):
#         for j in i:
#             if isinstance(j, str):
#                 key = len(j)
#                 sum_ += key
#             if isinstance(j, int):
#                 sum_ += j
#             value = i.get(j)
#             if isinstance(value, str):
#                 value = len(value)
#                 sum_ += value
#             if isinstance(value, int):
#                 sum_ += value
# print('tuple3', sum_)

# for i in str4:
#     if isinstance(i, str):
#         sum_ += len(i)
# print(sum_)

# tuple5 = ((), [{(2, 'Urban', ('Urban2', 35))}])
# for i in tuple5:
#     while type(i) is list or tuple or set or dict:
#         if type(i) is list:

# <class 'list'>
# <class 'dict'>
# <class 'tuple'>
# <class 'str'>
# <class 'tuple'>
