[Назад](Конспект_Python.md)
# Списки
#### Добавление, изменение, удаление и вывод количиство элементов списка.
* [append()](./1_append_del_pop_remove_insert.py) -  Добавление элемента в конец списка 
* [insert()](./1_append_del_pop_remove_insert.py) -  Добавление элемента в указанную ячейку списка 
* [pop()](./1_append_del_pop_remove_insert.py) -  Удалить последнее значение из списка
* [pop(0)](./1_append_del_pop_remove_insert.py) -  Добавление элемента в начале списка 
* [.remove() ](./1_append_del_pop_remove_insert.py) -  Удаление затем использование значения с помощью 
    >##### _Метод remove удаляет первое совпадение, если есть повторения, необходимо использовать цикл._

#### Сортировка 
* [sort()](./3_sort_sorted_len.py)  -  Сортировка по алфавиту
* [sort(reverse=True)](./3_sort_sorted_len.py)  -   Сортировка по алфавиту в обратном порядке 
* [sorted(cars, reverse=True)](./3_sort_sorted_len.py)  -   Сортировка по алфавиту в обратном порядке временно
* [reverse()](./3_sort_sorted_len.py)  -  Переход к обратному порядку списка 
* [len(cars)](./3_sort_sorted_len.py) -  Показывает количество элементов в списке
# Цикл for
* [for magic in magics:](./5_for.py) -  Берем поочередно значение из magics и сохраняем в переменной magic
#### Числовые списки
* [value in range(0,6)](./7_nambers.py) -  с помощью range выведем числа от 0 до 5
* [list(range(1,6))](./7_nambers.py) -  создаем список чисел
* [Игры с последовательностью чисел](./5_for.py) 
* [print(min(digits))](./7_nambers.py) -  вывести минимально число из списка
* [print(max(digits))](./7_nambers.py) -  вывести максимальное число
* [print(sum(digits))](./7_nambers.py) -  вывести сумму чисел
#### Генератор списка
* [squares = [value**2 for value in range(1,11)]](./7_nambers.py) -  генерация список от 1 до 10, значения возведены в степень 2ки.
#### Сегменты списка
* [print(players[0:3])](./9_sigment_list.py) - вывести часть списка, 1-3 значение
* [print(players[-3:])](./9_sigment_list.py) - отобразим последние 3 значения из списка
* [for player in players[0:3]: ](./9_sigment_list.py) -  обработать сегмент списка в цикле
#### Копирование списка

* [copy_list = players[:] ](./9_sigment_list.py) -  Копируем список
    >##### list = listcopy -  не работает!!! Нужно указать сегмент [:]   
* [copy_list = players[:3] ](./9_sigment_list.py) -  Копируем список в указанном диапазоне (первые 3 значения)

# Кортежи - неизменяемый список 
* [dim = (200, 50)](./9_sigment_list.py) -  создаем кортеж
    >##### В кортеж можна задать новые значения
```Python
dims = (400, 100)
print("\nOrigin dim:")
for dimse in dims:
    print(dimse)

dims = (800, 200) # новые значения
print("\nModified dim")
for dimse in dims:
    print(dimse)

```
[Назад](Конспект_Python.md)