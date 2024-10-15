
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # Сортровка по алфавиту - sort
print(cars)
cars.sort(reverse=True) # Сортровка по алфавиту в обратном порядке 

print(f"\n{cars}")
print(sorted(cars)) # Сортровка по алфавиту временно - sorted
print(cars)

cars_rev = sorted(cars, reverse=True) # Сортровка по алфавиту в обратном порядке временно - sorted
print(cars_rev)

cars.sort()
print(f"\n{cars}")

cars.reverse() # Переход к обратному порядку списка 
print(cars)

cars.reverse() # Переход к обратному порядку списка 
print(cars)

lenlist = len(cars) # Показывает количество элементов в списке
print(f"\nЭлементов в списке: {lenlist} ")