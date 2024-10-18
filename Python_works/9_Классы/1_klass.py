# Классы используется для описывания существующих предметов и ситуаций  для  обьектов на основе этих ситуаций
# Другими словами мы определяем общее поведение для целой категории обьектов

class Pin(): # определяем класс с именем Dog
    """Простая модель собаки"""

    def __init__(self, name, age):  
        """Инициализирует атрибут name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Пингвин садится по команде."""
        print(f"{self.name} садится")

    def roll_over(self):
        """Пингвин перекатывается по команде"""
        print(f"{self.name} Катится!") 
    
my_pin = Pin('Пепе', 6)
your_pin = Pin('Лоло', 4)

print(f"Моего пингвина зовут {my_pin.name}")
print(f"возраст {my_pin.age} лет")
my_pin.sit()
my_pin.roll_over()

print(f"Моего пингвина зовут {your_pin.name}")
print(f"возраст  {your_pin.age} лет")
my_pin.sit()