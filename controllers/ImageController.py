import os
from app import app 
from flask import request, jsonify
from models.CaptureClothe.imageManager import sendPictureToPI

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
RASPBERRY_PI_SERVER_URL = 'http://192.168.10.94:8008/receive_image'

@app.route('/upload_picture', methods=['POST'])
def upload_picture():
    global RASPBERRRY_PI_SERVER_URL
    picture = request.files['file']
    if picture:
        file_path = os.path.join('uploads', picture.filename)
        picture.save(file_path)
        
        # Leer la imagen guardada y enviarla al servidor en la Raspberry Pi
        
        with open(file_path, 'rb') as image_file:
            files = {'file': (picture.filename, image_file, picture.content_type)}
            response = request.post(RASPBERRY_PI_SERVER_URL, files=files)
        
        # Verificar la respuesta del servidor en la Raspberry Pi
        if response.status_code == 200:
            return jsonify({"message": "Image received and forwarded successfully!", "file_path": file_path})
        else:
            return jsonify({"message": "Image received but failed to forward", "error": response.text}), 500

    return jsonify({"message": "No file received"}), 400
        
'''    
  

