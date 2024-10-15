#######################################################################
# ИСКЛЮЧЕНИЯ try-except

try:
    print(5/0)
except ZeroDivisionError: # Указываем как необхдимо действовать в случае ошибки
                          # случае ошибки ZeroDivisionError
    print("На 0 делить нальзя")
#######################################################################
# Пример с Предотвращение аварийного завершения программы

print("Введите числа для деления")
print("Нажмите 'q' для выхода")

while True:
    first_number = input("\n Первое чилсо: ")
    if first_number == 'q':
        break
    second_number = input("Второе число:  ")
    if second_number == 'q': 
        break
    try: # Выполняем код в блоке try
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: # Если код заканчивается ошибкой, выводим текст:
        print("На НОЛЬ не делиться!")
    else: # Если без ошибко:
        print(answer) # - вы полнем этот код 

#######################################################################
#  исключение FileNotFoundError

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Извините, файл {filename} не нйден")    

#######################################################################
#  анализ Текста, подсчет слов


filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Извините, файл {filename} не нйден")    
else:
    # Подсчет приблизительного количества строк в файле.
    words = contents.split()
    num_worlds = len(words)
    print(f"В файле {filename} - {num_worlds} слов")



#######################################################################
#  анализ Текста, подсчет строк

def count_words(filename):
    """Подсчет приблизительного количества слов в файле."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Извините, файл {filename} не нйден")    
    else:
        # Подсчет приблизительного количества строк в файле.
        words = contents.split() ## метод подсчета слов
        num_worlds = len(words)
        print(f"В файле {filename} - {num_worlds} слов")

filenames = ['alice.txt', 'ring.txt', 'none.txt']
for filename in filenames:
    count_words(filename)


#######################################################################
#  Ошибка без уведомления
print("\n")
def count_words(filename):
    """Подсчет приблизительного количества слов в файле."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass   # НЕ выводим ошибку
    else:
        # Подсчет приблизительного количества строк в файле.
        words = contents.split() ## метод подсчета слов
        num_worlds = len(words)
        print(f"В файле {filename} - {num_worlds} слов")

filenames = ['alice.txt', 'ring.txt', 'none.txt']
for filename in filenames:
    count_words(filename)
