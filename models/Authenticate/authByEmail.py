import abc

class authEmail(abc.ABC):
    @abc.abstractmethod
    def loginByEmail(self, email, password):
        pass
    @abc.abstractmethod
    def registerByEmail(self, email, password, name, lastname):
        pass
    
    '''
    def __init__(self, email, password) -> None:
        self._email = email
        self._password = password
    def loginByEmail(self, email, password):
        print("Iniciando sesion con correo electronico")
    def registerByEmail(self, email, password):
        print("Registrando con correo electronico")
    '''