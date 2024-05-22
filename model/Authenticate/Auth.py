import abc 
'''
Interfaz que usaran las funcionalidades del
adapter

'''
class Auth(abc.ABC):
    @abc.abstractmethod
    def operation(self):
        pass
'''
registro correo
'''
class authEmailRegister(Auth):
    def __init__(self) -> None:
        '''
        Aqui iria el proxy 
        '''
        pass

    def operation(self, email, password, name, lastname):
        print('registro con email')
'''
login correo
'''
class authEmail(Auth):
    def __init__(self) -> None:
        '''
        Aqui iria el proxy 
        '''
        pass

    def operation(self, email, password):
        print('login con email')
'''
interface login usuario
'''
class authUsername(abc.ABC):
    @abc.abstractmethod    
    def loginByUsername(self):
        pass
'''
interface registro usuario
'''
class authUsernameRegister(abc.ABC):
    @abc.abstractmethod    
    def registerByUsername(self):
        pass
'''
registro extra
'''
class authAdapter(Auth, authUsername, authUsernameRegister):
    def __init__(self) -> None:
        '''
        Aqui iria el proxy 
        '''
        pass

    def operation(self):
        print('login con email o registro con correo')

    def loginByUsername(self, email, password):
        print('Login con username')

    def registerByUsername(self, username, password, name, lastname):
        print('Registro con username')


'''
client: authManager.py


'''

def auth_email(email: str, password: str):
    return authEmail().operation(email, password)

def register_email(email: str, password: str, name: str, lastname: str):
    return authEmailRegister().operacion(email, password, name, lastname)

def auth_username(username: str, password: str):
    return authAdapter().loginByUsername(username, password)

def register_username(username: str, password: str, name: str, lastname: str):
    return authAdapter().registerByUsername(username, password, name, lastname)