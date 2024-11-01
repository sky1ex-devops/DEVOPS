from flask import Flask, render_template, request
import consul

#######################################################################
#           ЗАБИРАЕМ ИНФОРМАЦИЮ ИЗ CONSUL

app = Flask(__name__)
c = consul.Consul(host='127.0.0.1', port=8500)
index, data = c.kv.get(key='', recurse=True) # Забираем инфу о ключах из consul

keys = []
    
for edata in data:
    data = edata.get('Key', None)
    keys.append(data)

#######################################################################
#           ПЕРЕБИРАЕМ КАТАЛОГИ И КЛЮЧИ

vles=keys
d_folder = [] # список для не отсартированых каталогов
dir_folder = [] # список для отсартированых каталогов
dir_key = [] # список для ключей
for p in vles: # перебираем элементы списка
    if '/' in p:                        # Если присутствует / 
        folder, key = p.split('/', 1)   # Отделяем строку на до и после /
        d_folder.append(folder)         # Записываем то что до в список 
    else:                               # Если / НЕТ 
        dir_key.append(p)               # значит это ключ, записываем в список ключей

    del_fld = list(set(d_folder)) # Удаляем поворяющиеся значения
    dir_folder = sorted(del_fld)

#######################################################################
#      ВЫВОДИМ НА ГЛАВНУЮ СТРАНИЦУ МЕНЮ НАВИГАЦИИ И ЗАПОЛНИТЕЛЬ          

@app.route("/")
def home():
   
    return render_template("base.html", title="task_KV", dir_folder=dir_folder, dir_key=dir_key)

#######################################################################
#         ОБРАБАТЫВАЕМ НАЖАТИЕ НА КАТАЛОГ ROOT В МЕНЮ НАВИГАЦИИ

@app.route("/root", methods=['POST'])
def root():
    
    return render_template("base.html", title="task_KV", dir_folder=dir_folder, dir_key=dir_key)

#######################################################################
#         ОБРАБАТЫВАЕМ НАЖАТИЕ НА КАТАЛОГ В МЕНЮ НАВИГАЦИИ

@app.route("/folders", methods=['POST'])
def folders():
    global ddir_key
    ddir_key = []
    m = request.form['tap_fl'] # Записываем введенный ключ пользователем, в переменную mess
    #m = "folder1"
    ### КЛЮЧИ В УКАЗАННОЙ ДЕРРИКТОРИИ
    
    
    for p in vles: # перебираем элементы списка
        if m in p and '/' in p:
            folder, key = p.split('/', 1)   # Отделяем строку на до и после /
            if key != "":
                ddir_key.append(p)         # Записываем то что до в список 
        
    
    
    return render_template("base.html", title="task_KV", dir_folder=dir_folder, dir_key=ddir_key)

#######################################################################
#                    ФУНКЦИОНАЛ ПОИСКА КЛЮЧЕЙ

@app.route('/search', methods=['POST']) # создаем маршрут /sumbit
def submit(): # создаем функцию sumbit без параметров
    global mess
    global ddir_key
    
    mess = request.form['name'] # Записываем введенный ключ пользователем, в переменную mess

    if mess in keys:
        index, data = c.kv.get(mess) # по ключу
        req_value = data['Value']          # записываем полученное значение из consul в переменную req_value
        reqdecode = req_value.decode()     # приобразовуем байтовую строку
        return render_template(f"base.html", title="task_KV", messg=mess, result=reqdecode, dir_folder=dir_folder, dir_key=dir_key) # выводим значение на страницу
    elif mess in ddir_key:
        index, data = c.kv.get(mess) # по ключу
        req_value = data['Value']          # записываем полученное значение из consul в переменную req_value
        reqdecode = req_value.decode()     # приобразовуем байтовую строку
        return render_template(f"base.html", title="task_KV", messg=mess, result=reqdecode, dir_folder=dir_folder, dir_key=ddir_key) # выводим значение на страницу
    else:
        return render_template(f"base.html", title="task_KV", messg=" не существует!") # выводим значение на страницу
        
#######################################################################
#                       ЗАПИСЬ НОВЫЙХ ЗНАЧЕНИЙ

@app.route('/edit', methods=['POST'])
def edit():
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

    vl = request.form['req'] # записываем ввод пользователя,поле нового значения
    
    if vl != '':
        c.kv.put(mess, vl) # Записываем изменения в консул 
        return render_template(f"base.html", title="task_KV", messg=mess, result=vl, ktl_root=ktl, data_root=keys, dir_folder=dir_folder, dir_key=dir_key) # выводим значение на страницу
    elif mess == '':
        return render_template(f"base.html", title="task_KV", messg=" Какой ключ!?", ktl_root=ktl, data_root=keys, dir_folder=dir_folder, dir_key=dir_key) # выводим значение на страницу
    else:
        return render_template(f"base.html", title="task_KV", nono=" Введите значение !", ktl_root=ktl, data_root=keys, dir_folder=dir_folder, dir_key=dir_key) # выводим значение на страницу

#######################################################################

if __name__ == "__main__":
    app.run(debug=True)