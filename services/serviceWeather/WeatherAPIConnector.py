from WeatherService import WeatherService
import requests
class WeatherAPI(WeatherService):
    def __init__(self) -> None:
        self._API_KEY = "de5592c2993d510b9e18d50fc4b37211"
        self._BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def get_current_weather(self, city: str):
        try:
            response = requests.get(self._BASE_URL, params={
                'q': city,
                'appid': self._API_KEY,
                'units': 'metric'  
            })
            response.raise_for_status()
            data = response.json()
            return { 'city': data['name'], 'temperature': data['main']['temp'] }
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}