outs = []
for out in range(1,21):
    print(out)

#mlns = range(1,1000001)
#for mln in mlns:
#    print(mln)
#print(f"\nМинимальное значение: {min(mlns)}")
#print(f"\nМаксимальное значение: {max(mlns)}")
#print(f"\nСумируем значения: {sum(mlns)}")

nevent_numbers = []
for num in range(1,21,2):
    nevent_numbers.append(num)
print(f"Выводим нечетные числа {nevent_numbers}")

three = []
for numb in range(3,30,3):
    three.append(numb)
print(f"Выводим числа кратные 3м{three}")

cubs = []
for cub in range(1,11):
    cubs.append(cub**3)
print(f"Числа от 1 до 10 в кубе{cubs}")

gen_list = [value**3 for value in range(1,11)]
print(f"генерируем список чесел в кубе {gen_list}")

