from abc import ABC, abstractmethod
from Logging.ContextObject import WeatherContext, ForecastContext

class Interceptor(ABC):
    @abstractmethod
    def update(self, context):
        pass

class WeatherUpdateInterceptor(Interceptor):
    def update(self, context: WeatherContext):
        print("::LOG::Weather has been updated\n {}".format(context.getWeatherContext()))

class ForecastInterceptor(Interceptor):
    def update(self, context: ForecastContext):
        print("::LOG::Forecast changed -> {}".format(context.getForecastContext()))