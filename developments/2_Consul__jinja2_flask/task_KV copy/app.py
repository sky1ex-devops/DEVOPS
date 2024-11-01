from flask import Flask, render_template, request
import consul

app = Flask(__name__)
c = consul.Consul(host='127.0.0.1', port=8500)


@app.route("/")
def home():
    global c
    index, data = c.kv.get(key='', recurse=True) # Забираем инфу о ключах из consul

 #-----ЗАБИРАЕМ ЗНАЧЕНИЯ ИЗ CONSUL-----#
    keys = []
    
    for edata in data:
        data = edata.get('Key', None)
        keys.append(data)

#-----СОРТИРУЕМ КЛЮЧИ, ОТБИРАЕМ КАТАЛОГИ-----#
# оставляем элементы где присутстует /
    stringVal = "/"
    no_key = [ x for x in keys if stringVal in x ] 
# удалить все после символа /
    no_slash = [x.replace(" ", "").split("/")[0] for x in no_key] 
# Удаляем повторяющиеся значения
    kt = list(set(no_slash))
    ktl = sorted(kt)

    index, data = c.kv.get(key='', recurse=True) # Забираем инфу о ключах из consul
    krtg = []
    for edata in data: 
        keys = edata.get('Key', None) # оставляем только ключи 
        krtg.append(keys) # и соханяем в кортеж для будушей проверки

    return render_template("base.html", title="task_KV", ktl_root=ktl, data_root=krtg)

@app.route("/root")  
def root():
    krtg = []
    global c
    index, data = c.kv.get(key='', recurse=True) # Забираем инфу о ключах из consul
    
    for edata in data: 
        keys = edata.get('Key', None) # оставляем только ключи 
        krtg.append(keys) # и соханяем в кортеж для будушей проверки

    return render_template(f"base.html", title="task_KV", data_root=krtg) # выводим значение на страницу

@app.route("/folder1")
def folder1():
    global c
    index, data = c.kv.get(key='', recurse=True)
    ddata = []
    for d in data:
        ddata = d.get("Key")
    return render_template("folder1.html", title="task_KV", data_folder1=ddata)

@app.route("/folder2")
def folder2():
    return render_template("folder2.html", title="task_KV")

@app.route("/folder3")
def folder3():
    return render_template("folder3.html", title="task_KV")

#######################################################################

@app.route('/search', methods=['POST']) # создаем маршрут /sumbit
def submit(): # создаем функцию sumbit без параметров
    krtg = [] 
    global c
    index, data = c.kv.get(key='', recurse=True) # Забираем инфу о ключах из consul
    
    for edata in data: 
        keys = edata.get('Key', None) # оставляем только ключи 
        krtg.append(keys) # и соханяем в кортеж для будушей проверки

    global mess
    mess = request.form['name'] # Записываем введенный ключ пользователем, в переменную mess

    index, data = c.kv.get(key='', recurse=True) # Забираем инфу о ключах из consul

 #-----ОТБИРАЕМ ЗНАЧЕНИЯ ИЗ CONSUL-----#
    keys = []
    
    for edata in data:
        data = edata.get('Key', None)
        keys.append(data)

#-----СОРТИРУЕМ КЛЮЧИ, ОТБИРАЕМ КАТАЛОГИ-----#
# оставляем элементы где присутстует /
    stringVal = "/"
    no_key = [ x for x in keys if stringVal in x ] 
# удалить все после символа /
    no_slash = [x.replace(" ", "").split("/")[0] for x in no_key] 
# Удаляем повторяющиеся значения
    kt = list(set(no_slash))
    ktl = sorted(kt)
    

    while True:
        if mess not in krtg:
            return render_template(f"base.html", title="task_KV", messg=" не существует!") # выводим значение на страницу
        else:
            index, data = c.kv.get(mess) # по ключу
            req_value = data['Value']          # записываем полученное значение из consul в переменную req_value
            #reqdecode = req_value.decode()     # приобразовуем байтовую строку
            
            return render_template(f"base.html", title="task_KV", messg=mess, result=req_value, data_root=krtg, ktl_root=ktl) # выводим значение на страницу

@app.route('/edit', methods=['POST'])
def edit():
    
    global mess # обьявляем глобальную переменную
    global c
    index, data = c.kv.get(key='', recurse=True) # Забираем инфу о ключах из consul

 #-----ОТБИРАЕМ ЗНАЧЕНИЯ ИЗ CONSUL-----#
    keys = []
    for edata in data:
        data = edata.get('Key', None)
        keys.append(data)

#-----СОРТИРУЕМ КЛЮЧИ, ОТБИРАЕМ КАТАЛОГИ-----#
# оставляем элементы где присутстует /
    stringVal = "/"
    no_key = [ x for x in keys if stringVal in x ] 
# удалить все после символа /
    no_slash = [x.replace(" ", "").split("/")[0] for x in no_key] 
# Удаляем повторяющиеся значения
    kt = list(set(no_slash))
    ktl = sorted(kt)
    vl = request.form['req'] # записываем ввод пользователя для поле нового значения
    
    
    if vl != '':
        c.kv.put(mess, vl) # Записываем изменения в консул 
        return render_template(f"base.html", title="task_KV", messg=mess, result=vl, ktl_root=ktl) # выводим значение на страницу
    elif mess == '':
        return render_template(f"base.html", title="task_KV", messg=" Какой ключ!?", ktl_root=ktl) # выводим значение на страницу
    else:
        return render_template(f"base.html", title="task_KV", nono=" Введите значение !", ktl_root=ktl) # выводим значение на страницу



if __name__ == "__main__":
    app.run(debug=True)