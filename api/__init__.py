from flask import Flask
# import firebase_admin
from firebase_admin import credentials, initialize_app
# from .userAPI import userAPI

cred = credentials.Certificate("api/key.json")
default_app = initialize_app(cred, {
    'storageBucket':'db-wardrobe.appspot.com'
    
    })

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345rtfescdvf'

    from .userAPI import userAPI

    app.register_blueprint(userAPI, url_prefix='/user')

    return app