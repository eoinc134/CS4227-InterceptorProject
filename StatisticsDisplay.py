class StatisticsDisplay():
    def __init__(self, weatherData) -> None:
        self.weatherData = weatherData
        self.maxTemp = 0.0
        self.minTemp = 200
        self.tempSum = 0.0
        self.numReadings = 0
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.tempSum += temperature
        self.numReadings += 1

        if(temperature > self.maxTemp):
            self.maxTemp = temperature

        if(temperature < self.minTemp):
            self.minTemp = temperature

        self.display()

    def display(self):
        avgTemp = self.tempSum / self.numReadings
        print("Avg/Max/Min Temperature: {}/{}/{}".format(avgTemp, self.maxTemp, self.minTemp))