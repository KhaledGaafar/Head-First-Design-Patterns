from abc import ABC, abstractmethod
from typing import List
from observers import IObserver

class ISubject(ABC):

    @abstractmethod
    def register_observer(self, o: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, o: IObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class WeatherData(ISubject):

    def __init__(self, observers: List[IObserver] = None):
        self.observers: List[IObserver] = observers if observers is not None else []
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0

    def register_observer(self, o: IObserver):
        if o not in self.observers:
            self.observers.append(o)

    def remove_observer(self, o: IObserver):
        if o in self.observers:
            self.observers.remove(o)

    def notify_observers(self):
        for o in self.observers:
            o.update()

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()
