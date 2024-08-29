import pprint

def introspection_info(obj):
    print('Имя объекта', obj.__name__)
    print('Тип объекта', type(obj))
    print('Список доступных атрибутов и методов', dir(obj))
    # print('Документация объекта', help(obj))
    print('', help(obj))


introspection_info(str)










