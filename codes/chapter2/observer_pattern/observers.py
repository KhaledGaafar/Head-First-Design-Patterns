from abc import ABC, abstractmethod
from displaying import IDisplayElement

class IObserver(ABC):

    @abstractmethod
    def update(self):
        pass


class CurrentConditionsDisplay(IObserver, IDisplayElement):

    def __init__(self, weather_data):
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self):
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.display()  # Corrected from display() to self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}°C and {self.humidity}% humidity")