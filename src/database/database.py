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
    #Seleccionar TODOS clientes        
    def get_users(self):
        sql ="SELECT * FROM cliente"

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



    


