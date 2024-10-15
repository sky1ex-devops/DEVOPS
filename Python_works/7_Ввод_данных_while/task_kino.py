# v2
pull = {}

active_pull = True

while active_pull:
    name = input("Ваше имя: ")
    age = input("Возрас: ")

    pull[name] = age

    maybe_off = input("Для завершения опроса введите (YES/no):")
    if maybe_off == 'no':
        active_pull = False

print("\n --- Опрос окончен ---")

for name, age in pull.items():
    age = int(age)
    if age < 3:
        print(f"{name} ваш билет бесплатный")
    elif age >=3 and age < 12:
        print(f"{name} ваш билет стоит 10Bit")
    else:
        print(f"{name} ваш билет стоит 15Bit")



