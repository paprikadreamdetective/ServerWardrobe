
# import mysql
#import json

import mysql
import json
from flask import Flask, render_template, request, redirect, url_for, flash

from .UserServices import UserServices
"""
    In this script we are going to call
    the sql sentences for the db

"""

class UserCrud(UserServices):
    """
    Define the real object that the proxy represents.
    """
    def __init__(self) -> None:
        self._connection_db_user = self.conectar_bd()
        #self._close_db_user = 

    def conectar_bd(self):
        db_user_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '1234',
            'database': 'proyecto_pp'
        }
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
            # Construir el diccionario del usuario
            user = {
                'Usuario' : username,
                'Nombre' : name,
                'Apellido' : lastname,
                'Contrasena' : password
            }

            # Verificar si ya existe un usuario con el mismo nombre de usuario
            conn = self._connection_db_user
            cursor = conn.cursor()
            query_select = "SELECT * FROM users WHERE BINARY username = %s"
            cursor.execute(query_select, (user['Usuario'],))
            existing_user = cursor.fetchone()

            # Si el usuario no existe, proceder con la inserción
            if not existing_user:
                query_insert = "INSERT INTO users (username, uname, lastname, password) VALUES (%s, %s, %s, %s)"
                cursor.execute(query_insert, (user['Usuario'], user['Nombre'], user['Apellido'], user['Contrasena']))
                conn.commit()
                self.cerrar_bd(conn)  # Utilizar la función para cerrar la conexión
                print('Usuario insertado', user)
                flash('Usuario agregado exitosamente!', 'success')
                return 'Usuario insertado', 200
            
            else:
                print("El usuario ya existe en la base de datos. No se ha realizado la inserción.")
                flash('El Usuario ya existe!', 'danger')
                return 'El usuario ya existe en la base de datos. No se ha realizado la inserción.', 400

        except Exception as e:
            print('Error al insertar usuario por username', e)
            return 'Error al insertar usuario por username', 500

        
    def email_register(self, email: str, name: str, lastname: str, password: str):
        try:
            # Construir el diccionario del usuario
            user = {
                'Correo' : email,
                'Nombre' : name,
                'Apellido' : lastname,
                'Contrasena' : password
            }

            # Verificar si ya existe un usuario con el mismo correo electrónico
            conn = self._connection_db_user
            cursor = conn.cursor()
            query_select = "SELECT * FROM users WHERE BINARY email = %s"
            cursor.execute(query_select, (user['Correo'],))
            existing_user = cursor.fetchone()

            # Si el usuario no existe, proceder con la inserción
            if not existing_user:
                query_insert = "INSERT INTO users (email, uname, lastname, password) VALUES (%s, %s, %s, %s)"
                cursor.execute(query_insert, (user['Correo'], user['Nombre'], user['Apellido'], user['Contrasena']))
                conn.commit()
                self.cerrar_bd(conn)  # Utilizar la función para cerrar la conexión
                print('Usuario insertado por correo', user)
                flash('Usuario agregado exitosamente!', 'success')
                return 'Usuario insertado', 200
            else:
                print("El usuario ya existe en la base de datos. No se ha realizado la inserción.")
                flash('El Correo ya existe!', 'danger')
                return 'El usuario ya existe en la base de datos. No se ha realizado la inserción.', 400

        except Exception as e:
            print('Error al insertar usuario por correo', e)
            return 'Error al insertar usuario', 500

        
    def email_login(self, email: str, password: str):
        try:
            # Crear un diccionario con los datos del usuario
            user = {
                'Correo': email,
                'Contrasena': password
            }

            # Obtener la conexión a la base de datos
            conn = self._connection_db_user
            cursor = conn.cursor()

            # Ejecutar una consulta para buscar al usuario por correo
            cursor.execute("SELECT password FROM users WHERE BINARY email = %s", (user['Correo'],))
            result = cursor.fetchone()

            # Cerrar la conexión a la base de datos
            self.cerrar_bd(conn)

            # Verificar si se encontró un usuario y si la contraseña es correcta
            if result:
                stored_password = result[0]
                if stored_password == user['Contrasena']:
                    print('Login exitoso para el usuario:', user['Correo'])
                    return 'Login exitoso', 200
                else:
                    print('Contraseña incorrecta para el usuario:', user['Correo'])
                    return 'Contraseña incorrecta', 401
            else:
                print('Usuario no encontrado:', user['Correo'])
                return 'Usuario no encontrado', 404

        except Exception as e:
            print('Error al intentar iniciar sesión:', e)
            return 'Error al intentar iniciar sesión', 500



    def username_login(self, username: str, password: str):
        try:
            # Crear un diccionario con los datos del usuario
            user = {
                'Username': username,
                'Contrasena': password
            }

            # Obtener la conexión a la base de datos
            conn = self._connection_db_user
            cursor = conn.cursor()

            # Ejecutar una consulta para buscar al usuario por nombre de usuario
            cursor.execute("SELECT password FROM users WHERE username = %s", (user['Username'],))
            result = cursor.fetchone()

            # Cerrar la conexión a la base de datos
            self.cerrar_bd(conn)

            # Verificar si se encontró un usuario y si la contraseña es correcta
            if result:
                stored_password = result[0]
                if stored_password == user['Contrasena']:
                    print('Login exitoso para el usuario:', user['Username'])
                    return 'Login exitoso', 200
                else:
                    print('Contraseña incorrecta para el usuario:', user['Username'])
                    return 'Contraseña incorrecta', 401
            else:
                print('Usuario no encontrado:', user['Username'])
                return 'Usuario no encontrado', 404

        except Exception as e:
            print('Error al intentar iniciar sesión:', e)
            return 'Error al intentar iniciar sesión', 500


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