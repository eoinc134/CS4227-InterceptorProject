class WeatherContext:
   def __init__(self, update):
        self.update = update

   def getWeatherContext(self):
      return self.update


class ForecastContext:
   def __init__(self, forecast) -> None:
       self.update = forecast

   def getForecastContext(self):
      return self.update