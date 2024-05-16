class authEmail:
    def __init__(self, email, password) -> None:
        self._email = email
        self._password = password
    def loginByEmail(self, email, password):
        print("Iniciando sesion con correo electronico")
    def registerByEmail(self, email, password):
        print("Registrando con correo electronico")