"""Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text
и возвращает объект-генератор, при каждой итерации которого будет возвращаться
подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации."""


def all_variants(text: str):
    for length in range(1, len(text) + 1):  # 1 | 2 | 3 | длина строки
        for start in range(len(text) - length + 1):  # 3 | 2 | 1 | количество вариантов
            yield text[start:start + length]  # [0:1],[1:2],[2:3] | [0:2],[1:3] | [0:3]


a: all_variants = all_variants("abc")
for i in a:
    print(i)


















