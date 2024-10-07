for value in range(1,5): # с помощью range выведем числа от 1 до 4 
    print(value)

print("\n ")

for value in range(0,6): # с помощью range выведем числа от 0 до 5
    print(value)

numb = list(range(1,6)) # создаем список чисел
print(numb)

even_num = list(range(2,11,2)) # генерируем последовательность с 2х 
print(even_num) # увеличивая значение на 2 до конечного значения 11 

squs = [] # создаем пустой список
for value in range(1,11): # Перебираем все значения от 1 до 10
    squ = value**2 # Возводим во вторую степень
    squs.append(squ) # Каждое новое значение присоединяем к списку squs
print(squs)

squares = []
for value in range(1,11): # ^
    squares.append(value**2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # вывести минимально число из списка
print(max(digits)) # вывести максимальное число
print(sum(digits)) # вывести сумму чисел

squares = [value**2 for value in range(1,11)]# сoздаем переменную squares, которая равна
print(squares) # переменной value возведенной в степень и цикл который запишет 
# последовательность чисел в переменную value.