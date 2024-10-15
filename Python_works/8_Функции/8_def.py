#############################################################################################
# ФУНКЦИИ
# Использование функции в цикле while

def get_formatted_name(first_name, last_name): # Параметры заданы по умолчанию и являются пустыми
    """Возвращает аккуратно отформатированное полное имя.""" 
    full_name = f"{first_name} {last_name} " # записываем в строку
    return full_name.title() # возвращаем значение в get_formatted_name
# бесконечный цикл
while True: 
    print("\nКак к вам обращаться? ") 
    print("для ввыхода введите 'q' ")
    f_name = input("Имя: ") # Ожидаем ввода Имени
    if f_name == 'q':
        break
    l_name = input("Фамилия:") # Ожидаем ввода Фамилии
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nПривет, {formatted_name}")