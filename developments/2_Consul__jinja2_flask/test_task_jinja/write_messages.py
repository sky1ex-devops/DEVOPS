from jinja2 import Environment, FileSystemLoader

max_score = 100 # Задаем максимальное значение для переменной.
test_name = "Тест-Python"
students = [
    {"name": "Sandrine",  "score": 100}, # Создаем словари с данными для каждого ученика 
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
]

environment = Environment(loader=FileSystemLoader("temp/")) # Создаем среду и указываем путь к шаблону
temp = environment.get_template("message.txt") # Загружаем шаблон

for student in students: 
    filename = f"message_{student['name'].lower()}.txt" # 
    content = temp.render( # возвращаем отображаемый шаблон в виде строки
        student,
        max_score=max_score,
        test_name=test_name
    )
    with open(filename, mode="w", encoding="utf-8") as message: # открывем файл с функцией записи
        message.write(content) # записываем в файл готовые строки 
        print(f"... wrote {filename}")