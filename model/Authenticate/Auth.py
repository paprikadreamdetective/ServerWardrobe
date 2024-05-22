import abc 

from services.serviceUser.ProxyUser import ProxyUser
from services.serviceUser.UserCrud import UserCrud
'''
Interfaz que usaran las funcionalidades del
adapter

'''
class Auth(abc.ABC):
    @abc.abstractmethod
    def operation(self):
        pass
'''

class authEmailRegister(Auth):
    def __init__(self, proxy: ProxyUser) -> None:
        
        pass

    def operation(self, email, password, name, lastname):
        print('registro con email')
class authEmail(Auth):
    def __init__(self) -> None:
        
        pass

    def operation(self, email, password):
        print('login con email')

class authUsername(abc.ABC):
    @abc.abstractmethod    
    def loginByUsername(self):
        pass

class authUsernameRegister(abc.ABC):
    @abc.abstractmethod    
    def registerByUsername(self):
        pass

class authAdapter(Auth, authUsername, authUsernameRegister):
    def __init__(self) -> None:
        
        pass

    def operation(self):
        print('login con email o registro con correo')

    def loginByUsername(self, email, password):
        print('Login con username')

    def registerByUsername(self, username, password, name, lastname):
        print('Registro con username')



def auth_email(email: str, password: str):
    return authEmail().operation(email, password)

def register_email(email: str, password: str, name: str, lastname: str):
    return authEmailRegister().operation(email, password, name, lastname)

def auth_username(username: str, password: str):
    return authAdapter().loginByUsername(username, password)

def register_username(username: str, password: str, name: str, lastname: str):
    return authAdapter().registerByUsername(username, password, name, lastname)
    '''