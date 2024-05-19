from .authAdapter import Auth
#from serviceUser.ProxyUser import ProxyUser
#from serviceUser.UserCrud import UserCrud


def user_auth(email: str, password: str):
    return Auth().loginByEmail(email, password)
    #auth = Auth()
    #auth.loginByEmail(email, password)
    #return ProxyUser(UserCrud()).auth(username, password)
    #proxy = ProxyUser(UserCrud())
    #proxy.auth(username, password)
