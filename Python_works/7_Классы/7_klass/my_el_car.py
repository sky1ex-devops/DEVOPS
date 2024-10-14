from car import ElCar

my_tesla = ElCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # Обращаемся к my_tesla, находим атрибут battery
                                    #  и вызываем метод describe_battery
my_tesla.battery.get_range()