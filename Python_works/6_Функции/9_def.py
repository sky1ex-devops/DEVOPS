#############################################################################################
# ФУНКЦИИ
# Передача, изменения и запрет изменений списка

def greet_users(names): # Создаем функцию greet_users с аргументом names
    """Вывод простого приветствия для каждого пользователя в системе"""
    for name in names: # поочередно забираем значения из names и записываем в name
        msg = f"Привет, {name.title()}!" # Создаем переменную с выводом текста и аргумента функции
        print(msg) # выводим на экран

username = ['Жорик', 'Жора', 'Жор'] # задаем значения для списка
greet_users(username)


# изменения списка 
print("\n")
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] # создаем список деталей которые необходимо напечатать
completed_models = [] # создаем пустой список для готовых деталей 

while unprinted_designs: # создаем цикл который будет выполняться пока в unprinted_designs емеются значения
    current_design = unprinted_designs.pop() # Забираем элементы с конца  и записываем в  current_design
    print(f"Printing model: {current_design}") # Выводим модели которые будут печататься 
    completed_models.append(current_design) # Добовляем элементы в список completed_models

print("\nThe following models have been printed: ")
for completed_model in completed_models:    #  поочередно выводим список готовых деталей
    print(completed_model)

print("\n")
#  для запрета изменения
# необходимо передать копию списка вместо оригинала
# Имя_функции(имя_списка[:])
# [:] - создаст копию списка для передачи функции.

###################################################################################################
# Создаем функцию (Что мы делаем?) 

def functions(msgs): # Задаем функции аргумент msgs
    for msg in msgs: # поочередно обрабатываем значения из msgs и записываем в msg
        print(f"{msg}") # и выводим значенина на экран 

# Задаем обькеты для функции (С чем мы делаем?)

show_messages = ['Элемент1', 'Элемент2', 'Элемент3'] # создаем список 
functions(show_messages) # запускаем функцию


###################################################################################################
print("\n")
sent_messages = []

def send_messages(messages):
    """копируем спиок и выводим процес на экран"""
    for message in messages:
        print(f" Копируем элемент: {message}")
        sent_messages.append(message)

one_list = ['Элемент1', 'Элемент2', 'Элемент3']
send_messages(one_list)
print(f"Выводим скопированные элементы: {sent_messages}")
print(f"Сравниваем с исходным списком: {one_list}")

if sent_messages == one_list:
    print("Копирование прошло успешно!") 



