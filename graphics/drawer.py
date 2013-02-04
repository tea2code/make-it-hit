from abc import ABCMeta, abstractmethod  

class Drawer(metaclass = ABCMeta):
    ''' Base class for objects which can draw something. '''
    
    @abstractmethod
    def draw( self, canvas ):
        ''' The derived class must implement this method. Receives the canvas to draw on. '''