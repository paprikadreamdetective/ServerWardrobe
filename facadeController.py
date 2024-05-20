#from models.
# ControladorAuth
import os
from app import app 
from flask import request, jsonify

from models.Authenticate.authManager import user_auth
from models.CaptureClothe.imageManager import sendPictureToPI
from models.CreateOutfit.cliente import create_outfit


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
 
@app.route('/create_outfit', methods=['POST'])
def createOutfit():
    create_outfit()

@app.route('/get_clothe', methods=['GET'])
def get_clothe():
    pass

@app.route('/register', methods=['POST'])
def register():
    pass
