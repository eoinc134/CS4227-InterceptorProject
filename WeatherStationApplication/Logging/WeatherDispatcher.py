from Logging.WeatherContext import WeatherContext

class WeatherDispatcher():
    def __init__(self):
        self.interceptors = []

    def add_interceptor(self, interceptor):
        self.interceptors.append(interceptor)

    def remove_interceptor(self, interceptor):
        i = self.interceptors.index(interceptor)
        if(i >= 0):
            self.interceptors.remove(interceptor)

    def update(self, update):
        context = WeatherContext(update)
        for interceptor in self.interceptors:
            interceptor.update(context)