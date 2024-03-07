import os
import firebase_admin
from firebase_admin import credentials, storage, firestore
from flask import Flask, render_template, request, jsonify, Blueprint
from PIL import Image
from rembg import remove
import uuid


# from app import app
db = firestore.client()
user_ref = db.collection('ropa')

userAPI = Blueprint('userAPI', __name__)


# Configuración de Firebase Admin SDK
# cred = credentials.Certificate("app/key.json")
# firebase_admin.initialize_app(cred, {'storageBucket': 'tu-storage-bucket'})

UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def remove_background(input_path, output_folder):
    # Abrir la imagen
    imagen = Image.open(input_path)

    # Convertir la imagen a formato RGBA (si no lo es ya)
    imagen = imagen.convert("RGBA")

    #removerfondo
    imagen = remove(imagen)

    # Obtener los píxeles de la imagen
    datos = imagen.getdata()

    # Crear una nueva lista de píxeles con fondo transparente
    nuevos_datos = []
    for item in datos:
        # Si el píxel es blanco (fondo), hacerlo transparente
        if item[:3] == (255, 255, 255):
            nuevos_datos.append((255, 255, 255, 0))  # Transparente
        else:
            nuevos_datos.append(item)

    # Actualizar los datos de la imagen
    imagen.putdata(nuevos_datos)

    # Generar un nombre de archivo único para la imagen de salida
    output_filename = str(uuid.uuid4()) + ".png"
    output_path = os.path.join(output_folder, output_filename)

    # Guardar la imagen como PNG con fondo transparente
    imagen.save(output_path, "PNG")

    print('En la función el valor que devuelve es: ', output_path)

    return output_path, output_filename


@userAPI.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    print('Haciendo la actualización')

    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)
    [path_new, new_name] = remove_background(filename, PROCESSED_FOLDER)
    print('Despues de la funcion filename = ', filename)

    # Subir la imagen procesada a Storage
    processed_filename = os.path.basename(new_name)
    processed_filepath = os.path.join(PROCESSED_FOLDER, processed_filename)

    bucket = storage.bucket()
    print(f"processed_filename: {processed_filename}")
    print('Variable processed_filepath = ', processed_filepath)

    blob = bucket.blob(processed_filename)
    blob.upload_from_filename(processed_filepath)
    # Generar la URL de acceso a la imagen
    image_url = blob.public_url
    print(f"URL generada: {image_url}")


    return jsonify({'message': 'File uploaded successfully', 'image_url': image_url})


@userAPI.route('/upload', methods=['GET'])
def get_upload():
    return jsonify({"msg": "received"})
