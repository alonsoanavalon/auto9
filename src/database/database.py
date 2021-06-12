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




    


