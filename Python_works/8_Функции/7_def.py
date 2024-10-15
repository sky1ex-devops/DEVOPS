#############################################################################################
# ФУНКЦИИ
# Возвращение словаря

def build_person(first_name, last_name): # значения по умолчанию
    """Возвращает словарь с информцией о человеке"""
    person = {'first': first_name, 'last': last_name} # полученное значение сохраняем в словаре
    return person # возвращаем весь словарь

musician = build_person('jimi', 'hendrix')
print(musician)