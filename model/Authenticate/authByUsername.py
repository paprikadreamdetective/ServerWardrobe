import abc

class authUsername(abc.ABC):
    @abc.abstractmethod
    def loginByUsername(self, username, password):
        pass
    @abc.abstractmethod
    def registerByUsername(self, username, password, name, lastname):
        pass
    '''
    def __init__(self, username, password) -> None:
        self._username = username
        self._password = password
    def loginByUsername(self, username, password):
        print("Iniciando sesion con username")
    def registerByUsername(self, username, password):
        print("Registrando con username")
    '''