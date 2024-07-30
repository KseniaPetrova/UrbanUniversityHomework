"""Задание:
Моделирование работы сети кафе с несколькими столиками и потоком посетителей, прибывающих для заказа
пищи и уходящих после завершения приема.

Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют
еду и уходят. Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в
очередь на ожидание.

Создайте 3 класса:
Table - класс для столов, который будет содержать следующие атрибуты: number(int) - номер стола,
is_busy(bool) - занят стол или нет.

Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных
столов, в случае наличия стола - начинает обслуживание посетителя (запуск потока), в противном случае
- посетитель поступает в очередь. Время обслуживания 5 секунд.
Customer - класс (поток) посетителя. Запускается, если есть свободные столы.

Так же должны выводиться текстовые сообщения соответствующие событиям:
Посетитель номер <номер посетителя> прибыл.
Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)"""

import queue
import time
from threading import Thread

class Table:

    def __init__(self, number: int, is_busy: bool=False):
        self.number = number
        self.is_busy = is_busy


class Cafe:

    def __init__(self, tables: list):
        self.queue = queue.Queue()
        self.tables = tables
        self.visitor = 0

    def customer_arrival(self):
        """моделирует приход посетителя(каждую секунду)"""
        visitor_max = 10
        while self.visitor < visitor_max:
            self.visitor += 1
            self.queue.put(self.visitor)
            print(f'Посетитель номер {self.visitor} прибыл')
            time.sleep(1)

    def serve_customer(self, customer):
        """моделирует обслуживание посетителя. Проверяет наличие свободных столов,
        в случае наличия стола - начинает обслуживание посетителя (запуск потока),
        в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд"""
        self.visitor = self.queue.get()
        for tabel in self.tables:
            if tabel.is_busy is False:
                tabel.is_busy = True
                print(f'Посетитель номер {self.visitor} сел за стол {tabel.number}. (начало обслуживания)')
                time.sleep(5)
                tabel.is_busy = False
                print(f'Посетитель номер {self.visitor} покушал и ушёл. (конец обслуживания)')
                return
        self.queue.put(self.visitor)
        print(f'Посетитель номер {self.visitor} ожидает свободный стол. (помещение в очередь)')



class Customer(Thread):
    def __init__(self):
        super().__init__()



    def run(self):
        pass

# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
serve_customer_thread = Thread(target=cafe.serve_customer)

customer_arrival_thread.start()
serve_customer_thread.start()

customer_arrival_thread.join()
serve_customer_thread.join()

































