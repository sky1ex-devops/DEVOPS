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

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odom = 23
my_new_car.read_odometer()