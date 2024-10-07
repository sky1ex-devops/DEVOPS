
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


# if_elif_else


agee = 49

if agee < 4:
    print("Сумма к оплате 0р.")
elif agee < 18:
    print("Сумма к оплате 25р.")
elif agee > 50:
    print("Сумма к оплате 25р.")
else:
    print("Сумма к оплате 50р.")

print("\n")
r_topp = ['mushrooms', 'extra', 'cheese']

if 'mushrooms' in r_topp:
    print("Adding mushrooms")

if 'papperoni' in r_topp:
    print("Adding papperoni")
    
if 'cheese' in r_topp:
    print("Adding cheese")


print("\n")
alien_color = ['green', 'yellow', 'red']
if 'white' in alien_color:
    print("Вы выбрали green - заработали 5 очков")