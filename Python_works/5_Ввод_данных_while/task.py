
# task: pizza

#pizza = []
#topping = ['оливки', 'курица', 'двойной сыр', 'грибы']
mess = "Введите какой топпинг добавить "
while True:
    pizz = input(mess)
    
    if pizz == 'q':
        break
    else:
        print(f"Вы добавили {pizz}")

