"""
Задача "План перехват":
Напишите 2 функции:
Функция personal_sum(numbers):
Должна принимать коллекцию numbers.
Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError,
увеличив счётчик incorrect_data на 1.
В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел,
incorrect_data - кол-во некорректных данных.
Функция calculate_average(numbers)
Среднее арифметическое - сумма всех данных делённая на их количество.
Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
Также в numbers может быть записана не коллекция, а другие типы данных, например числа.
Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'.
В таком случае функция просто вернёт None.

Пункты задачи:
Создайте функцию personal_sum на основе условий задачи.
Создайте функцию calculate_average на основе условий задачи.
Вызовите функцию calculate_average несколько раз, передав в неё данные разных вариаций.
"""

def personal_sum(numbers: list[int]):
    result: int = 0
    incorrect_data: int = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    return (result, incorrect_data)


def calculate_average(numbers: list[int]):
    # if not isinstance(numbers, list):  # Пригодится если мы хотим принят именно список, а не тюпл, словарь, множество
    #     return f'В numbers записан некорректный тип данных:'
    try:
        output: tuple = personal_sum(numbers)
        len_arr: int = len(numbers) - output[1]  # количество чисел
        arit_mean: int or float = output[0] / len_arr  # среднее арифметическое всех чисел
    except TypeError as e:
        print(f'В numbers записан некорректный тип данных: {e}')
        return
    except ZeroDivisionError as e:
        return 0
    return arit_mean


a = [1, '123', 2, 3, 'qwe', [1,1,1]]
b = (1, '123', 2, 3, 'qwe', [1,1,1])
c = {4: '123', 2: 'qwe', 3: 'zxc'}
d = 'qwe'
e = 1
print(calculate_average(a))
print(calculate_average(b))  # заругался, что передаю тюпл, а не список, но посчитал
print(calculate_average(c))  # заругался, что передаю словарь, а не список, но посчитал ключи
print(calculate_average(d))  # ZeroDivisionError
print(calculate_average('zxc'))  # ZeroDivisionError
print(calculate_average(e))  # TypeError





























