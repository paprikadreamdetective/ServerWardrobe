from flask import Blueprint
from controllers.facadeController import index, login

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/login', methods=['POST'])(login)
# blueprint.route('/register', methods=['POST'])(insert)
