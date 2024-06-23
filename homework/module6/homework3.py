"""
Ваша задача:
Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и
функцию def horse_powers, которая возвращает количество лошадиных сил для автомобиля
Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
а также переопределите функцию horse_powers
Создайте экземпляр класса Nissan и распечатайте через функцию print vehicle_type, price
"""

class Vehicle:
    vehicle_type = 'None'


class Car:
    price = 1000000

    def horse_powers(self):
        return 0


class Nissan(Vehicle, Car):
    vehicle_type = 'sedan'
    price = 980000

    def horse_powers(self):
        return 143


almera = Nissan()
print(f'Тип транспортного средства: {almera.vehicle_type}\nЦена: {almera.price}')