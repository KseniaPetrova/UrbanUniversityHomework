import pprint
import inspect


def introspection_info(obj):
    info = {}
    info['Тип объекта'] = type(obj)
    attributes = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)
    info['Атрибуты'] = attributes
    info['Методы'] = methods
    info['Модуль'] = __name__
    info['ID'] = id(obj)
    return info


number_info = introspection_info(42)
print(number_info)


#-----------------------------------------------------------

# def introspection_info(obj):
#     info = {}
#     if isinstance(obj, (str, int, float, type)):
#         info['Объект'] = obj
#     elif inspect.isfunction(obj):
#         info['Имя объекта'] = obj.__name__
#     # elif callable(getattr(obj,'__class__')):
#     #     print('Объект является объектом класса')
#     info['Тип объекта'] = type(obj)
#     if not isinstance(obj,(str,int,float)):
#         info['Модуль'] = obj.__module__
#     dunder_methods = []
#     methods = []
#     for method in dir(obj):
#         if callable(getattr(obj, method)) and method.startswith("__") and method.endswith("__"):
#             dunder_methods.append(method)
#         elif callable(getattr(obj, method)) and not method.startswith("__") and not method.endswith("__"):
#             methods.append(method)
#     info['Магические методы'] = dunder_methods
#     info['Методы'] = methods
#     if not inspect.isbuiltin(obj) and not isinstance(obj, (str,int,float,bool)):
#         info['Атрибуты'] = obj.__dict__
#     # print('Список доступных атрибутов и методов', dir(obj))
#     # print('Документация объекта', help(obj))
#     info['ID'] = id(obj)
#     return info

# def sum_three(a:int, b:int, c:int) -> int:
#     sum_three.x = '23'
#     return a + b + c
# class new_class:
#     pi = 3.14
#     def __init__(self, number):
#         self.multi = int(number) * 2
#         self.string = str(number)
#
#
# a: new_class = new_class(8)
# sum_three(1,2,3)
# info_func = introspection_info(sum_three)
# info_str = introspection_info("72")
# info_bool = introspection_info(True)
# info_class = introspection_info(new_class)
# info_buit = introspection_info(sum)
# info_obj_class = introspection_info(a)
#
# print(info_func)
# print(info_str)
# print(info_bool)
# print(info_class)
# print(info_buit)
# print(info_obj_class)












































