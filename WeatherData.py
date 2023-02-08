import Observer

class WeatherData():
    
    def __init__(self) -> None:
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        i = self.observers.index(observer)
        if(i >= 0):
            self.observers.remove(observer)

    def notifyObservers(self):
        for x in self.observers:
            x.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure