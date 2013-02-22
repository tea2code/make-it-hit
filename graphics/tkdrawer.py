from abc import ABCMeta, abstractmethod  

class TkDrawer(metaclass = ABCMeta):
    ''' Base class for objects which can draw something using tk. 
    
    Member:
    color -- The color of the line (string).
    fill -- The fill color (string).
    line -- The line width (float).
    '''
    
    color = 'black'
    fill = ''
    line = 1
    
    @abstractmethod
    def draw( self, canvas ):
        ''' The derived class must implement this method. Receives the canvas to draw on. '''