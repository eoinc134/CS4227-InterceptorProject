from WeatherData import WeatherData
from CurrentConditionsDisplay import CurrentConditionsDisplay 
from StatisticsDisplay import StatisticsDisplay 
from ForecastDisplay import ForecastDisplay

class WeaterStation:
    def main():
        weatherData = WeatherData()

        currentConditionsDisplay = CurrentConditionsDisplay(weatherData)
        statisticsDisplay = StatisticsDisplay(weatherData)
        forecastDisplay = ForecastDisplay(weatherData)

        weatherData.setMeasurements(80, 65, 30.4)
        weatherData.setMeasurements(82, 70, 29.2)
        weatherData.setMeasurements(78, 90, 29.2)

    if __name__ == "__main__":
        main()