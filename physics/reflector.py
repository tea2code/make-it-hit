from abc import ABCMeta, abstractmethod  

class Reflector(metaclass = ABCMeta):
    ''' Base class for objects which calculate reflection. '''

    @abstractmethod
    def reflect( self ):
        ''' The derived class must implement this method. Must return the resulting momentum vector.'''