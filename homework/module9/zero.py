import time
import threading
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.customer_id = 0

    def customer_arrival(self):
        while self.customer_id < 10:
            self.serve_customer(self.customer_id)
            self.customer_id += 1
            time.sleep(1)

    def serve_customer(self, customer_id):
        print(f"Посетитель номер {customer_id} прибыл.")

        free_table = self.find_free_table()
        if free_table:
            self.start_serving(customer_id, free_table)
        else:
            self.queue.put(customer_id)
            print(f"Посетитель номер {customer_id} ожидает свободный стол.")

    def find_free_table(self):
        for table in self.tables:
            if not table.is_busy:
                return table
        return None

    def start_serving(self, customer_id, table):
        table.is_busy = True
        print(f"Посетитель номер {customer_id} сел за стол {table.number}.")

        threading.Thread(target=self.serve, args=(customer_id, table)).start()

    def serve(self, customer_id, table):
        time.sleep(5)
        table.is_busy = False
        print(f"Посетитель номер {customer_id} покушал и ушёл.")

        if not self.queue.empty():
            next_customer = self.queue.get()
            self.start_serving(next_customer, table)

class Customer(threading.Thread):
    def __init__(self, cafe, customer_id):
        super().__init__()
        self.cafe = cafe
        self.customer_id = customer_id

    def run(self):
        self.cafe.serve_customer(self.customer_id)

# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
