from .authAdapter import Auth
#from serviceUser.ProxyUser import ProxyUser
#from serviceUser.UserCrud import UserCrud

def user_auth(email: str, password: str):
    return Auth().auth(email, password)

def user_auth_email(email: str, password: str):
    return Auth().loginByEmail(email, password)

def user_auth_username(username: str, password: str):
    return Auth().loginByUsername(username, password)

def user_register_email(email: str, password: str, name: str, lastname: str):
    return Auth().registerByEmail(email, password, name, lastname)

def user_register_username(username: str, password: str, name: str, lastname: str):
    return Auth().registerByUsername(username, password, name, lastname)
    
    
    
    #auth = Auth()
    #auth.loginByEmail(email, password)
    #return ProxyUser(UserCrud()).auth(username, password)
    #proxy = ProxyUser(UserCrud())
    #proxy.auth(username, password)
