"""Моржовый оператор"""

if (number := int(input())) < 10000:
    print(f'Сумма {number} не превышает лимит, проходите')
else:
    print(f'Ого! {number}! Куда вам столько? Мы заберем {number - 10000}')

# if number := int(input()) < 10000:  # number == True
# if (number := int(input())) < 10000:  # number == input

if "walrus" in (number := input()):
    print(f'Нашли моржа')
else:
    print(f'Никаких моржей тут нет')

# s = input()
# t = input()
if (s := input()) == (t := input()[::-1]):  # Если слово t является словом s, записанным наоборот, выведите YES, иначе выведите NO.
    print('YES')
else:
    print('NO')

if (a := input()) == a[::-1]:
    print('YES')
else:
    print('NO')