<<<<<<< HEAD
from os import error
import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host="uh1.hnc.cl",
            user="keyzencl_admin",
            password="keyzencl123",
            db="keyzencl_auto9"
        )
        self.cursor = self.connection.cursor()

    #CRUD cliente
    
    #Añadir un cliente
    def add_user(self, nombre, apellido,  email, telefono):
        sql ="INSERT INTO cliente (nombre, apellido, email, telefono) VALUES ('{}', '{}', '{}', '{}')".format(nombre, apellido, email,telefono)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except ValueError:
            print("Ha ocurrido un error")
    #Seleccionar un cliente
    def get_user(self, id):
        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            else:
                sql = "SELECT * FROM cliente WHERE id={}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
                user = self.cursor.fetchone()
                return user
        except Exception:
            raise
    #Seleccionar un cliente por email
    def get_user_by_email(self, email):
        try:
            if email == None:
                raise Exception("No se ha ingresado ningún email")
            else:
                sql = "SELECT * FROM cliente WHERE email = '{}'".format(email)
                self.cursor.execute(sql)
                self.connection.commit()
                user = self.cursor.fetchone()
                return user
        except Exception:
            raise
    #actualizar un cliente
    def update_user(self, id, nombre, apellido, email, telefono):
        try:
            if id == None:
                raise Exception
            else:
                sql = "UPDATE cliente SET nombre = '{}', apellido = '{}', email = '{}', telefono = '{}' WHERE id='{}'".format(nombre, apellido, email, telefono, id)
                self.cursor.execute(sql)
                self.connection.commit()

        except Exception:
            raise
    #Seleccionar TODOS clientes        
    def get_users(self):
        sql ="SELECT * FROM cliente ORDER BY id ASC"

        try:

            self.cursor.execute(sql)
            self.connection.commit()
            users = self.cursor.fetchall()
            print(users)
            print("Se han obtenido los usuarios")
            return users

        except ValueError:
            print("Ha ocurrido un error al obtener los usuarios")
            return "No se han obtenido los usuarios"

    #Actualizar un nombre
    def update_users_name(self, id = None, nombre = None):

        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            elif nombre == None:
                raise Exception("No ha ingresado nombre para actualizar")
            else:
                if nombre != None:
                    if type(nombre) == str:
                        sql = "UPDATE cliente SET nombre = '{}' WHERE id = {} ".format(nombre, id)
                    else:
                        raise Exception("Debe ingresar un dato tipo cadena")

            self.cursor.execute(sql)
            self.connection.commit()
        except Exception:
            raise

    #Actualizar un apellido
    def update_users_surname(self, id = None, apellido = None):
        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            elif apellido == None:
                raise Exception("No ha ingresado apellido para actualizar")
            else:
                if apellido != None:
                    if type(apellido) == str:
                        sql = "UPDATE cliente SET apellido = '{}' WHERE id = {} ".format(apellido, id)
                    else:
                        raise Exception("Debe ingresar un dato tipo cadena")

            self.cursor.execute(sql)
            self.connection.commit()
        except Exception:
            raise     

    #Actualizar un email
    def update_users_email(self, id = None, email = None):
        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            elif email == None:
                raise Exception("No ha ingresado email para actualizar")
            else:
                if email != None:
                    if type(email) == str:
                        sql = "UPDATE cliente SET email = '{}' WHERE id = {} ".format(email, id)
                    else:
                        raise Exception("Debe ingresar un dato tipo cadena")

            self.cursor.execute(sql)
            self.connection.commit()
        except Exception:
            raise   

    #Actualizar un telefono
    def update_users_number(self, id = None, telefono = None):
        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            elif telefono == None:
                raise Exception("No ha ingresado telefono para actualizar")
            else:
                if telefono != None:
                    if type(telefono) == str:
                        sql = "UPDATE cliente SET telefono = '{}' WHERE id = {} ".format(telefono, id)
                    else:
                        raise Exception("Debe ingresar un dato tipo cadena")

            self.cursor.execute(sql)
            self.connection.commit()
        except Exception:
            raise     
    #Eliminar usuario  
    def delete_user(self, id = None):
        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            else:
                sql = "DELETE FROM cliente WHERE id = {}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    #Last users
    def last_users(self):
        try:
            sql = "SELECT * FROM cliente ORDER BY id DESC LIMIT 5;"
            self.cursor.execute(sql)
            self.connection.commit()
            lastUsers = self.cursor.fetchmany(5)
            return lastUsers
        except Exception:
            raise

    #Fabricantes
    def get_fabricators(self):
        try:
            sql = "SELECT * FROM fabricante"
            self.cursor.execute(sql)
            self.connection.commit()
            fabricators = self.cursor.fetchall()
            return fabricators
        except Exception:
            raise
    #Repuesto
    def add_spare(self, name, fabricator, observation):
        sql ="INSERT INTO repuesto (nombre, fabricante_id, observacion) VALUES ('{}', '{}', '{}')".format(name, fabricator, observation)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except ValueError:
            print("Ha ocurrido un error")
    def get_products(self):
        try:
            sql = "SELECT repuesto.id AS ID, repuesto.nombre AS Nombre, fabricante.nombre AS Fabricante, repuesto.observacion AS Observacion FROM repuesto INNER JOIN fabricante ON fabricante.id = repuesto.fabricante_id ORDER BY id ASC"
            self.cursor.execute(sql)
            products = self.cursor.fetchall()
            return products
        except Exception:
            raise
    def last_products(self):
        try:
            sql = "SELECT repuesto.id AS ID, repuesto.nombre AS Nombre, fabricante.nombre AS Fabricante, repuesto.observacion AS Observacion FROM repuesto INNER JOIN fabricante ON fabricante.id = repuesto.fabricante_id ORDER BY id DESC LIMIT 5;"
            self.cursor.execute(sql)
            self.connection.commit()
            lastProducts = self.cursor.fetchmany(5)
            return lastProducts
        except Exception:
            raise
    #obtener un producto
    def get_product(self, id):
        try:
            if id == None:
                raise Exception("No ha ingresado ningún id")
            else:
                sql = "SELECT * FROM repuesto WHERE id={}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
                product = self.cursor.fetchone()
                return product
        except Exception:
            raise
    #actualizar un producto
    def update_product(self, id, nombre, fabricante_id, observacion):
        try:
            if id == None:
                raise Exception("No se ha ingresado ningún id")
            else:
                sql = "UPDATE repuesto SET nombre = '{}', fabricante_id = '{}', observacion = '{}' WHERE id= {}".format(nombre, fabricante_id, observacion, id)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    #Eliminar producto
    def delete_product(self, id):
        try:
            if id == None:
                raise Exception("No se ha ingresado ningún id")
            else:
                sql = "DELETE FROM repuesto WHERE id = {}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    #Eliminar un fabricante
    def delete_fabricator(self, id):
        try:
            if id == None:
                raise Exception("No se ha ingresado ningún id")
            else:
                sql = "DELETE FROM fabricante WHERE id= {}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    def update_fabricator(self, id, name, country):
        try:
            if id == None:
                raise Exception("No ha ingresado ningún id")
            else:
                sql = "UPDATE fabricante SET nombre = '{}', pais = '{}' WHERE id ={}".format(name, country, id)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise 
    def get_fabricator(self, id):
        try:
            if id == None:
                raise Exception("No ha ingresado ningún id")
            else:
                sql = "SELECT * FROM fabricante WHERE id={}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
                fabricator = self.cursor.fetchone()
                return fabricator
        except Exception:
            raise
    def last_fabricators(self):
        try:
            sql = "SELECT * FROM fabricante ORDER BY id DESC LIMIT 5;"
            self.cursor.execute(sql)
            self.connection.commit()
            lastFabricators = self.cursor.fetchmany(5)
            return lastFabricators
        except Exception:
            raise
    def add_fabricator(self, name, country):
        try:
            if name == None or country == None:
                raise Exception("No se han ingresado suficientes datos")
            else:
                sql = "INSERT INTO fabricante (nombre, pais) VALUES ('{}','{}')".format(name, country)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    def add_quotation(self, cliente_id, mensaje, fabricante, modelo):
        try:
            if cliente_id == None:
                raise Exception("No hay id al cual agregar cotizacion")
            else:
                sql = "INSERT INTO cotizacion (cliente_id, mensaje, fabricante, modelo) VALUES ({}, '{}', '{}', '{}')".format(cliente_id, mensaje, fabricante, modelo)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    #Last quotations
    def last_quotations(self):
        try:
            sql = "SELECT cotizacion.id as id, cliente.nombre as Cliente,cotizacion.fabricante as Fabricante, cotizacion.modelo as Modelo, cotizacion.mensaje as Mensaje, cliente.email as Correo FROM cotizacion INNER JOIN cliente ON cliente.id = cotizacion.cliente_id ORDER BY id DESC LIMIT 6;"
            self.cursor.execute(sql)
            self.connection.commit()
            lastQuotations = self.cursor.fetchmany(6)
            return lastQuotations
        except Exception:
            raise
    #todas las cotizaciones
    def get_quotations(self):
        sql = "SELECT cotizacion.id as id, cliente.id as id_cliente, cliente.nombre as Cliente, cotizacion.fabricante as Fabricante, cotizacion.modelo as Modelo, cliente.email as Correo FROM cotizacion INNER JOIN cliente ON cliente.id = cotizacion.cliente_id"
        self.cursor.execute(sql)
        self.connection.commit()
        quotations = self.cursor.fetchall()
        return quotations
    #obtener texto cotizacion
    def get_quote(self, id):
        sql = "SELECT * FROM cotizacion WHERE id = {}".format()
        self.cursor.execute(sql)
        self.connection.commit()
        quote = self.cursor.fetchone()
        return quote
    def delete_quotation(self, id):
        try:
            if id == None:
                raise Exception("No se ha ingresado ningún id")
            else:
                sql = "DELETE FROM cotizacion WHERE id = {}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    def get_message(self, id):
        sql = "SELECT cotizacion.id, cliente.nombre as Cliente,cotizacion.fabricante as Fabricante, cotizacion.modelo as Modelo, cotizacion.mensaje as Mensaje, cliente.email as Correo FROM cotizacion INNER JOIN cliente ON cliente.id = cotizacion.cliente_id WHERE cotizacion.id = {}".format(id)
        self.cursor.execute(sql)
        self.connection.commit()
        quote = self.cursor.fetchone()
        return quote
    #agregar un modelo

    def add_model(self, fabricante_id, nombre, fabricacion):
        try:
            if fabricante_id == None:
                raise Exception("No se ha ingresado ningún id")
            else: 
                sql = "INSERT INTO modelo (fabricante_id, nombre, fabricacion) VALUES ('{}', '{}', '{}')".format(fabricante_id, nombre, fabricacion)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    #actualizar un modelo
    def update_model(self, id, fabricante_id, nombre, fabricacion):
        try:
            if id == None:
                raise Exception("No se ha ingresado ningún id")
            else:
                sql = "UPDATE modelo SET fabricante_id='{}', nombre = '{}', fabricacion = '{}' WHERE id = {}".format(fabricante_id, nombre, fabricacion, id)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    #eliminar un modelo
    def delete_model(self, id):
        try:
            if id == None:
                raise Exception("No se ha ingresado ningún id")
            else:
                sql = "DELETE FROM modelo WHERE id = {}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    #conseguir todos los modelos
    def get_models(self):
        sql = "SELECT modelo.id as id, fabricante.nombre as Fabricante, modelo.nombre as Modelo, modelo.fabricacion as Fecha FROM modelo INNER JOIN fabricante ON fabricante.id = modelo.fabricante_id"
        self.cursor.execute(sql)
        self.connection.commit()
        models = self.cursor.fetchall()
        return models

        

    def last_models(self):
        sql = "SELECT modelo.id as id, fabricante.nombre as Fabricante, modelo.nombre as Modelo, modelo.fabricacion as Fecha FROM modelo INNER JOIN fabricante ON fabricante.id = modelo.fabricante_id ORDER BY modelo.id DESC LIMIT 5;"
        self.cursor.execute(sql)
        self.connection.commit()
        models = self.cursor.fetchmany(5)
        return models
    #conseguir solo un modelo
    def get_model(self, id):
        try:
            if id == None:
                raise Exception("No se ha ingresado ningún id")
            else:
                sql = "SELECT modelo.id as id, fabricante.nombre as Fabricante, modelo.nombre as Modelo, modelo.fabricacion as Fecha FROM modelo INNER JOIN fabricante ON fabricante.id = modelo.fabricante_id WHERE modelo.id = {}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
                model = self.cursor.fetchone()
                return model
        except Exception:
            raise
        
    #agregar listaRepuestos
    def add_compatibility (self, repuesto_id, modelo_id, observaciones):
        sql = "INSERT INTO listarepuesto (repuesto_id, modelo_id, observaciones) values ('{}', '{}', '{}')".format(repuesto_id, modelo_id, observaciones)
        self.cursor.execute(sql)
        self.connection.commit()
    #Todos los listarepuestos
    def last_compatibility(self):
        sql = "select listarepuesto.id as id, repuesto.nombre as repuesto, modelo.nombre as modelo, modelo.fabricacion as año, listarepuesto.observaciones as observaciones from listarepuesto inner join repuesto on repuesto.id = listarepuesto.repuesto_id inner join modelo on modelo.id = listarepuesto.modelo_id ORDER BY id DESC LIMIT 6;"
        self.cursor.execute(sql)
        compatibility = self.cursor.fetchmany(6)
        return compatibility
    #obtener todas las compatibilidades
    def all_compatibility(self):
        sql = "select listarepuesto.id as id, repuesto.nombre as repuesto, modelo.nombre as modelo, modelo.fabricacion as año, listarepuesto.observaciones as observaciones from listarepuesto inner join repuesto on repuesto.id = listarepuesto.repuesto_id inner join modelo on modelo.id = listarepuesto.modelo_id ORDER BY id DESC"
        self.cursor.execute(sql)
        self.connection.commit()
        compatibilities = self.cursor.fetchall()
        return compatibilities 
    #eliminar compatibilidad
    def delete_compatibility(self, id):
        try:
            if id == None:
                raise Exception("No se ha ingresado ningún id")
            else:
                sql = "DELETE FROM listarepuesto WHERE id = {}".format(id)     
                self.cursor.execute(sql)
                self.connection.commit()   
        except Exception:
            raise
    #buscar compatibilidad
    def search_compatibility(self, search):
        try:
            if search == None:
                raise Exception("No se ha ingresado ningún id")
            else:
                sql = "select repuesto.nombre as Repuesto, modelo.nombre as Modelo, modelo.fabricacion as Fecha, fabricante.nombre as Fabricante FROM listarepuesto INNER JOIN repuesto ON repuesto.id = listarepuesto.repuesto_id INNER JOIN modelo ON modelo_id = listarepuesto.modelo_id INNER JOIN fabricante ON modelo.fabricante_id=fabricante.id WHERE modelo.nombre LIKE '{0}' or modelo.fabricacion LIKE '{0}' or fabricante.nombre LIKE '{0}' or repuesto.nombre LIKE '{0}'".format(search)
                self.cursor.execute(sql)
                self.connection.commit()
                items = self.cursor.fetchall()
                return items

        except Exception:
            raise

    


=======
from os import error
import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host="uh1.hnc.cl",
            user="keyzencl_admin",
            password="keyzencl123",
            db="keyzencl_auto9"
        )
        self.cursor = self.connection.cursor()

    #CRUD cliente
    
    #Añadir un cliente
    def add_user(self, nombre, apellido,  email, telefono):
        sql ="INSERT INTO cliente (nombre, apellido, email, telefono) VALUES ('{}', '{}', '{}', '{}')".format(nombre, apellido, email,telefono)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except ValueError:
            print("Ha ocurrido un error")
    #Seleccionar un cliente
    def get_user(self, id):
        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            else:
                sql = "SELECT * FROM cliente WHERE id={}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
                user = self.cursor.fetchone()
                return user
        except Exception:
            raise
    #actualizar un cliente
    def update_user(self, id, nombre, apellido, email, telefono):
        try:
            if id == None:
                raise Exception
            else:
                sql = "UPDATE cliente SET nombre = '{}', apellido = '{}', email = '{}', telefono = '{}' WHERE id='{}'".format(nombre, apellido, email, telefono, id)
                self.cursor.execute(sql)
                self.connection.commit()

        except Exception:
            raise
    #Seleccionar TODOS clientes        
    def get_users(self):
        sql ="SELECT * FROM cliente ORDER BY id ASC"

        try:

            self.cursor.execute(sql)
            self.connection.commit()
            users = self.cursor.fetchall()
            print(users)
            print("Se han obtenido los usuarios")
            return users

        except ValueError:
            print("Ha ocurrido un error al obtener los usuarios")
            return "No se han obtenido los usuarios"

    #Actualizar un nombre
    def update_users_name(self, id = None, nombre = None):

        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            elif nombre == None:
                raise Exception("No ha ingresado nombre para actualizar")
            else:
                if nombre != None:
                    if type(nombre) == str:
                        sql = "UPDATE cliente SET nombre = '{}' WHERE id = {} ".format(nombre, id)
                    else:
                        raise Exception("Debe ingresar un dato tipo cadena")

            self.cursor.execute(sql)
            self.connection.commit()
        except Exception:
            raise

    #Actualizar un apellido
    def update_users_surname(self, id = None, apellido = None):
        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            elif apellido == None:
                raise Exception("No ha ingresado apellido para actualizar")
            else:
                if apellido != None:
                    if type(apellido) == str:
                        sql = "UPDATE cliente SET apellido = '{}' WHERE id = {} ".format(apellido, id)
                    else:
                        raise Exception("Debe ingresar un dato tipo cadena")

            self.cursor.execute(sql)
            self.connection.commit()
        except Exception:
            raise     

    #Actualizar un email
    def update_users_email(self, id = None, email = None):
        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            elif email == None:
                raise Exception("No ha ingresado email para actualizar")
            else:
                if email != None:
                    if type(email) == str:
                        sql = "UPDATE cliente SET email = '{}' WHERE id = {} ".format(email, id)
                    else:
                        raise Exception("Debe ingresar un dato tipo cadena")

            self.cursor.execute(sql)
            self.connection.commit()
        except Exception:
            raise   

    #Actualizar un telefono
    def update_users_number(self, id = None, telefono = None):
        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            elif telefono == None:
                raise Exception("No ha ingresado telefono para actualizar")
            else:
                if telefono != None:
                    if type(telefono) == str:
                        sql = "UPDATE cliente SET telefono = '{}' WHERE id = {} ".format(telefono, id)
                    else:
                        raise Exception("Debe ingresar un dato tipo cadena")

            self.cursor.execute(sql)
            self.connection.commit()
        except Exception:
            raise     
    #Eliminar usuario  
    def delete_user(self, id = None):
        try:
            if id == None:
                raise Exception("No ha ingresado ningun id")
            else:
                sql = "DELETE FROM cliente WHERE id = {}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    #Last users
    def last_users(self):
        try:
            sql = "SELECT * FROM cliente ORDER BY id DESC LIMIT 5;"
            self.cursor.execute(sql)
            self.connection.commit()
            lastUsers = self.cursor.fetchall()
            return lastUsers
        except Exception:
            raise

    #Fabricantes
    def get_fabricators(self):
        try:
            sql = "SELECT * FROM fabricante"
            self.cursor.execute(sql)
            self.connection.commit()
            fabricators = self.cursor.fetchall()
            return fabricators
        except Exception:
            raise
    #Repuesto
    def add_spare(self, name, fabricator, observation):
        sql ="INSERT INTO repuesto (nombre, fabricante_id, observacion) VALUES ('{}', '{}', '{}')".format(name, fabricator, observation)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except ValueError:
            print("Ha ocurrido un error")
    def get_products(self):
        try:
            sql = "SELECT repuesto.id AS ID, repuesto.nombre AS Nombre, fabricante.nombre AS Fabricante, repuesto.observacion AS Observacion FROM repuesto INNER JOIN fabricante ON fabricante.id = repuesto.fabricante_id ORDER BY id ASC"
            self.cursor.execute(sql)
            products = self.cursor.fetchall()
            return products
        except Exception:
            raise
    def last_products(self):
        try:
            sql = "SELECT repuesto.id AS ID, repuesto.nombre AS Nombre, fabricante.nombre AS Fabricante, repuesto.observacion AS Observacion FROM repuesto INNER JOIN fabricante ON fabricante.id = repuesto.fabricante_id ORDER BY id DESC LIMIT 5;"
            self.cursor.execute(sql)
            self.connection.commit()
            lastProducts = self.cursor.fetchall()
            return lastProducts
        except Exception:
            raise
    #obtener un producto
    def get_product(self, id):
        try:
            if id == None:
                raise Exception("No ha ingresado ningún id")
            else:
                sql = "SELECT * FROM repuesto WHERE id={}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
                product = self.cursor.fetchone()
                return product
        except Exception:
            raise
    #actualizar un producto
    def update_product(self, id, nombre, fabricante_id, observacion):
        try:
            if id == None:
                raise Exception("No se ha ingresado ningún id")
            else:
                sql = "UPDATE repuesto SET nombre = '{}', fabricante_id = '{}', observacion = '{}' WHERE id= {}".format(nombre, fabricante_id, observacion, id)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise
    #Eliminar producto
    def delete_product(self, id):
        try:
            if id == None:
                raise Exception("No se ha ingresado ningún id")
            else:
                sql = "DELETE FROM repuesto WHERE id = {}".format(id)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception:
            raise




    


>>>>>>> 0bda20bd28948ad8f035e735437996e297167a76
