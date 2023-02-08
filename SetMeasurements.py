import abc

class SetMeasurements(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'setMeasurements')
                and callable(subclass.setMeasurements))