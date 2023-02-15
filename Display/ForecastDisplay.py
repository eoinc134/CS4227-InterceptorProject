from Logging.ContextObject import ForecastContext

class ForecastDisplay():
    def __init__(self, weatherData, dispatcher) -> None:
        self.weatherData = weatherData
        self.currentPressure = 0.0
        self.lastPressure = 0.0
        self.dispatcher = dispatcher
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.lastPressure = self.currentPressure
        self.currentPressure = pressure

        
        self.display()

    def display(self):
        forecast = ""

        if(self.currentPressure > self.lastPressure):
            forecast = "Improving weather is on the way!"
        elif(self.currentPressure < self.lastPressure):
            forecast = "Watch out for cooler, rainy weather"
        else:
            forecast = "More of the same"

        self.logUpdate(forecast)
        print("Forecast: {}\n".format(forecast))

    def logUpdate(self, forecast):
        self.dispatcher.dispatch(forecast)