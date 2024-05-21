"""
Adapter Design Pattern

Intent: Provides a unified interface that allows objects with incompatible
interfaces to collaborate.
"""
#authAdapter
from .authByEmail import authEmail
from .authByUsername import authUsername
from .authByEmailRegister import authEmailRegister
from .authByUsernameRegister import authUsernameRegister

from services.serviceUser.ProxyUser import ProxyUser
from services.serviceUser.UserCrud import UserCrud

class Auth(authEmail, authUsername, authEmailRegister, authUsernameRegister):
    def __init__(self):
        self._proxy = ProxyUser(UserCrud())

    """
    The Target defines the domain-specific interface used by the client code.
    """
    def auth(self, email, password):
        return self._proxy.auth(email, password)
        
    def loginByUsername(self, username, password):
        return self._proxy.username_login(username, password)

    def registerByUsername(self, username, pasword, name, lastname):
        return self._proxy.username_register(username, pasword, name, lastname)

    def loginByEmail(self, email, password):
        return self._proxy.email_login(email, password)
        #ProxyUser(UserCrud()).auth(email, password)

    def registerByEmail(self, email, password, name, lastname):
        return self._proxy.email_register(email, password, name, lastname)
        



    '''
    def request(self) -> str:
        return "Target: The default target's behavior."
    '''