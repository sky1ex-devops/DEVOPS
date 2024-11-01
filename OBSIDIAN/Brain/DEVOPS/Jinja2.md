#Jinja2 - Python-библиотека для рендеринга шаблонов.
Позиционирует себя как инструмент для дизайнеров и верстальщиков, упрощающий вёрстку и отделяющий её от разработки, и пытающийся по мере возможностей изолировать не-разработчиков от Python.

### Как работает?

Jinja2 компилирует каждый шаблон в #python_executable, который
на вход принимает контекст и возвращает строку - отрендеренный шаблон.

Процесс работы:
1. **Загрузка**. Вы можете хранить шаблоны в файловой системе, в папке с вашим Python-пакетом, в памяти или просто генерировать на лету — в первую очередь Jinja2 определяет, какой из способов актуален, и загружает исходники шаблона в память.
2. **Токенизация**. Лексический анализатор (lexer) бьёт исходный текст шаблона на простейшие сущности — токены. Пример токена — открывающая теги конструкция `{%`
3. **Парсинг**. Синтаксический анализатор (parser) разбирает поток токенов, вычленяя синтаксические конструкции. Пример синтаксической конструкции — подставляющая значение переменной конструкция `{{ variable }}` (она состоит из трёх токенов — открывающего `{{`, имени `variable` и закрывающего `}}`).
4. **Оптимизация**. На этом этапе вычисляются все константные выражения. Например, конструкция `{{ 1 + 2 }}` будет превращена в `{{ 3 }}`.
5. **Генерация**. Синтаксические конструкции, до сих пор хранившиеся в виде абстрактного синтаксического дерева (AST), конвертируются в код на Python.
6. **Компиляция**. Полученный Python-код компилируется встроенной функций `compile`. Получившийся объект можно запускать встроенной фукнцией `exec`, что шаблоны и делают при рендеринге.

Можно использовать Jinja без #веб-фреймворка работающего в 
фоновом режиме.

### Установка Jinja

Создаем и активируем виртуальную среду
```python
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $
```

Устанавливаем jinja
```python
python -m pip install Jinja2
```

###  Рендеринг первого шаблона

Создаем среду jinja без аргументов. Затем создаем свою среду в которую загружаем строку Hello, {{ name }}! как шаблон.

```python
>>> import jinja2
>>> environment = jinja2.Environment()
>>> template = environment.from_string("Hello, {{ name }}!")
>>> template.render(name="World")
'Hello, World!'
```

По фату этим кодом, выполнили 2 шага:
1. Загрузка шаблона - загружаем источник, содержащий переменные-заполнители. По умолчанию они заключаются в пару фигурных скобок (`{{ }}`).

2. Визуализация шаблона - помещаем содержимое в плейсхолдер. Вы можете передать словарь или аргументы ключевого слова как содержимое. Заполнив плейсхолдер, на выходе вы получаете _Hello, World!_.

Можно использовать внешние файлы в качестве шаблонов.

Файл шаблона:
```
{# templates/message.txt #}

Hello {{ name }}!

I'm happy to inform you that you did very well on today's {{ test_name }}.
You reached {{ score }} out of {{ max_score }} points.

See you tomorrow!
Anke
```
Шаблон message.txt содержит черновик сообщений, который можно скопировать и вставить для отправки позже.

Файл программы:
```python
# write_messages.py

from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
]

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("message.txt")

for student in students:
    filename = f"message_{student['name'].lower()}.txt"
    content = template.render(
        student,
        max_score=max_score,
        test_name=test_name
    )
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")
```

Когда мы создаем среду Jinja с помощью `FileSystemLoader`, можете передать путь к папке с  шаблонами.
Вместо того, чтобы передавать строку, теперь загружаем `message.txt` как свой шаблон.

Ключи словаря `students`, наряду с `max_score` и `test_name`, соответствуют переменным шаблона в `message.txt`. 
Если не передавать контекст для переменных в шаблон,
ошибки не будет.

Переменные шаблона message.txt получили данные.
И при выполнении программы было создано 
3 заполненных файла:
message_gergeley.txt
message_sandrine.txt
message_frieda.txt

### Используйте Jinja с Flask

#Flask - этот микро-фреймворк, для языка Python



https://habr.com/ru/articles/340254/

https://proglib.io/p/rukovodstvo-dlya-nachinayushchih-po-shablonam-jinja-v-flask-2022-09-05

https://sky.pro/wiki/python/ispolzovanie-funktsiy-python-v-shablonizatore-jinja2/
