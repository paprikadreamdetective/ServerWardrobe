from .UserServices import UserServices
"""
    In this script we are going to call
    the sql sentences for the db

"""

class UserCrud(UserServices):
    """
    Define the real object that the proxy represents.
    """
    def auth(self, username: str, password: str) -> bool:
        if username == 'user' and password == '123':
            return True
        else:
            return False
        
