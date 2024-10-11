players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3]) # вывести часть списка, 1-3 значение
print(players[-3:]) # отобразим последние 3 значения из списка

print("\nВыводим первые 3 значения списка:")
for player in players[0:3]: # обработать сигмент списка в цикле
    print(player.title()) 

copy_list = players[:] # копируем весь список
#copy_list = players[0:3] # сохраняем часть списка часть списка 
print(copy_list)

copy_list.append('lulu')
print(f"вывести список 1 {players}")
print(f"вывести список 2 {copy_list}")

##########################################################################
#    list = listcopy - так не работает!!! Нужно указать сигмент [:]          #
##########################################################################

dim = (200, 50) # создаем кортеж
print(dim[0]) # выводим элемент из кортежа
print(dim[1])
print(dim)

dims = (400, 100)
print("\nOrigin dim:")
for dimse in dims:
    print(dimse)

dims = (800, 200) # В кортеж можно задавать новые значения
print("\nModified dim")
for dimse in dims:
    print(dimse)