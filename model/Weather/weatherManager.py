from services.serviceWeather.ProxyWeather import ProxyWeather
from services.serviceWeather.WeatherAPIConnector import WeatherAPI


def getCurrentWeather(city: str):
    return ProxyWeather(WeatherAPI()).get_current_weather(city)