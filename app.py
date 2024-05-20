from controllers.ImageController import *
from controllers.AuthController import *
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)  # flask app object
    CORS(app)
    return app


app = create_app()  # Creating the app

if __name__ == '__main__':  # Running the app
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(host='127.0.0.1', port=5000, debug=True)
