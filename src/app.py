#Modulos necesarios

from database import database
from flask import Flask, redirect, url_for, request, jsonify, render_template


#Inicialización de servidor y database
app = Flask(__name__)
db = database.DataBase()

#Rutas

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        print("Entraron al index")
        return render_template("index.html")


@app.route('/users', methods=["GET", "POST"])

def get_users():
    if request.method == "GET":
        #Si no viene nada en el id quiere decir que solo quiere obtener usuarios, sino quiere eliminar
        if request.args.get('id') == None:
            users = db.get_users()
            return render_template('users.html', users = users)
        #Si viene algo en el id hace esto
        elif request.args.get('id') != None:
            #Si el metodo es delete, se elimina por id, sino puedo hacer alguna otra cosa
            if request.args.get('method') == "delete":
                id = request.args.get('id')
                print(request.args.get('method'))
                print("pasamos method")
                db.delete_user(id)
                return redirect('/users')
            

@app.route('/users/add', methods=["GET", "POST"])
def show_forms():
    if request.method == "GET":
        return render_template("addusers.html")
    elif request.method == "POST":
        print("Estan agregando un usuario")
        print(request.form)
        print(request.form["name"])
        req = request.form
        db.add_user(req["name"], req["surname"], req["email"],req["phone"])
        return render_template('success.html', user = req["name"])

@app.route('/products', methods=["GET", "POST"])
def products():
    if request.method == "GET":
        products = db.get_products()
        return render_template('products.html', products = products)




app.run(debug=True)
