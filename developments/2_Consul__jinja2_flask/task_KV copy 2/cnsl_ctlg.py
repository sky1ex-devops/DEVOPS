import consul
import os 

import pathlib
from pathlib import Path

c = consul.Consul(host='127.0.0.1', port=8500)

index, data = c.kv.get(key='', recurse=True)

print("\n")
keys = []
    
for edata in data:
    data = edata.get('Key', None)
    keys.append(data)
    
print(keys)
print("\n")


print("\n")
vle = ["folder2/key2"]
for p in vle:
    print(p)
    p = str(vle)
    print(p)
    path = Path(p)
print(path.parents[-2])
print("\n")


print("\n")
for value in keys:
    path = Path("folder1/key1/Value1")
    print(path.parents[-2])      

print("\n")


print("\n")
path = Path("folder1/and/key1/")
print(path.parents[-2])
path = Path("key2/Value2")
print(path.parents[-2])
path = Path("folder3/ ") # без пробела ошибка IndexError -2
print(path.parents[-2])
path = Path("keys/ ") # keys привидет к ошибке IndexError -2
print(path.parents[-2])
print("\n")


print("\n####################################################################################################################################")



vles = keys
print(f"Структура дериктории: {vles}")
print("\n")

print("В текущем дериктории имеются: \n")
d_folder = [] # список для не отсартированых каталогов
dir_folder = [] # список для отсартированых каталогов
dir_key = [] # список для ключей
for p in vles: # перебираем элементы списка
    if '/' in p:                        # Если присутствует / 
        folder, key = p.split('/', 1)   # Отделяем строку на до и после /
        d_folder.append(folder)         # Записываем то что до в список 
        
    else:                               # Если / НЕТ 
        dir_key.append(p)               # значит это ключ, записываем в список ключей

dir_folder = list(set(d_folder)) # Удаляем поворяющиеся значения
print(f"Каталоги: {sorted(dir_folder)}") # Выводим и сортируем
print(f"Ключи: {dir_key}") 
print("\n")
