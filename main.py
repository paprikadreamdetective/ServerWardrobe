
from api import create_app, userAPI
from flask_cors import CORS

app = create_app()

CORS(app)

# app.register_blueprint(userAPI, url_prefix='/user')


if __name__ == '__main__':
    app.run(debug=True)