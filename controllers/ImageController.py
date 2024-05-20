import requests
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

