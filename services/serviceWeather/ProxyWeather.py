from .WeatherService import WeatherService

class ProxyWeather(WeatherService):
    """
    Clase Proxy para WeatherService.
    """
    def __init__(self, real_service):
        self._real_service = real_service

    def get_current_weather(self, location):
        # se llama al servicio de clima
        return self._real_service.get_current_weather(location)
