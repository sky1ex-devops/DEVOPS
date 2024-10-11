import keyboard # копируем модуль keyboard
import os # копируем модуль os
import time


# Функция, вызываемая при нажатии клавиши
def on_press(key): # Создаем функцию on_press с параметром key
    
#    print(f"Нажата клавиша {key.name}") # Текст - проверка нажатия
    led_on = 'xset led 3' # записываем необходимую команду в переменную
    led_off = 'xset -led 3'
    os.system (led_on) # выполняем внешнюю команду на включение led
    time.sleep(3) # Задержка 3 сек
    os.system (led_off) # выполняем внешнюю команду на выключение led


keyboard.on_press(on_press) # вызываем функцию 
             
#keyboard.on_release(on_release) # вызываем функцию 
keyboard.wait()# вызываем функцию - блокирует программу
               #до тех пор, пока не будет нажата клавиша.
