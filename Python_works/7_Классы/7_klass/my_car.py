from car import Car, ElCar # импортируем класс Car и ElCar
from car  # Импортируем весть модуль
from car import * # импорт всех классов
# Также можно импортировать классы из модуля в модуль  from car import car
# Можно использовать псевданимы from car import Car as MC

print("\n")
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(25)
my_new_car.read_odometer()