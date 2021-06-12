#Modulos necesarios

from database import database
from flask import Flask, redirect, url_for, request, jsonify, render_template


#Inicialización de servidor y database
app = Flask(__name__)
db = database.DataBase()

                                                #Rutas

#Ruta de inicio
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        print("Entraron al index")
        return render_template("index.html")

#Ruta de administrador
@app.route('/admin', methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        if request.args.get('id') == None:
            return render_template('admin.html')        

                                        #Ruta para panel de usuarios
@app.route('/admin/users', methods=["GET", "POST"])

def users():
    if request.method == "GET":
        lastUsers = db.last_users()
        return render_template('users.html', lastUsers = lastUsers)


#Ruta para obtener todos los usuarios/actualizar/eliminar
@app.route('/admin/users/all', methods=["GET", "POST"])
def get_users():
        if request.method == "GET":
        #Si no viene nada en el id quiere decir que solo quiere obtener usuarios, sino quiere eliminar
            if request.args.get('id') == None:
                users = db.get_users()
                return render_template('all_users.html', users = users)
            elif request.args.get('id') != None:
                #Si el metodo es delete, se elimina por id, sino puedo hacer alguna otra cosa
                id = request.args.get('id')
                if request.args.get('method') == "delete":
                    print(request.args.get('method'))
                    print("pasamos method")
                    db.delete_user(id)
                    return redirect('/admin/users/all')
                if request.args.get('method') == 'update':
                    user = db.get_user(id)
                    return render_template("update_user.html", user = user)
#Ruta para actualizar usuario
@app.route('/admin/users/update', methods = ["GET", "POST"])
def update_user():
    if request.method == "POST":
        req = request.form
        db.update_user(req["id"], req["name"], req["surname"], req["email"], req["phone"])
        return render_template("success.html", updatedUser = req["name"] )
                    
    
#Ruta para agregar un usuario
@app.route('/admin/users/add', methods=["GET", "POST"])
def show_forms():
    if request.method == "POST":
        print("Estan agregando un usuario")
        print(request.form)
        print(request.form["name"])
        req = request.form
        db.add_user(req["name"], req["surname"], req["email"],req["phone"])
        return render_template('success.html', user = req["name"])
    else:
        return render_template('404.html')
                                            #Ruta para panel de productos

@app.route('/admin/products', methods=["GET", "POST"])
def products():
    fabricators = db.get_fabricators()
    lastProducts = db.last_products()
    return render_template('products.html', fabricators = fabricators, lastProducts = lastProducts)
#Ruta para ver todos los productos
@app.route('/admin/products/all', methods = ["GET", "POST"])
def get_products():
    if request.args.get('id') == None:
        if request.method == "GET":
            products = db.get_products()
            return render_template('all_products.html', products = products)
    elif request.args.get('id') != None:
        id = request.args.get('id')
        if request.args.get('method') == 'delete':
            db.delete_product(id)
            return redirect('/admin/products/all')
        elif request.args.get('method') == 'update':
            product = db.get_product(id)
            fabricators = db.get_fabricators()
            return render_template('update_product.html', product = product, fabricators = fabricators)

#Ruta para agregar productos
@app.route('/admin/products/add', methods=["GET", "POST"])
def add_products():
    if request.method == "GET":
        return render_template("404.html")
    elif request.method == "POST":
        print("Estan agregando un repuesto")
        print(request.form)
        req = request.form
        db.add_spare(req["name"], req["fabricator"], req["observation"])
        return render_template('success.html', spare = req["name"]) 
#Ruta para actualizar repuestos
@app.route('/admin/products/update', methods=["POST"])
def update_products():
    if request.method == "POST":
        req = request.form
        print(req)
        db.update_product(req['id'], req['name'], req['fabricator'], req['observation'])
        return render_template('success.html',updatedSpare = req['name'] )





app.run(debug=True)
