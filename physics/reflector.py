from abc import ABCMeta, abstractmethod  

class Reflector(metaclass = ABCMeta):
    ''' Base class for objects which calculate reflection. '''

    @abstractmethod
    def reflect( self, x, y ):
        ''' The derived class must implement this method. Must return the resulting momentum vector.
        Takes the position of the reflection point as argument. '''