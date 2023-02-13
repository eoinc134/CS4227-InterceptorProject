import abc

class DisplayElement(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'display')
                and callable(subclass.display))