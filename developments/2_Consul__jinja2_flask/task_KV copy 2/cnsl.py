import consul

c = consul.Consul(host='127.0.0.1', port=8500)

index, data = c.kv.get(key='', recurse=True)

print(data)

print("\n")


for d in data:
    print(d.get("Key"), d.get("Value"))

print("\n")

ddata = []
for d in data:
   ddata = (d.get("Key"), d.get("Value"))
print(data)

print("\n")

#-----ОТБИРАЕМ ЗНАЧЕНИЯ ИЗ CONSUL-----#
keys = []
for edata in data:
    data = edata.get('Key', None)
    keys.append(data)

#-----СОРТИРУЕМ КЛЮЧИ, ОТБИРАЕМ КАТАЛОГИ-----#

# оставляем элементы где присутстует /
stringVal = "/"
no_key = [ x for x in keys if stringVal in x ] 

# удалить все после символа /
no_slash = [x.replace(" ", "").split("/")[0] for x in no_key] 

# Удаляем повторяющиеся значения
kt = list(set(no_slash))
ktl = sorted(kt)
print(ktl)


# print("Введите key1, key2, key3: ")

# mess = 'key1'
# if mess in keys:
#    print(f"Найдено совпадение {mess}")
# else:
#    print("Совпадений нет")

