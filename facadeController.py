#from models.

from app import app 
from flask import request, jsonify

from services.userServices.UserManager import user_auth 

#def index():
#    return {'status': 'OK',
#            'localhost:5000/ctrl/login':'user login'}


@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    if user_auth(email, password):
        print("Datos correctos")
    else:
        print("Datos incorrectos")


