from .UserServices import UserServices

class ProxyUser(UserServices):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def email_login(self, username: str, password: str):
        return self._real_subject.auth(username, password)
    
    def username_login(self, username: str, password: str):
        return self._real_subject.auth(username, password)
    
    def email_register(self, email: str, name: str, lastname: str, password: str):
        return self._real_subject.auth(email, password, name, lastname)

    def user_register(self, username: str, name: str, lastname: str, password: str):
        return self._real_subject.auth(username, password, name, lastname)
     
     
    
     
        # ...
        #if self._real_subject.auth(username, password):
        #    print("Successful")
        #else:
        #    print("Not Successful")
        # ...
