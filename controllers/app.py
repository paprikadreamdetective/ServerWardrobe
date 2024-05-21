# app.py
from flask import Flask

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Importa las rutas después de crear la aplicación
import facadeController

if __name__ == '__main__':
    app.run(debug=True)
