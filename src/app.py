#Modulos necesarios
from database import *
from flask import Flask, redirect, url_for, request, jsonify, render_template

#Inicialización de servidor y database
app = Flask(__name__)
database = DataBase()

users = [{"nombre":"pepe", "numero":"9"}, {"nombre":"jose", "numero":"10"}]



@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        print("Entraron al index")
        return render_template("index.html")


@app.route('/users', methods=["GET", "POST"])

def get_users():
    if request.method == "GET":
        print("Hola mundo desde python")
        usuarios = database.get_users()
        return redirect(url_for('.index'))      

@app.route('/users/add', methods=["GET", "POST"])
def show_forms():
    if request.method == "GET":
        return render_template("addusers.html")
    elif request.method == "POST":
        print("Estan agregando un usuario")
        print(request.form)
        print(request.form["name"])
        req = request.form
        database.add_user(req["name"], req["surname"], req["email"],req["phone"])
        user = {
            "nombre" : req["name"],
            "apellido" : req["surname"],
            "email" : req["email"],
            "teléfono" : req["phone"]
        }
        return user
@app.route('/test')
def test():
    return "Hola como tas"



app.run(debug=True)
