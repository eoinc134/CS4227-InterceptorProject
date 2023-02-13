from abc import ABC, abstractmethod

class Interceptor(ABC):
    @abstractmethod
    def update(self, context):
        pass

class WeatherUpdateInterceptor(Interceptor):
    def update(self, context):
        print("Weather has been updated:\n {}".format(context.update))