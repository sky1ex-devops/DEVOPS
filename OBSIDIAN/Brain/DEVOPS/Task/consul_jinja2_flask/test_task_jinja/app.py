from flask import Flask, render_template, request
import consul

app = Flask(__name__) # Создаем переменную app и записываем в неё класс Flask с функцией __name__

@app.route("/") # создаем маршрут /
def home(): # создаем функцию home без параметров
   # return "Hello, World!" # тест 
    return render_template("base.html", title="Jinja and Flask") # Возвращаем шаблон base.html и заполняем в нем переменную title

@app.route('/submit', methods=['POST'])
def submit():
  mess = request.form['name']
 # return f'{mess}'
  return render_template(f"base.html", result=mess) 


if __name__ == "__main__": 
    app.run(debug=True) # Выполнять программу пока нет ошибок