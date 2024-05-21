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
                'units': 'metric'  # Opcional: para obtener la temperatura en Celsius
            })
            response.raise_for_status()
            data = response.json()
            
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather_info

        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

if __name__ == '__main__':
    city = input("Ingrese el nombre de la ciudad: ")
    weather = WeatherAPI().get_current_weather(city)
    if 'error' in weather:
        print(f"Error al obtener el clima: {weather['error']}")
    else:
        print(f"Clima en {weather['city']}:")
        print(f"Temperatura: {weather['temperature']}°C")
        print(f"Descripción: {weather['description']}")
        print(f"Humedad: {weather['humidity']}%")
        print(f"Velocidad del viento: {weather['wind_speed']} m/s")