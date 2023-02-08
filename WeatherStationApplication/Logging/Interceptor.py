import abc

class Interceptor(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'updateLog') and callable(subclass.updateLog))