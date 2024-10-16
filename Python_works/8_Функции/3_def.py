#############################################################################################
# ФУНКЦИИ
#### Позиционные Аргументы 

def desctible_pet(animal_type, pet_name):
    """Выводит информацию о животных"""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

desctible_pet('hamster', 'frodo')
desctible_pet('Dog', 'bax')