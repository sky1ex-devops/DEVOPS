# app.py
from flask import render_template # Remove: import Flask
import connexion

app = connexion.App(__name__, specification_dir="./") # specification_dir сообщает классу Connexion,
# в какой директории искать конфигурационный файл. В данном случае он находится в той же папке, что и файл app.py.
app.add_api("swagger.yml") # читаем файл swagger.yml и настраиваем систему для обеспечения 
# функциональности класса Connexion.

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)