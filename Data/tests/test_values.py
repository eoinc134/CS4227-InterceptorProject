from .. import WeatherData, app
from Display.CurrentConditionsDisplay import CurrentConditionsDisplay
from Logging.Interceptor import WeatherUpdateInterceptor
from Logging.Dispatcher import WeatherDispatcher

#######
#SETUP#
#######
dispatcher = WeatherDispatcher()
dispatcher.add_interceptor(WeatherUpdateInterceptor())

weatherData = WeatherData.WeatherData(dispatcher)
currentConditionsDisplay = CurrentConditionsDisplay(weatherData)

weatherData.setMeasurements(80, 65, 30.4)


#######
#TESTS#
#######
def test_temperature():
    assert weatherData.getTemperature() == 80

def test_humidity():
    assert weatherData.getHumidity() == 65

def test_pressure():
    assert weatherData.getPressure() == 30.4