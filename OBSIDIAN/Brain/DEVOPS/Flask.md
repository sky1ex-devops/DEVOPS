#Flask - этот микро-фреймворк, для языка Python

Преимущества:
- **Минимальный набор инструментов из коробки.** Причём они не навязывают какую-то архитектуру или жёсткую структуру проектов. Разработчики сами решают, как и что они будут создавать.
- **Гибкость.** Работая с Flask, программист может выбирать только необходимые встроенные инструменты и подключать дополнительные внешние, не перегружая проект лишними модулями.
- **Расширяемость.** У Flask много расширений и плагинов, которые помогают быстро добавить новую функциональность. Например, авторизацию, управление базами данных и работу с формами.
- **Простота.** У Flask простой синтаксис, что делает изучение этого фреймворка более простым, а также позволяет быстрее создавать прототипы веб-приложений.
- **Поддержка сообщества.** Flask запустили в 2010 году, и почти по любому связанному с ним вопросу в интернете уже есть ответы.
### Установка Flask

```bash
pip install Flask
pip install Flask==<version>
pip show flask # проверить, работает ли Flask

```

### **Простой сайт на Flask**
```python
# импортируем класс Flask из библиотеки Flask
from flask import Flask 
# создадим экземпляр класса Flask:
app = Flask(__name__)
# передаем аргумент __name__ конструктору класса, этот аргумент скажет Flask, где находится наше приложение. Так Flask сможет определить местоположение шаблонов и статических файлов, о которых речь пойдёт дальше.

```
Весь бэкенд строится на маршрутах — или URL-адресах. Они помогают задавать удобную структуру и понятное поведение веб-приложениям.
Для пользователя маршруты — это отдельные «вкладки» на сайте.

Создаем первый маршрут:

```python
@app.route('/')
def hello_world():
    return 'Hello, World!'
```
Маршрут задаётся в строке @app.route('/'). Внутрь круглых скобок

Запускаем приложение:
```python
if __name__ == '__main__':
    app.run()
```
Этот код гарантирует, что сервер Flask будет запущен только в том случае, если файл app.py был запущен напрямую, а не импортирован как модуль.

Весь код:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

if __name__ == '__main__':
   app.run()
```
Сохраняем файл app.py и запускаем его с помощью команды в консоли:
```
python app.py
```

После запуска, должны увидеть сообщение о том, что сервер Flask был запущен:
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Проверяем приложения:
![[Pasted image 20241017163525.png]]

### **Cоздаём блог на Flask**

**Создаём HTML-шаблон**
#HTML-шаблоны — это файлы, которые задают структуру и содержимое страниц сайта. Шаблоны упрощают жизнь программистам — им не приходится десятки раз писать один и тот же #HTML -код, ведь его можно просто взять и… шаблонизировать.
Создадим файл: base.html
```html
<!DOCTYPE html>
<html>
  <head><!--Заголовок-->
    <title>{% block title %}{% endblock %}</title>
  </head>
  <body> <!--Тело страницы-->
    {% block content %}{% endblock %} 
  </body>
</html>
```

Теги {% block %} и {% endblock %}  нужны, чтобы динамически добавлять туда новые элементы: другие HTML-блоки, JavaScript-код и тому подобное.

Cоздаём второй шаблон index.html который будет наследовать элементы базового шаблона:
```html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
  <h1>Welcome to my website!</h1>
  <p>This is the homepage.</p>
{% endblock %}
```
Этот шаблон переопределяет заголовок страницы и определяет контент, который будет отображаться на домашней странице: заголовок страницы Home и немного текста.

### **Используем HTML-шаблоны**

Создаём файл программы app.py и импортируем функцию render_template из библиотеки Flask, которая позволяет работать с шаблонами:
```python
from flask import Flask, render_template
```

Задаём маршрут главной страницы и используем в нём новую функцию, чтобы отобразить шаблон index.html:
```python
@app.route('/')
def index():
    return render_template('index.html')
```

Запускаем программу app.py
![[Pasted image 20241017165639.png]]




https://skillbox.ru/media/code/freymvork-flask-kak-on-rabotaet-i-zachem-nuzhen/


https://habr.com/ru/articles/783574/

https://proglib.io/p/rukovodstvo-dlya-nachinayushchih-po-shablonam-jinja-v-flask-2022-09-05

https://victor-komlev.ru/frejmvork-flask/

https://stackforgeeks.com/blog/navigating-in-flask-using-js


https://proprogrammer.ru/izuchenie/parsing-json-v-python-polnoe-rukovodstvo-dlya-nachinayushix


https://www.algotree.org/algorithms/dynamic_programming/longest_common_subsequence/


https://github.com/Algo-Phantoms/Algo-Tree/blob/main/Code/Python/left_rotation.py

https://mashagpt.ru/chat