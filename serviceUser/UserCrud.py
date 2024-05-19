# import mysql
#import json
from .UserServices import UserServices
"""
    In this script we are going to call
    the sql sentences for the db

"""
'''
class UserCrud(UserServices):
    """
    Define the real object that the proxy represents.
    """
    def __init__(self) -> None:
        self._connection_db_user = self.conectar_bd()
        #self._close_db_user = 

    def conectar_bd(self, db_user_config):
        return mysql.connector.connect(**db_user_config)

# Función para cerrar la conexión a la base de datos
    def cerrar_bd(self, conn):
        conn.close()
        #self._connection_db_user.close()

    def auth(self, username: str, password: str) -> bool:
        if username == 'user' and password == '123':
            return True
        else:
            return False
        
    def user_register(self, username: str, name: str, lastname: str, password: str):
        try:
            #user = request.json
            #conn = conectar_bd()  # Utilizar la función de conexión
            #user = {'Usuario' : }
            user = {
            'Usuario' : username,
            'Nombre' : name,
            'Apellido' : lastname,
            'Contrasena' : password
            }

            conn = self._connection_db_user
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (user_name, nombre, apellido, contrasena) VALUES (%s, %s, %s, %s)",
                            (user['Usuario'], user['Nombre'], user['Apellido'], user['Contrasena']))
            conn.commit()
            self.cerrar_bd(conn)  # Utilizar la función para cerrar la conexión
            print('Usuario insertado', user)
            return 'Usuario insertado', 200
        except Exception as e:
            print('Error al insertar usuario', e)
            return 'Error al insertar usuario', 500
        
    def email_register(self, email: str, name: str, lastname: str, password: str):
        try:
            #user = request.json
            #conn = conectar_bd()  # Utilizar la función de conexión
            #user = {'Usuario' : }
            user = {
            'Correo' : email,
            'Nombre' : name,
            'Apellido' : lastname,
            'Contrasena' : password
            }

            conn = self._connection_db_user
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (correo, nombre, apellido, contrasena) VALUES (%s, %s, %s, %s)",
                            (user['Correo'], user['Nombre'], user['Apellido'], user['Contrasena']))
            conn.commit()
            self.cerrar_bd(conn)  # Utilizar la función para cerrar la conexión
            print('Usuario insertado por correo', user)
            return 'Usuario insertado', 200
        except Exception as e:
            print('Error al insertar usuario por', e)
            return 'Error al insertar usuario', 500
'''
class UserCrud(UserServices):
    def __init__(self) -> None:
        pass
        #self._connection_db_user = self.conectar_bd()
        #self._close_db_user = 
    def auth(self, username, password) -> bool:
        if username == 'user' and password == '123':
            return True
        else:
            return False