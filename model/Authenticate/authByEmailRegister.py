import abc
from .Auth import Auth
from services.serviceUser.ProxyUser import ProxyUser
class authEmailRegister(Auth):
    def __init__(self, proxy: ProxyUser) -> None:
        '''
            Aqui va el proxy
        '''
        self._proxy = proxy 
    '''
    Funcion encargada de registrar una cuenta del usuario 
    con correo electronico, contraseña, nombre, apellido
    '''
    def operation(self, email, password, name, lastname):
        return self._proxy.email_register(email, password, name, lastname)