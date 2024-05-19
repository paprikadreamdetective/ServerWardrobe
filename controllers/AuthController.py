#from models.

from app import app 
from flask import request, jsonify

from models.Authenticate.authManager import user_auth
#from services.userServices.UserManager import user_auth 

#def index():
#    return {'status': 'OK',
#            'localhost:5000/ctrl/login':'user login'}


@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    print("Recv data: " + str(email) + " : " + str(password))
    if user_auth(email, password):
        print("Datos correctos")
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        print("Datos incorrectos")
        return jsonify({'success': False, 'message': 'Invalid credentials'})


