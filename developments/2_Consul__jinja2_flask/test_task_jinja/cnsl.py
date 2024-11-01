import consul

c = consul.Consul(host='127.0.0.1', port=8500)

index, data = c.kv.get(key='', recurse=True)

print(data)

print("\n")

for d in data:
    print(d.get("Key"), d.get("Value"))




print("\n")

keys = []
for edata in data:
    data = edata.get('Key', None)
    keys.append(data)

print(f"\n{keys}")





# print("Введите key1, key2, key3: ")

# mess = 'key1'
# if mess in keys:
#    print(f"Найдено совпадение {mess}")
# else:
#    print("Совпадений нет")

