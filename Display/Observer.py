import abc

class Observer(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'update')
                and callable(subclass.update))
