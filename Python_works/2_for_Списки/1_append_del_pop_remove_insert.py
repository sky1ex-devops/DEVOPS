bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles[0]) # отобразит 1й элемент из списка
print(bicycles[0].title()) 
print(bicycles[-2].title()) # отобразит 2й элемент с конца списка

message = f"My first bicycle was a {bicycles[1].title()}.\n"
print(message)

names = ['Djony', 'Alex', 'Serj', 'Shurik']
message = "This message to "
print(f"{message}{names[0]}")
print(f"{message}{names[1]}")
print(f"{message}{names[2]}")
print(f"{message}{names[3]}\n")

# Изменение в списке
motos = ['honda', 'suzuki', 'yamaha']
print(motos)
motos[2] = 'ducati' # Изменит 1й элемент в списке на заданное зхначение
print(motos)

# Добавление в список
motos.append('ИЖ') #  Добавление в конец списка 
motos.append('BMW')
motos.insert(0,'yral') # Добавление в указанное место
motos.append('Ишак')
print(motos)

# удаление в списке
del motos[2]
print(motos)

# удаление методом pop
popped_motos = motos.pop() # удаляет последний элемент из списка
print(motos)
print(popped_motos)
list_purchased = motos.pop()
print(f"{list_purchased.title()} - This bike purchased\n")

# Удаление первого элемента из списка
list_purchased2 = motos.pop(0)
print(f"Приз в студию!!! Это же мотоцикл {list_purchased2.title()}!\n")

# Удаление затем использование значения с помощью .remove() 
too_expensive = 'ИЖ'
motos.remove(too_expensive)
print(motos)
print(f"\n{too_expensive.title()} - Был удален из списка, так как нужно было что то удалить.\n")
###############################################################################################
# Метод remove удаляет первое совпадение, если есть повторения, необходимо использовать цикл. #
###############################################################################################

