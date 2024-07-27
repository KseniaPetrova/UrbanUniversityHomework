# Задача - есть функция, которая возвращает результат введения числа в степень b.
# Нужно усторить ее, чтобы она не делала повторные вычисления

def memoize_func(f):
    mem: dict = {}

    def wrapper(*args):
        print(f'Выполняем функцию с аргументами={args}, внутреняя память={mem} ')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась, ответ={mem[args]}'
        else:
            return f'Функция была выполнена раньше,ответ={mem[args]}'
    return wrapper

@memoize_func
def func(a: int, b: int):
    print(f'Выполняем функцию с аргументами ({a}, {b})')
    return a ** b

print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')