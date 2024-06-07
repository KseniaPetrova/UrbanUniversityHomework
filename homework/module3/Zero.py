

# def count_numbers_and_strings(data):  # когда на вход принимается один аргумент
#     ttl = 0
#     for element in data:
#         if isinstance(element, (list, tuple, set)):
#             for sub_element in element:
#                 ttl += count_numbers_and_strings([sub_element])    # здесь к саб_элементу обращаемся через []
#         elif isinstance(element, dict):  # словарь не обрабатывается
#             for value in element.values():
#                 ttl += count_numbers_and_strings([value])
#         elif isinstance(element, int):
#             ttl += element
#         elif isinstance(element, str):
#             ttl += len(element)
#
#     return ttl
#
#
# test1 = ({'cube': 7, 'drum': 8, 4: [1, 2, 3]})
# total2 = count_numbers_and_strings(test1)
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# total = count_numbers_and_strings(data_structure)
# print("Total sum of numbers and lengths of strings:", total)

a = False
b = True
print(a or b)