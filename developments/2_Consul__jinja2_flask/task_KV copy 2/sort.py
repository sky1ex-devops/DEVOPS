import consul
import re

c = consul.Consul(host='127.0.0.1', port=8500)

index, data = c.kv.get(key='', recurse=True)

print(data)

print(f"\n")

ky = []
for ky in data:
    print(ky.get("Key"))
    separator, _ = ky.split('/', 1)
print(separator)
print("\n")

print(ky)




text = "foo/bar/pizza"
  # Вывод: foo





# print("Введите key1, key2, key3: ")

# mess = 'key1'
# if mess in keys:
#    print(f"Найдено совпадение {mess}")
# else:
#    print("Совпадений нет")

