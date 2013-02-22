from abc import ABCMeta, abstractmethod  

class Collider(metaclass = ABCMeta):
    ''' Base class for objects which calculate collision. '''

    @abstractmethod
    def collide( self ):
        ''' The derived class must implement this method. '''