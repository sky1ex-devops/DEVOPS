#####################################################################################################################
# if

req_topping = 'mushroom'
                                # != не равно
if req_topping != 'anchovies': # Если переменная не равна 'anchovies'...
    print("Hold the anchovies!") # выводим сообщение

age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 == 18) # Проверяем совпадения одной и второй переменной
                                   # true - оба условия совпали

print(age_0 >= 23 or age_1 == 19)  # Проверяем совпадения одной и второй переменной
                                   # true - одно или оба уловий совпали

reqlists = ['mushrooms', 'onions', 'pineapple']
print(f"\n{'mushrooms' in reqlists}") # true - если значение входит в список
print("\n")

#####################################################################################################################
# if_else


age = 17
if age >= 18:
    print("Вы емеете право учавтсвовать в выборах")
else:
    print("Вы не имеете право учавствовать в выборах")

cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars: 
    if car == 'bmw': # Проверка, содержит ли переменная значение 'bmw'
        print(car.upper()) # если да - выводим все симвлы Заглавными
    else:
        print(car.title()) # иначе - выводим только первый символ заглавный
print("\n")

#####################################################################################################################
# if_elif_else
# для выявления одного совпадения

agee = 49

if agee < 4:
    print("Сумма к оплате 0р.")
elif agee < 18:
    print("Сумма к оплате 25р.")
elif agee > 50:
    print("Сумма к оплате 25р.")
else:
    print("Сумма к оплате 50р.")

#####################################################################################################################
# if
# для выявления нескольких совпадений

print("\n")
r_topp = ['mushrooms', 'extra', 'cheese']

if 'mushrooms' in r_topp:
    print("Adding mushrooms")

if 'papperoni' in r_topp:
    print("Adding papperoni")
    
if 'cheese' in r_topp:
    print("Adding cheese")

#####################################################################################################################
# for and if and lists
print("\n") 
requested_toppings = ['mushrooms', 'green peppers', 'extra chees']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#####################################################################################################################

print("\n")
requested_toppings = [] # Пустой список
if requested_toppings: # Если ..
    for requested_topping in requested_toppings:
        print(f"Добавлен {requested_topping}.") # Имеется значение в переменной
    print("\nВаши пожелания исполнены!") # выводим сообщение
else: # если нет значения
    print("\nИнградиенты закончились") # выводим это сообщение

#####################################################################################################################
# Множественные списки

print("\n")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'papperoni', 'extra cheese', 'pineapple'] # Список возможных добавок
requested_toppings = ['mushrooms',  'papperoni', 'extra cheese', 'tee', 'coffe'] # Добавки которые заазал клиент

for requested_topping in requested_toppings: 
    if requested_topping in available_toppings: # если значиения из requested_topping имеються в available_toppings, то ..
        print(f"Adding {requested_topping}.") # выводим заказаные добавки
    else:                                     # если условия выше не совпали...
        print(f"Sorry, we don`t have {requested_topping}.") #Показываем какого инградиента не хватает
print("\nFinished making your pizza")

#####################################################################################################################
print("\n")
who = 'usr' # ввод пользователя 
users = ['usr',  'Admin', 'lui', 'jora', 'Djon_Doe'] # имеющийся пользователи

if "admin" in who:                                   # если ввели admin 
    print(f"Привет {who}.")                          # выводим привет admin
elif who in users:                                   # если ввели пользователя из списка имеющихся
    print(f"Привет {who}")                           # выводим привет по имени
else:                                                # если ввели не из имеющихся и не admin
    who != users and who != 'Admin'                  # ввыводим сообщение ....
    print("Спасибо что посетили наш сайт")

#####################################################################################################################
print("\n")
new_users = ['Djin',  'Admin', 'lui', 'Petr', 'Gosha'] # новые обтекты 
current_users = ['usr',  'Admin', 'lui', 'jora', 'Djon_Doe'] # имеющейся база

for new_user in new_users: # заставляем применять нижесказанное к каждому элементу в списке new_users
    if new_user in current_users: # если новый обьект имееться в базе (current_users)
        print(f"\nПользователь '{new_user}' уже существует в базе, придумайте другой Ник") # выводим сообщение 
    else: # если
        new_user != current_users # нет совпадения нового обьекта с базой
        print(f"\nПользователь {new_user} создан!") # выводим сообщение

#####################################################################################################################
print("\n")
nmbrs = list(range(1,10))
for nmbr in nmbrs:
    if nmbr >= 4: 
        print(f"{nmbr}th")
    elif nmbr == 3:
        print(f"{nmbr}rd")
    elif nmbr == 2:
        print(f"{nmbr}nd")
    elif nmbr == 1:
        print(f"{nmbr}st")
