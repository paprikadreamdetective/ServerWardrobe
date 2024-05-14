from UserCrud import UserCrud
from ProxyUser import ProxyUser


proxy = ProxyUser(UserCrud())
proxy.auth("user", "123")
