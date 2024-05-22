import abc
from .Auth import Auth
from services.serviceUser.ProxyUser import ProxyUser
class authEmail(Auth):
    def __init__(self, proxy: ProxyUser) -> None:
        '''
            Aqui va el proxy
        '''
        self._proxy = proxy 
    '''
    Funcion encargada de autentitifcar la cuenta del usuario 
    con correo electronico y contraseña
    '''
    def operation(self, email, password):
        return self._proxy.email_login(email, password)

    
    '''
    def __init__(self, email, password) -> None:
        self._email = email
        self._password = password
    def loginByEmail(self, email, password):
        print("Iniciando sesion con correo electronico")
    def registerByEmail(self, email, password):
        print("Registrando con correo electronico")
    '''