from flask import Flask, render_template, request
import consul

app = Flask(__name__) # Создаем переменную app и записываем в неё класс Flask с функцией __name__


@app.route("/") # создаем маршрут /
def home(): # создаем функцию home без параметров
    return render_template("base.html", title="Consul-Jinja-Flask") # Возвращаем шаблон base.html и заполняем в нем переменную title


@app.route('/search', methods=['POST']) # создаем маршрут /sumbit
def submit(): # создаем функцию sumbit без параметров
    krtg = [] 
    c = consul.Consul(host='127.0.0.1', port=8500) 
    index, data = c.kv.get(key='', recurse=True) # Забираем инфу о ключах из consul
    
    for edata in data: 
        keys = edata.get('Key', None) # оставляем только ключи 
        krtg.append(keys) # и соханяем в кортеж для будушей проверки

    mess = request.form['name'] # Записываем введенный ключ пользователем, в переменную mess
    
    while True:
        if mess not in krtg:
            return render_template(f"base.html", title="Consul-Jinja-Flask", messg=" не существует!") # выводим значение на страницу
        else:
            index, data = c.kv.get(mess) # по ключу
            req_value = data['Value']          # записываем полученное значение из consul в переменную req_value
            #reqdecode = req_value.decode()     # приобразовуем байтовую строку
            
            return render_template(f"base.html", title="Consul-Jinja-Flask", messg=mess, result=req_value) # выводим значение на страницу


@app.route('/edit', methods=['POST'])
def edit():
    mess = request.form['name'] # Записываем введенный ключ пользователем, в переменную mess
    req = request.form['req']
    c = consul.Consul(host='127.0.0.1', port=8500) 
    c.kv.put(mess, req)
    return render_template(f"base.html", title="Consul-Jinja-Flask", messg=mess, result=req) # выводим значение на страницу



if __name__ == "__main__":
    app.run(debug=True) # Выполнять программу в режиме debug mode