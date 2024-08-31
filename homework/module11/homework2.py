import pprint
import inspect


def introspection_info(obj):
    if isinstance(obj, (str, int, float, type)):
        print('Объект', obj)
    elif inspect.isfunction(obj):
        print('Имя объекта', obj.__name__)
    elif callable(getattr(obj,'__class__')):
        print('Объект является объектом класса')
    print('Тип объекта', type(obj))
    print('Список доступных атрибутов и методов', dir(obj))
    # print('Документация объекта', help(obj))
    if not isinstance(obj,(str,int,float)):
        print('Модуль', obj.__module__)
    print('ID', id(obj))
    dunder_methods = []
    methods = []
    for method in dir(obj):
        if callable(getattr(obj, method)) and method.startswith("__") and method.endswith("__"):
            dunder_methods.append(method)
        elif callable(getattr(obj, method)) and not method.startswith("__") and not method.endswith("__"):
            methods.append(method)
    print('Магические методы', dunder_methods)
    print('Методы', methods)
    print()

def sum_three(a, b, c):
    return a + b + c
class new_class:
    def __init__(self, number):
        self.multi = int(number) * 2
        self.string = str(number)


a: new_class = new_class(8)
introspection_info("72")
introspection_info(sum_three)
introspection_info(True)
introspection_info(new_class)
introspection_info(a)
















































