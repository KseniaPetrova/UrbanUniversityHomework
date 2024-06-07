# print("Hello word")
# print(23891471923807487.142352314353455 +
#       23891471923843245.142352314334563 >
#       23891471923807487.142352314356734 +
#       23891471923843245.142352314334553)
#
# num1 = 23891471923807487.142352314353455
# num2 = 23891471923807487.142352314356734
# num3 = 23891471923843245.142352314334563
# num4 = 23891471923843245.142352314334553
#
# sum1 = num1 + num3
# sum2 = num2 + num4
# print(sum1 > sum2)
#
# name = 'Denis'
# print(name[0:5:3])  # [начало массива:конец массива:шаг]
# # если шаг -1 то массив будет ввыведен в обратном порядке
# print(name[0:-1])
#
# # ПРЕОБРАЗОВАНИЕ КОРТЕЖА В ЛИСТ
# tuple_4 = (1, 'str', True, [2, 3])
# list_5 = [element if isinstance(element, list) else [element] for element in tuple_4]
# print(list_5)
#
#
# tuple_9 = (1, 'str', True, [2, 3])
# list_9 = []
# for element in tuple_9:
#     if isinstance(element, list):
#         list_9.append(element)
#     else:
#         list_9.append([element])
# print(list_9)

# list_te = [1, 5, 3, 4, 2, 8]
# print(sum(list_te))

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)


print(fac(5))
f = 5 * 4 * 3 * 2 * 1 * 5
print(f)