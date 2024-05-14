from UserServices import UserServices

class ProxyUser(UserServices):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def auth(self, username: str, password: str):
        # ...
        if self._real_subject.auth(username, password):
            print("Successful")
        else:
            print("Not Successful")
        # ...
