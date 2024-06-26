"""
Задача "Счётчик вызовов":
Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт
вызовов автоматически.
Давайте реализуем данную фишку самостоятельно!

Вам необходимо написать 3 функции:
Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
Пункты задачи:
Создать переменную calls = 0 вне функций.
Создать функцию count_calls и изменять в ней значение переменной calls.
Эта функция должна вызываться в остальных двух функциях.
Создать функцию string_info с параметром string и реализовать логику работы по описанию.
Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
Вывести значение переменной calls на экран(в консоль).

Примечания:
Для использования глобальной переменной внутри функции используйте оператор global.
Для функции is_contains лучше привести и искомую строку и все строки в списке в один регистр.
"""
calls = 0


def count_calls():  # подсчитывающая вызовы остальных функций
    global calls
    return calls


def string_info(string: str):  # принимает аргумент - строку и возвращает кортеж из: длины этой строки,
    # строку в верхнем регистре,
    # строку в нижнем регистре
    global calls
    calls += 1
    len_str = len(string)
    up_str = string.upper()
    low_str = string.lower()
    tuple_ = (len_str, up_str, low_str)
    return tuple_


def is_contains(string: str, list_to_search: list):  # принимает два аргумента: строку и список, и
    # возвращает True, если строка находится в этом списке,
    # False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
    global calls
    calls += 1
    string = string.lower()
    for item in list_to_search:
        item = item.lower()
        if string == item:
            return True
    return False


print(string_info('Capybara'))  # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycle', 'cyclic']))  # False
print(count_calls())  # 4
