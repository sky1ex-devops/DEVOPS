#######################################################################
# ФУНКЦИИ
# Произвольный набор именованных аргументов

#---------------------------------------------------------------------#
#   Можно передать функции столько пар ключ-значение, сколько         №
#   указанно в команде вызова                                         #
#---------------------------------------------------------------------#

def build_profile(first, last, **user_info): # ожидаем ввода имени, фамилии
                                             # ** создает пустой словарь
    """Строит словарь с ифно о пользователе."""# с именем user_info
    user_info['first_name'] = first # функция подставит значение(имя) к
                                    # ключу first_name и запишет в словарь
    user_info['last_name'] = last   # функция подставит значение(фамилия) к
                                    # ключу first_name и запишет в словарь
    return user_info                # возвращаем значения функции
    
user_profile = build_profile(
                            'albert', 'einstein',   # first and last
                             location= 'princeton', # пара для словаря
                             field='physics'        # пара для словаря
                            )
print(user_profile) 

#######################################################################

def make_car(whos, modeles, **conf):
    """Получение инфо об авто]"""
    conf['mark'] = whos
    conf['model'] =  modeles
    return conf

car = make_car(
                'toyota', 'prius',
                color= 'white',
                tow_package=True
              )
print(car)


