from abc import ABC, abstractmethod

# Funciones de utilidad para calcular diferencias de colores y encontrar colores coincidentes


def calculate_color_difference(color1, color2):
    return sum(abs(component1 - component2) for component1, component2 in zip(color1, color2))


def color_combines(color_base, color_to_compare, tolerance):
    difference = calculate_color_difference(color_base, color_to_compare)
    return difference <= tolerance


def matching_colors(selected_color, color_list, tolerance):
    matching_colors = []
    for color in color_list:
        if color_combines(selected_color, color, tolerance):
            matching_colors.append(color)
    return matching_colors

# Productos abstractos


class Outfit(ABC):
    @abstractmethod
    def create_outfit(self) -> str:
        pass

# Productos concretos


class ColdCloudyOutfit(Outfit):
    def create_outfit(self) -> str:
        return "Cold and cloudy outfit"


class ColdSunnyOutfit(Outfit):
    def create_outfit(self) -> str:
        return "Cold and sunny outfit"


class SunnyFreshOutfit(Outfit):
    def create_outfit(self) -> str:
        return "Sunny and fresh outfit"


class SunnyHotOutfit(Outfit):
    def create_outfit(self) -> str:
        return "Sunny and hot outfit"

# Fábrica abstracta


class OutfitFactory(ABC):
    @abstractmethod
    def create_outfit(self, image_path: str) -> tuple:
        pass

# Proxy del servicio climático


class WeatherServiceProxy:
    def get_weather(self, location: str) -> dict:
        # Aquí iría la lógica para obtener la información climática
        # Por simplicidad, solo retornaremos un valor predefinido
        return {'color_predominant': (100, 50, 30)}

# Fábrica concreta


class WeatherBasedOutfitFactory(OutfitFactory):
    def create_outfit(self, color_clothe) -> tuple:
        # color_clothe = self.recognize_predominant_color(image_path)
        weather_info = self.weather_service_proxy.get_weather(location)
            color_predominant = weather_info.get('color_predominant')
        matching_bottom_colors = matching_colors(
            color_clothe, self.bottom_color_list, self.tolerance)
        matching_top_colors = matching_colors(
            color_clothe, self.top_color_list, self.tolerance)
        matching_shoes_colors = matching_colors(
            color_clothe, self.shoes_color_list, self.tolerance)

        # Encontrar una combinación de colores que se encuentre en todas las listas
        for color in matching_bottom_colors:
            if color in matching_top_colors and color in matching_shoes_colors:
                return color, color, color

        # Si no se encuentra una combinación, devolver None para todas las prendas
        return None, None, None

    def __init__(self, weather_service_proxy, bottom_color_list, top_color_list, shoes_color_list, tolerance):
        self.weather_service_proxy = weather_service_proxy
        self.bottom_color_list = bottom_color_list
        self.top_color_list = top_color_list
        self.shoes_color_list = shoes_color_list
        self.tolerance = tolerance

# Cliente


def client_code(factory: OutfitFactory, color_predominant: tuple) -> None:
    top, bottom, shoes = factory.create_outfit(color_predominant)
    if top and bottom and shoes:
        print(f"Outfit recommendation:\nTop: {
              top}\nBottom: {bottom}\nShoes: {shoes}")
    else:
        print("No matching outfit found for the given image.")


# ejemplo de uso
if __name__ == "__main__":
    # Supongamos que tienes listas de colores separadas para diferentes prendas
    bottom_color_list = [
        (100, 50, 30),
        (110, 60, 40),
        (90, 40, 20),
        (140, 80, 50),
        (40, 80, 40),
        (20, 45, 78)
    ]

    top_color_list = [
        (100, 50, 30),
        (120, 70, 40),
        (90, 40, 20),
        (140, 80, 50),
        (31, 60, 40),
        (20, 45, 78)
    ]

    shoes_color_list = [
        (100, 50, 30),
        (100, 40, 40),
        (90, 40, 20),
        (140, 80, 50),
        (31, 41, 71),
        (20, 45, 78)
    ]

    # Define una tolerancia
    tolerance = 50  # Puedes ajustar este valor según tus necesidades
    # Crear una instancia del proxy del servicio climático
    weather_service_proxy = WeatherServiceProxy()


    factory = WeatherBasedOutfitFactory(
        weather_service_proxy,
        bottom_color_list,
        top_color_list,
        shoes_color_list,
        tolerance
    )
    
    image_path = "images/outputs/out.png"

    color_predominant = (100, 50, 30)
  
    location = "CDMX"

    # client_code(factory, color_predominant, location)
