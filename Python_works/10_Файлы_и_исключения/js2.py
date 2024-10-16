#######################################################################
#  Функции json.dump() и json.load()
## Используется для сохранения и выгрузки из файла .json

import json

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
    
def get_new_username():
    """Запрашивает новое имя пользователя"""
    username = input(" Имя: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Приветствует пользователя по имени"""
    username = get_stored_username()
    if username:
        print(f"Приветствую, {username}")
    else:
        username = get_new_username()
        print(f"Имя {username} записанно в файл")
greet_user()

