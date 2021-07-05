#Modulos necesarios

from pymysql import get_client_info
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
        fabricators = db.get_fabricators()
        models = db.get_models()
        return render_template("index.html", fabricators = fabricators, models = models)
    
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

#Ruta para acceder a clientes
@app.route('/admin/fabricators/all', methods=["GET", "POST"])

def get_fabricators():
    if request.method == "GET":
        if request.args.get("id") == None:
            fabricators = db.get_fabricators()
            return render_template("all_fabricators.html", fabricators = fabricators)
        else:
            id = request.args.get("id")
            method = request.args.get("method")
            if method == "delete":
                db.delete_fabricator(id)
                return redirect('/admin/fabricators/all')
            else:
                fabricator = db.get_fabricator(id)
                return render_template('update_fabricator.html', fabricator = fabricator)
@app.route('/admin/fabricators/update', methods=["GET", "POST"])
def update_fabricator():
    if request.method == "POST":
        req = request.form
        db.update_fabricator(req["id"], req["name"], req["country"])
        return render_template("success.html", updatedFabricator = req["name"])


@app.route('/admin/fabricators', methods=["GET", "POST"])
def fabricators():
    if request.method == "GET":
        lastFabricators = db.last_fabricators()
        return render_template("fabricators.html", lastFabricators = lastFabricators)

@app.route('/admin/fabricators/add', methods=["GET", "POST"])
def add_fabricator():
    if request.method == "POST":
        req = request.form
        db.add_fabricator(req["name"], req["country"])
        fabricator = req["name"]
        return render_template("success.html", fabricator = fabricator)
@app.route('/quotation/add', methods=["GET", "POST"])
def add_quotation():
    if request.method == "POST":
        req = request.form
        print(req)
        user = db.get_user_by_email(req["email"])
        if user == None:
            db.add_user(req["name"], req["surname"], req["email"], req["phone"])
            user = db.get_user_by_email(req["email"])
            db.add_quotation(user[0], req["message"], req["fabricante"], req["model"])
            return("La cotizacion {} ha sido añadida al usuario NUEVO {} id {}".format(req["message"], user[1], user[0]))   
        else:
            db.add_quotation(user[0], req["message"], req["fabricante"], req["model"])
            return("La cotizacion {} ha sido añadida al usuario EXISTENTE {} id {}".format(req["message"], user[1], user[0]))
@app.route('/admin/quotations', methods = ["GET", "POST"])
def quotations():
    if request.method == "GET":
        lastQuotations = db.last_quotations()
        return render_template('quotations.html', lastQuotations = lastQuotations)
@app.route('/admin/quotations/all', methods=["GET", "POST"])
def all_quotations():
    if request.method == "GET":
        if request.args.get("id") == None:
                quotations = db.get_quotations()
                return render_template("all_quotations.html", quotations = quotations)      
        else:
            id = request.args.get("id")
            method = request.args.get("method")
            if method == "view":
                quote = db.get_message(id)
                return render_template("quote.html", quote = quote)
            elif method == "delete":
                db.delete_quotation(id)
                page = request.args.get("page")
                if page == "cards":
                    return redirect('/admin/quotations')
                else:
                    return redirect('/admin/quotations/all')
@app.route('/admin/models', methods=["GET", "POST"])
def models():
    if request.method == "GET":
        models = db.get_models()
        lastModels = db.last_models()
        fabricators = db.get_fabricators()
        return render_template("models.html", models = models, lastModels = lastModels, fabricators = fabricators)
    if request.method == "POST":
        req = request.form
        db.add_model(req["fabricator"], req["name"], req["year"])
        model = req["name"]
        return render_template("success.html", model = model)
@app.route('/admin/models/all', methods=["GET", "POST"])
def get_models():
    if request.method == "GET":
        id = request.args.get("id")
        method = request.args.get("method")
        if id == None:
            models = db.get_models()
            return render_template('all_models.html', models = models)
        else:
            if method == "update":
                model = db.get_model(id)
                fabricators = db.get_fabricators()
                return render_template("update_model.html", model = model, fabricators = fabricators)
            elif method == "delete":
                mensaje = db.delete_model(id)
                print(mensaje)
                return redirect("/admin/models/all")
@app.route('/admin/models/update', methods = ["GET", "POST"])
def update_model():
    if request.method == "POST":
        req = request.form
        db.update_model(req["id"], req["fabricator"], req["model"], req["year"])
        return redirect('/admin/models/all')
@app.route('/admin/compatibility', methods=["GET", "POST"])
def compatibility():
    if request.method == "GET":
        products = db.get_products()
        models = db.get_models()
        compatibility = db.last_compatibility()
        return render_template("compatibility.html", models = models, products = products, lastCompatibility = compatibility)
@app.route('/admin/compatibility/add', methods=["GET", "POST"])
def add_compatibility():
    if request.method == "POST":
        req = request.form
        db.add_compatibility(req["product"], req["model"], req["observaciones"])
        return redirect ('/admin/compatibility')

@app.route('/admin/compatibility/all', methods=["GET", "POST"])
def all_compatibility():
    if request.method == "GET":
        id = request.args.get("id")
        method = request.args.get("method")
        if id == None:
            compatibilities = db.all_compatibility()
            return render_template("all_compatibility.html", compatibilities = compatibilities)
        else:
            if method == "delete":
                db.delete_compatibility(id)
                return redirect('/admin/compatibility/all')

@app.route('/admin/compatibility/search', methods = ["GET", "POST"])
def search_compatibility():
    if request.method == "POST":
        req = request.form
        items = db.search_compatibility(req["keywords"])

        return render_template("search-compatibility.html", items = items)
    


              









app.run(debug=True)
