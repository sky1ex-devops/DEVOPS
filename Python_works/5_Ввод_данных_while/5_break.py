

#############################################################################################

# break и выход из цикла

#----------------------------------------------------------------------#
#    Прирывание програмы без оставшегося кода в цикле либо условий     #
#----------------------------------------------------------------------#


prompt = "\n Какой город ты недавно посещал?   "       #  опрееляем сообщение для пользователя
prompt += "\n Либо введите 'quit' для выхода: "

while True:                                            # создаем цикл с флагом True
    city = input(prompt)                               # Ожидаем ввода и записсываем его в city

    if city == 'quit':                                 # Если ввод 'quit'
        break                                          # Цикл останавливается
    else:                                              # Иначе выводим сообщение
        print(f"Я бы с радостью поехал в город {city.title()}")

