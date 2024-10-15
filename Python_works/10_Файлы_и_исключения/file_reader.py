# file_path = '/home/lex/file/pi_digits.txt' # можно передать абсолютный путь к файлу
# with open(file_path) as file_object: #
with open('pi_digits.txt') as file_object:# open() - открываем наш фаил,
                                        # with - закроет фаил когда надобность пропадет
    contents = file_object.read()  # read - забираем содержимое файла и сохраняем в строке
print(contents.rstrip())           # rstrip - удалит пустую строку в конце вывода

#######################################################################
print("\n")
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#######################################################################
# Сохраняем содержимое файлы в список
print("\n")
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() # readlines() - каждую строку файла сохранит в список
                                    # список сохраняем в переменную line
for line in lines:
    print(line.rstrip())

#######################################################################
# Работа с содержимим файла

print("\nРабота с содержимим файла")
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() # readlines() - каждую строку файла сохранит в список
                                    # список сохраняем в переменную line
pi_string = ''                 # создаем переменную для хранения цифр 
for line in lines:             # записываем каждую серию цифр в pi_string 
    pi_string += line.strip() # и удаляем пропуски

print(pi_string)  
print(len(pi_string)) # Выводим количество символов

#---------------------------------------------------------------------#
#   Весть текст в файле - это строки. Если нужно работать с числами   #
#    необходимо приобразование методом int() или float()              #
#---------------------------------------------------------------------#

#######################################################################
# Большие файлы: миллион цифр
filename = 'pi_million_digits.txt'
print("\nМиллион знаков")
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[0:52]}...") # выводим первые 52 знака
print(len(pi_string)) # Выводим количество символов


#######################################################################
# replace() - замена слова в строке другим словом
print("\n")
filename = 'pi_replace.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
worlds = ''
for line in lines:
    worlds += line.strip()
    world_rep = worlds.replace('C', 'Python')

print(f"\nДоступные языки програмирования {worlds}")
print(f"\nВаш выбор {world_rep} ?")


#######################################################################
# Сопоставляем ДР числу ПИ
print("\nДР и число ПИ")
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Введите дату рождения (mmddyy):")
if birthday in pi_string:
    print("Дата вашего Дня Рождения входит в первые миллион цифр числа ПИ.")
else:
    print("Дата вашего Дня Рождения НЕ входит в первые миллион цифр числа ПИ.")



