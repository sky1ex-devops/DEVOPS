#######################################################################
# ФУНКЦИИ
# Передача произвольного набора аргуентов

#---------------------------------------------------------------------#
#    Если не знаем заранее, сколько аргументов передаем функции       #
#    Можем получить произвольное количество аргументов                #
#---------------------------------------------------------------------#

def make_pizza(*toppings): # *создает пустой кортеж и упаковывает в 
    """Вывод списка заказанных товаров.""" # него полученные знач.
    for topping in toppings:
        print(f" - {topping}")

make_pizza('pepperoni')
make_pizza('green peppers', 'extra cheese')
