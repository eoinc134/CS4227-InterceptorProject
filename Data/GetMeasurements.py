import abc

class GetMeasurements(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'getTemperature') and callable(subclass.getTemperature) and
                hasattr(subclass, 'getHumidity') and callable(subclass.getHumidity) and
                hasattr(subclass, 'getPressure') and callable(subclass.getPressure))