

#############################################################################################

#### Удаление конкретных значений из списка

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
print(pets)

while 'cat' in pets:    # выполняем цикл пока есть значения 'cat' в списке pets
    pets.remove('cat')  # удаляем 'cat' из списка

print(pets)             # выводим получившейся список