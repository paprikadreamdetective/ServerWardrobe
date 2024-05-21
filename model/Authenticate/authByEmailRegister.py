import abc

class authEmailRegister(abc.ABC):
    @abc.abstractmethod
    def registerByEmail(self, email, password, name, lastname):
        pass