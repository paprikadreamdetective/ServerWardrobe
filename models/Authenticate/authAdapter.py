"""
Adapter Design Pattern

Intent: Provides a unified interface that allows objects with incompatible
interfaces to collaborate.
"""
from .authByEmail import authEmail
from .authByUsername import authUsername

from serviceUser.ProxyUser import ProxyUser
from serviceUser.UserCrud import UserCrud

class Auth(authEmail, authUsername):
    def __init__(self):
        self._proxy = ProxyUser(UserCrud())
    """
    The Target defines the domain-specific interface used by the client code.
    """
    def loginByEmail(self, email, password):
        self._proxy.auth(email, password)
        #ProxyUser(UserCrud()).auth(email, password)
        


    '''

    def request(self) -> str:
        return "Target: The default target's behavior."
    '''