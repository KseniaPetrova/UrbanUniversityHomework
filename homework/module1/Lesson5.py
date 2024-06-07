# Списки. Индексация и методы списков

# Лекция
# Списки - list = [ object1 , object2 ]
food = ['apple', 'coconut', 'banana']  # список, который может хранить объекты разных типов
print(food[0])  # вывод элемента по идексу. Работает так же как и со str [начало:конец:шаг]
food[0] = 'peach'  # перезаписать элемент по индексу
food.append(True)  # добавляет элемент в конец списка
food.insert(0, 1)  # по индексу 0 добавляет элемент 1
food.extend('str')  # добавит каждую букву как отдельный элемент [... 's', 't', 'r']
food.extend(['string', 2, 'int'])  # добавит три элемента
food.remove('banana')  # убирает выбранный элемент из списка
print('coconut' in food)  # in команда проверяющая нахождение элемента в списке. Возвращает true/false
print('apple' not in food)  # not in команда проверяющая отсутствие элемента в списке. Возвращает true/false
cut = food[1:-1:2]  # срез работает и со списком
print(food, "\n", cut, sep='')
# "\n" разделяет строки на абзацы
# функция print() по умолчанию добавляет пробел между аргументами, которые она выводит.
# Параметр sep изменяет разделитель
car = ['BMW', 'LADA', 'Toyota', 'Ford', 'Nissan', 'Renuaout']
print(car)  # ['BMW', 'LADA', 'Toyota', 'Ford', 'Nissan', 'Renuaout']
a = car.pop(1)  # вытащить из списка car значение LADA и присвоить переменной а
print(car)  # ['BMW', 'Toyota', 'Ford', 'Nissan', 'Renuaout']
print(a)  # LADA
print(type(car))