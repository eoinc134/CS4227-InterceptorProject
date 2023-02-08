import abc

class Subject(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'registerObserver') and callable(subclass.registerObserver) and
                hasattr(subclass, 'removeObserver') and callable(subclass.removeObserver) and
                hasattr(subclass, 'notifyObserver') and callable(subclass.notifyObserver))