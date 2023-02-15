from abc import ABC, abstractmethod
from Logging.ContextObject import WeatherContext, ForecastContext


class Dispatcher(ABC):
    def add_interceptor(self, interceptor):
        self.interceptors.append(interceptor)

    def remove_interceptor(self, interceptor):
        i = self.interceptors.index(interceptor)
        if(i >= 0):
            self.interceptors.remove(interceptor)


class WeatherDispatcher(Dispatcher):
    def __init__(self):
        self.interceptors = []

    def dispatch(self, context: WeatherContext):
        for interceptor in self.interceptors:
            interceptor.update(WeatherContext(context))


class ForecastDispatcher(Dispatcher):
    def __init__(self):
        self.interceptors = []

    def dispatch(self, context: ForecastContext):
        for interceptor in self.interceptors:
            interceptor.update(ForecastContext(context))