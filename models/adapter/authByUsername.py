class authUsername:
    def __init__(self, email, password) -> None:
        self._email = email
        self._password = password
    def loginByUsername(self, email, password):
        print("Iniciando sesion con username")
    def registerByUsername(self, email, password):
        print("Registrando con username")