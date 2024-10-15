from format_name import get_formatted_name

print("Введите 'q' для выхода")
while True:
    first = input("\n Введите Имя: ")
    if first == 'q':
        break
    last = input("Введите Фамилию: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\t Отформатированное имя: {formatted_name}")