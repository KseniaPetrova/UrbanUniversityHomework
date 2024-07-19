"""Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
и обладать следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
Все данные в строке разделены запятой с пробелами.

Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его
и возвращает единую строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'
"""


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'Название: {self.name}. Вес: {self.weight}. Категория: {self.category}.'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        """Cчитывает всю информацию из файла __file_name, закрывает его и возвращает единую строку
        со всеми товарами из файла __file_name."""
        products_in_file = ''
        file_products = open(self.__file_name, 'r', encoding='utf-8')
        products_in_file = file_products.read()
        file_products.close()
        return products_in_file

    def add(self, *products: Product):
        """Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'."""
        file_products = open(self.__file_name, 'a', encoding='utf-8')
        for product in products:
            if product.name not in self.get_products():
                file_products.write(f'{product.__str__()}\n')
            else:
                print(f'Продукт {product.name} уже есть в списке')
        file_products.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())