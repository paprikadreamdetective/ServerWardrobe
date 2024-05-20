import abc

class WeatherService(metaclass=abc.ABCMeta):
    """
    Define the common interface for RealSubject and Proxy so that a
    Proxy can be used anywhere a RealSubject is expected.
    """
    @abc.abstractmethod
    def get_current_weather(self):
        pass
    