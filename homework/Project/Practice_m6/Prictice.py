# Реализуем модель доставки грузов
#
# Дорога - хранит расстояния между объектами
# Склад - хранит груз и управляет очередями грузовиков

#
# Базовый класс - Машина
# имеет кол-во топлива, может заправляться

# Грузовик (производный от Машина)
# имеет емкость кузова, скорость движения, расход топлива за час поездки
# может стоять под погрузкой/разгрузкой, ехать со скоростью

# Погрузчик (производный от Машина)
# имеет скорость погрузки, расход топлива в час при работе
# может загружать/разгружать грузовик, ждать грузовик
from termcolor import cprint


class Road:  # Дорога

    def __init__(self, start, end, distance):  # начало, конец, расстояние
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:  # Склад

    def __init__(self, name, content=0):  # название, содержимое
        self.name = name
        self.content = content
        self.road_out = None
        self.queue_in = []  # очередь грузовиков на загрузку
        self.queue_out = []  # очередь грузовиков на разгрузку

    def __str__(self):
        return 'Склад {}, груза {}'.format(self.name, self.content)

    def set_road_out(self, road):  # дорога со склада
        self.road_out = road

    def truck_arrived(self, truck):  # грузовик прибыл на склад
        self.queue_in.append(truck)
        truck.place = self
        print('{} прибыл грузовик {}'.format(self.name, truck))

    def get_next_truck(self):  # выбор грузовика для разгрузки/загрузки
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):  # сообщает складу, что погрузчик закончил работу
        # с грузовиком
        self.queue_out.append(truck)
        print('{} грузовик готов {}'.format(self.name, truck))

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)


class Vehicle:  # Машины
    fuel_rate = 0  # скорость потребления топлива
    total_fuel = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0  # по умолчанию в машине нет топлива

    def __str__(self):  # вывод на консаоль
        return '{} топлива {}'.format(self.model, self.fuel)

    def tank_up(self):  # заправить машину
        self.fuel += 1000
        Vehicle.total_fuel += 1000
        print('{} заправился'.format(self.model))

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
            return False
        return True


class Truck(Vehicle):  # Грузовик
    fuel_rate = 50
    dead_time = 0  # Время простоя

    def __init__(self, model, body_space=1000):  # ёмкость грузовика по умолчанию 1000кг
        super().__init__(model=model)
        self.body_space = body_space
        self.cargo = 0  # сколько может везти груза
        self.velocity = 100  # скорость движения
        self.place = None  # где находится
        self.distance_to_target = 0  # сколько еще ехать

    def __str__(self):
        res = super().__str__()
        return res + 'груза {}'.format(self.cargo)

    def ride(self):  # едет по дороге
        self.fuel -= self.fuel_rate
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            print('{} едет по дороге, осталось {}'.format(self.model, self.distance_to_target))
        else:  # если расстояние до конечной точки меньше скорости грузовика
            self.place.end.truck_arrived(self)  # зарегистрирует в очередь прибывший грузовик
            print('{} доехал'.format(self.model))

    def go_to(self, road):  # выезжает на дорогу со склада и едет
        self.place = road
        self.distance_to_target = road.distance
        print(f'{self.model} выехал в путь')

    def act(self):  # принятия решений почасовое
        if super().act():
            if isinstance(self.place, Road):  # Если место это дорога
                self.ride()
            else:
                Truck.dead_time += 1  # простаивал


class OtherTruck(Truck):
    fuel_rate = 100


class AutoLoader(Vehicle):   # Погрузчик
    fuel_rate = 30
    dead_time = 0

    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        # ёмкость ковша=100, склад к которому он привязан, загружает/разгружает грузовик
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None  # у погрузчика должен быть грузовик. по умолчанию простаивает

    def __str__(self):
        res = super().__str__()
        return res + ' грузим {}'.format(self.truck)

    def act(self):
        if super().act():
            if self.truck is None:
                self.truck = self.warehouse.get_next_truck()
                if self.truck is None:
                    print('{} нет грузовиков для работы'.format(self.model))
                    AutoLoader.dead_time += 1
                else:
                    print('{} взял в работу {}'.format(self.model, self.truck))
            elif self.role == 'loader':
                self.load()
            else:
                self.unload()

    def load(self):  # загрузчик
        if self.warehouse.content == 0:
            print('{} на складе ничего нет!'.format(self.model))
            if self.truck:
                self.warehouse.truck_ready(self.truck)
                self.truck = None
            return
        self.fuel -= self.fuel_rate
        truck_cargo_rest = self.truck.body_space - self.truck.cargo  # количество груза в грузовике
        if truck_cargo_rest >= self.bucket_capacity:  # если надо загрузить больше чем ёмкость ковша
            cargo = self.bucket_capacity
        else:
            cargo = truck_cargo_rest
        if self.warehouse.content < cargo:
            cargo = self.warehouse.content
        self.warehouse.content -= cargo  # когда осталось загрузить не полный ковш
        self.truck.cargo += cargo
        print('{} грузил {}'.format(self.model, self.truck))
        if self.truck.cargo == self.truck.body_space:   # если грузовик полностью загружен
            self.warehouse.truck_ready(self.truck)  # погрузчик закончил работу с текущим грузовиком
            self.truck = None

    def unload(self):  # разгрузчик
        self.fuel -= self.fuel_rate
        if self.truck.cargo >= self.bucket_capacity:  # если места в грузовике больше объема ковша
            self.truck.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity
        else:
            self.truck.cargo -= self.truck.cargo
            self.warehouse.content += self.truck.cargo
        print('{} разгрузил {}'.format(self.model, self.truck))
        if self.truck.cargo == 0:   # если грузовик полностью разгружен
            self.warehouse.truck_ready(self.truck)  # погрузчик закончил работу с текущим грузовиком
            self.truck = None


TOTAL_CARGO = 100000

moscow = Warehouse(name='Москва', content=TOTAL_CARGO)  # склад в москве
piter = Warehouse(name='Питер', content=0)  # склад в Питере

moscow_piter = Road(start=moscow, end=piter, distance=715)  # дорога москва-питер
piter_moscow = Road(start=piter, end=moscow, distance=780)  # дорога питер-москва

moscow.set_road_out(moscow_piter)  # дорога со склада москвы
piter.set_road_out(piter_moscow)  # дорога со склада питера

loader_1 = AutoLoader(model='Bobcat', bucket_capacity=1000, warehouse=moscow, role='loader')  # погрузчик в МСК
loader_2 = AutoLoader(model='Lonking', bucket_capacity=500, warehouse=piter, role='unloader')  # погрузчик в СПБ

trucks = []
for number in range(5):
    truck = Truck(model='КАМАЗ #{}'.format(number), body_space=5000)
    moscow.truck_arrived(truck)
    trucks.append(truck)

for number in range(5):
    truck = OtherTruck(model='Volvo #{}'.format(number), body_space=10000)
    moscow.truck_arrived(truck)
    trucks.append(truck)

hour = 0
while piter.content < TOTAL_CARGO:  # пока содержимое питерского склада меньше общего содержимого товара
    hour += 1
    print(f'--------------- Час {hour} ---------------')
    for truck in trucks:
        truck.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    for truck in trucks:
        print(truck)
    print(loader_1)
    print(loader_2)
    print(moscow)
    print(piter)


print('Всего затрачено топлива {}'.format(Vehicle.total_fuel))
print('Общий простой грузовиков {}'.format(Truck.dead_time))
print('Общий простой погрузчиков {}'.format(AutoLoader.dead_time))
