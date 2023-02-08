class CurrentConditionsDisplay():
    def __init__(self, weatherData) -> None:
        self.weatherData = weatherData
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Temperature: {}C \nHumidity: {}%".format(self.temperature, self.humidity))
