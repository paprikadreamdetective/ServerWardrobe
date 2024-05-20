#from models.
# ControladorAuth
import os
from app import app 
from flask import request, jsonify

from model.Authenticate.authManager import user_auth, user_register_email, user_auth_username,user_register_username
from model.CaptureClothe.imageManager import sendPictureToPI
# from model.CreateOutfit.cliente import create_outfit


@app.route('/login_email', methods=['POST'])
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

@app.route('/register_email', methods=['POST'])
def register_email():
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']
    lastname = request.json['lastname']
    print("Recv data: " + str(email) + " : " + str(password) + " : " + str(name) + " : " + str(lastname))
    if user_register_email(email, password, name, lastname):
        print("Datos correctos")
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        print("Datos incorrectos")
        return jsonify({'success': False, 'message': 'Invalid credentials'})

@app.route('/login_username', methods=['POST'])
def login_username():
    username = request.json['username']
    password = request.json['password']
    print("Recv data: " + str(username) + " : " + str(password))
    if user_auth_username(username, password):
        print("Datos correctos")
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        print("Datos incorrectos")
        return jsonify({'success': False, 'message': 'Invalid credentials'})

@app.route('/register_username', methods=['POST'])
def register_username():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    lastname = request.json['lastname']
    print("Recv data: " + str(username) + " : " + str(password) + " : " + str(name) + " : " + str(lastname))
    if user_register_username(username, password, name, lastname):
        print("Datos correctos")
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        print("Datos incorrectos")
        return jsonify({'success': False, 'message': 'Invalid credentials'})


@app.route('/upload_picture', methods=['POST'])
def upload_picture():
    picture = request.files['file']
    if picture:
        file_path = os.path.join('uploads', picture.filename)
        picture.save(file_path)
        if sendPictureToPI(file_path, picture):
            return jsonify({"message": "Image received and forwarded successfully!", "file_path": file_path})
        else:
            return jsonify({"message": "Image received but failed to forward", "error": "ERROR"}), 500
    return jsonify({"message": "No file received"}), 400
 

'''
@app.route('/create_manual_outfit', methods=['POST'])
def create_manual_outfit():
    create_outfit()

@app.route('/create_automatic_outfit', methods=['POST'])
def generate_outfit():
    pass

@app.route('/get_clothe', methods=['GET'])
def get_clothe():
    pass

@app.route('/register', methods=['POST'])
def register():
    pass

@app.route('/get_current_weather', methods=['GET'])
def get_current_weather():
    pass
'''