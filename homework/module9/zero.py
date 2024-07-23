def all_variants(text):
    """
    Функция-генератор, которая возвращает все подпоследовательности переданной строки.
    """
    # Создаем список всех возможных длин подпоследовательностей
    lengths = list(range(1, len(text) + 1))

    # Проходим по всем возможным длинам
    for length in lengths:
        # Проходим по всем возможным начальным индексам
        for start in range(len(text) - length + 1):
            # Возвращаем подпоследовательность
            yield text[start:start + length]


a = all_variants("abc")
for i in a:
    print(i)

print(len('abc'))