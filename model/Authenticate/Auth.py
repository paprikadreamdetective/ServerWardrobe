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
