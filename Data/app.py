import os, sys
from WeatherData import WeatherData

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
if rootDir not in sys.path:  # add parent dir to paths
    sys.path.append(rootDir)

from Display.CurrentConditionsDisplay import CurrentConditionsDisplay 
from Display.StatisticsDisplay import StatisticsDisplay 
from Display.ForecastDisplay import ForecastDisplay

from Logging.WeatherDispatcher import WeatherDispatcher
from Logging.Interceptor import WeatherUpdateInterceptor


class WeaterStation:
    def main():
        dispatcher = WeatherDispatcher()
        dispatcher.add_interceptor(WeatherUpdateInterceptor())

        weatherData = WeatherData(dispatcher)

        currentConditionsDisplay = CurrentConditionsDisplay(weatherData)
        statisticsDisplay = StatisticsDisplay(weatherData)
        forecastDisplay = ForecastDisplay(weatherData)

        weatherData.setMeasurements(80, 65, 30.4)
        weatherData.setMeasurements(82, 70, 29.2)
        weatherData.setMeasurements(78, 90, 29.2)

        return "hello"

    if __name__ == "__main__":
        main()