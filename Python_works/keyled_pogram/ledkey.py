import keyboard # копируем модуль keyboard
import os # копируем модуль os
import time


# Функция, вызываемая при нажатии клавиши
def on_press(key): # Создаем функцию on_press с параметром key
    
    #print(f"Нажата клавиша {key.name}") # Текст - проверка нажатия
    led_on = 'xset led 3' # записываем необходимую команду в переменную
    os.system (led_on) # выполняем внешнюю команду на включение led
    time.sleep(1) # таймер. ждет 1с после каждого нажатия
    led_off = 'xset -led 3'
    os.system (led_off) # выполняем внешнюю команду на выключение led

    
keyboard.on_press(on_press)
keyboard.wait()    # вызываем функцию - блокирует программу
                   #до тех пор, пока не будет нажата клавиша.