from .UserCrud import UserCrud
from .ProxyUser import ProxyUser


def user_auth(username: str, password: str):
    return ProxyUser(UserCrud()).auth(username, password)
    #proxy = ProxyUser(UserCrud())
    #proxy.auth(username, password)
