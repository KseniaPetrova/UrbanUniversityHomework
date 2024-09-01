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
    if not isinstance(obj,(str,int,float)):
        print('Модуль', obj.__module__)
    dunder_methods = []
    methods = []
    for method in dir(obj):
        if callable(getattr(obj, method)) and method.startswith("__") and method.endswith("__"):
            dunder_methods.append(method)
        elif callable(getattr(obj, method)) and not method.startswith("__") and not method.endswith("__"):
            methods.append(method)
    print('Магические методы', dunder_methods)
    print('Методы', methods)
    if not inspect.isbuiltin(obj) and not isinstance(obj, (str,int,float,bool)):
        print('Атрибуты', obj.__dict__)
    # print('Список доступных атрибутов и методов', dir(obj))
    # print('Документация объекта', help(obj))
    print('ID', id(obj))
    print()

def sum_three(a:int, b:int, c:int) -> int:
    sum_three.x = '23'
    return a + b + c
class new_class:
    pi = 3.14
    def __init__(self, number):
        self.multi = int(number) * 2
        self.string = str(number)


a: new_class = new_class(8)
sum_three(1,2,3)
introspection_info(sum_three)
introspection_info("72")
introspection_info(True)
introspection_info(new_class)
introspection_info(sum)
introspection_info(a)

















































