import os
from flask import request, jsonify
from app import app
from model.Authenticate.authManager import user_auth_email, user_register_email, user_auth_username,user_register_username
from model.CaptureClothe.imageManager import sendPictureToPI
from model.Weather.weatherManager import getCurrentWeather
from model.CreateOutfit.gestorConjunto import create_outfit
from model.Wardrobe.wardrobeManager import add_outfit
from model.generateOutfit.generateOutfit import GenerateOutfit

@app.route('/login_email', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    print("Recv data: " + str(email) + " : " + str(password))
    result, status_code = user_auth_email(email, password)
    if status_code == 200:
        print("Datos correctos")
        return jsonify({'success': 200, 'message': result}), status_code
    else:
        print("Datos incorrectos")
        return jsonify({'success': status_code, 'message': result}), status_code

@app.route('/register_email', methods=['POST'])
def register_email():
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']
    lastname = request.json['lastname']
    print("Recv data: " + str(email) + " : " + str(password) + " : " + str(name) + " : " + str(lastname))
    if user_register_email(email, password, name, lastname):
        print("Datos correctos")
        return jsonify({'success': 200, 'message': 'Login successful'})
    else:
        print("Datos incorrectos")
        return jsonify({'success': 500, 'message': 'Invalid credentials'})

@app.route('/login_username', methods=['POST'])
def login_username():
    username = request.json['username']
    password = request.json['password']
    print("Recv data: " + str(username) + " : " + str(password))
    result, status_code = user_auth_username(username, password)
    if status_code == 200:
        print("Datos correctos")
        return jsonify({'success': 200, 'message': 'Login successful'})
    else:
        print("Datos incorrectos")
        return jsonify({'success': status_code, 'message': result}), status_code

@app.route('/register_username', methods=['POST'])
def register_username():
    print('ENTRA AL facade')
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    lastname = request.json['lastname']
    print("Recv data: " + str(username) + " : " + str(password) + " : " + str(name) + " : " + str(lastname))
    if user_register_username(username, password, name, lastname):
        print("Datos correctos")
        return jsonify({'success': 200, 'message': 'Register successful'})
    else:
        print("Datos incorrectos")
        return jsonify({'error': 500, 'message': 'Invalid register'})


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

@app.route('/get_current_weather', methods=['GET'])
def get_current_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400
    weather_info = getCurrentWeather(city)
    if 'error' in weather_info:
        return jsonify(weather_info), 500
    return jsonify(weather_info)

@app.route('/create_manual_outfit', methods=['POST'])
def create_manual_outfit():
    create_outfit()

@app.route('/create_automatic_outfit', methods=['POST'])
def generate_outfit():
    controller = GenerateOutfit()
    controller.operation()

@app.route('/add_outfit', methods=['POST'])
def add_outfit():
    add_outfit(request.json['type outfit'])
