alien_0 = {'color': 'green', 'points': 5} # создаем словарь
print(alien_0['color']) # выводим значение ключа color из словаря 
new_points = alien_0['points']  # Создаем переменную равную значению ключа points
print(f"You just earned {new_points} points!") # Выводим текст значение переменной

alien_0['x_position'] = 0 # Задаем новый ключ и значение для словаря alien_0
alien_0['y_position'] = 25 # Задаем новый ключ и значение для словаря alien_0
print(alien_0)

###################################################################################

#    Отслеживания перемещения 

print("\n")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} # определяем исходную позицию
print(f"Текущая позиция: {alien_0['x_position']}")               # выводим текущую позицию на экран
# обьект смещается в право.
# вычесляем величину смещения на основании текущей скорости.
if alien_0['speed'] == 'slow':                                   # Обозначаем условия:
    x_increment = 1                                              # если скорость slow - смещение обьекта на 1 единицу
elif alien_0['speed'] == 'medium':                               # если скорость medium - смещение обьекта на 2 единицы
    x_increment = 2 
else:                                                            # если условия выше не совпали - обьект смещаеться на 3
    #Обьект двигается быстро.
    x_increment = 3

# Новая позиция равна сумме старой позиции и приращения.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"Новая позиция: {alien_0['x_position']}")


###################################################################################

#   Словарь с однотипными обьектами

print("\n")
# Пример: опрос о любимых языках програмирования
favorite_languages = {                          # Перечисляем обьекты
    'Джин': 'python',
    'Люк': 'c',
    'Луи': 'rudy',
    'Анриано': 'python',
    }

languge = favorite_languages['Люк'].title()    # Определяем обьект для вывода, указываем 
                                               # что имя должно быть с заглавной буквы

print(f"Люку нравится: {languge}")             # Выводим обьект


###################################################################################

# Словари в списке

print("\n")
# Создаем несколько словарей(несколько пришельцев)
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
# Записываем словари в список
aliens = [alien_0, alien_1, alien_2]  

for alien in aliens: # Вывод списка
    print(alien)

###################################################################################

# Список в словаре

print("\n")
# Наполнение информацией о заказанной пицце.
pizza = {
    'crust': 'толстом',
    'toppings': ['грибы', 'двойной сыр'],
    }
# Описание заказа.
print(f"Вы заказали пиццу на '{pizza['crust']}' тесте, "
    " с такими добавками:")

for topping in pizza['toppings']:
    print(topping)



print("\n")
# Пример: опрос о любимых языках програмирования
favorite_languages = {                          # Перечисляем обьекты
    'Джин': ['python', 'C'],
    'Люк': ['c'],
    'Луи': ['rudy', 'go'],
    'Анриано': ['python', 'js'],
    }

for name, languages in favorite_languages.items(): # Перебираем ключи и значения словаря favorite_languages
    print(f"{name.title()}, интересуется языками програмирования:") # выводим ключ и текст
    for language in languages:                 # перебираем значения словаря 
        print(f"{language.title()}")     # и выводим на экран
   
###################################################################################

# Словарь в словаре

print("\n")
users = {                           # Создаем словарь с именем user

    'jdoe': {                       # содержащий два ключа jdoe и aeinstein
        'first': 'John',            # значение словаря представляет собой словарь с данными
        'last': 'Doe',
        'location': 'lab'
    },

    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

}

for username, user_info in users.items(): # Перебираем словарь users, разбираем на ключ и значение
    print(f"Username:{username}")   # выводим название ключа
    full_name = f"{user_info['first']} {user_info['last']}" # создаем переменную которая будет хранить полное имя(имя+ фамилия)
    location = user_info['location'] # создаем переменную которая будет хранить location
    print(f"\tFull name: {full_name.title()}") # выводим полное имя и
    print(f"\tLocation: {location.title()}") # локацию


       
###################################################################################

# упражнение Люди

print("\n")
people_0 = {'name': 'John_doe', 'location': 'asia'}
people_1 = {'name': 'gosha', 'location': 'rus'}
people_2 = {'name': 'John_doe', 'location': 'eur'}

peoples = [people_0, people_1, people_2]

for people in peoples:
    print(people)