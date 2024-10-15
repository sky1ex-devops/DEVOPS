#######################################################################
#  Функции json.dump() и json.load()
## Используется для сохранения и выгрузки из файла .json

import json



filename = 'numbers.json' # назначем фмя файла
with open(filename) as f: # открываем файл в режиме записи
    numbers = json.load(f) # используем функцию json.load
                          # для выгрузки списка из json

print(numbers)


#######################################################################

numbers = [2,3,5,6,11,13] #создаем список чисел

filename = 'numbers.json' # назначем фмя файла
with open(filename, 'w') as f: # открываем файл в режиме записи
    json.dump(numbers, f) # используем функцию json.dump 
                          # для сохранения списка в json

print(numbers)
#######################################################################
# Сохранение и чтение данных, сгенериованных пользователем

username = input("Имя: ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"Имя {username} успешно сохранено в json файл")


filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
    print(f"Приветствую {username} !")

#######################################################################

# Программа загружает имя пользователя, если оно было сохранено оанее.
# В противном случае она записывает имя пользователя и сохраняет его.

print("\n")
filename = 'username.json'

try:
    with open(filename) as f:
        username =json.load(f)
except FileNotFoundError:
    username = input(" Имя :")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"Имя {username} успешно сохранено в json файл")
else:
    print(f"Добро пожаловать, {username}!")

#######################################################################

# Рефакторинг - запаковываем код в функцию

print("\n")

def get_stored_username():
    """Приветствует пользователя по имени"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username =json.load(f)
    except FileNotFoundError:
        return None 
    else:
        return username

def greet_user():
    """Приветствует пользователя по имени"""
    username = get_stored_username()
    if username:
        print(f"Приветствую, {username}")
    else:
        username = input("Имя: ")
        filename = 'username.json'
        with open(filename, w) as f:
            json.dump(username, f)
            print(f"Имя {username} записанно в файл")
greet_user()

