"""Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат
1ой функции будет простым числом и "Составное" в противном случае."""

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result in [2, 3]:
            return f'Простое - {result}'
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                return f'Составное - {result}'
        return f'Простое - {result}'
    return wrapper

@is_prime
def sum_three(*args):
    sum_ = sum(args)
    return sum_

result = sum_three(2, 0, 0)
result1 = sum_three(2, 1, 0)
result2 = sum_three(2, 3, 0)
result3 = sum_three(2, 3, 2)
result4 = sum_three(2, 3, 6)
result5 = sum_three(4)
result6 = sum_three(6)
result7 = sum_three(8)
result8 = sum_three(9)
result9 = sum_three(10)

print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)














