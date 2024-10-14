class Car():
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атребуты описания автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odom = 0

    def get_descriptive_name(self):
        """Возвращает отфарматированиое описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Выводит пробег машины"""
        print(f"Машина проехала {self.odom} км")

    def update_odometer(self, klm):
        """Заданное значение га одометре.
        при попытке обратной подкрутки
        изменения отклоняются"""
        if klm >= self.odom:
            self.odom = klm
        else:
            print("Не верное значение км.")

    def increment_odom(self, klm):
        """Увеличение показания одометра с заданным приращиванием"""
        self.odom += klm

class Battery():
    """Простая модель аккумулятора элктромобиля"""
    def __init__(self, battery_size=75):
        """Инициализация атрибутов АКБ"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Выводит информацию о мощьности АКБ"""
        print(f"This car has a {self.battery_size} -kwh")

    def get_range(self):
        """Выводит приблизительный запас хода"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range - 315

        print(f"This car can go about {range} klm on a full charge")

class ElCar(Car):
    """Предоставляет аспекты машины, специфические для электромобиля"""

    def __init__(self, make, model, year):
        """инициализация атрибутов класс-родителя"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Выводит информацию о мощности АКБ"""
        print(f"This car has a {self.battery_size} -kwh")
    
    def fill_gas_tank(self):
        """У электромобиля нет бинзобака"""
        print("This car doesn't need a gas tank")

my_used_car = Car('subaru', 'outbask', 2015)
print(my_used_car.get_descriptive_name())
my_used_car .update_odometer(56000)
my_used_car .read_odometer()

my_used_car .increment_odom(250)
my_used_car .read_odometer()

print("\n")
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(25)
my_new_car.read_odometer()

print("\n")
my_tesla = ElCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # Обращаемся к my_tesla, находим атрибут battery
                                    #  и вызываем метод describe_battery
my_tesla.battery.get_range()
print("\n")