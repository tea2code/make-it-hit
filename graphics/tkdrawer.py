from abc import ABCMeta, abstractmethod  
from formulary import screenconvert

class TkDrawer(metaclass = ABCMeta):
    ''' Base class for objects which can draw something using tk. 
    
    Member:
    color -- The color of the line (string).
    fill -- The fill color (string).
    line -- The line width (float).
    screenXCoefficient -- Coefficient for world to screen conversion in x direction (float).
    screenYCoefficient -- Coefficient for world to screen conversion in y direction (float).
    '''
    
    def __init__( self ):
        self.color = 'black'
        self.fill = ''
        self.line = 1
        self.screenXCoefficient = 1
        self.screenYCoefficient = 1
    
    @abstractmethod
    def draw( self, canvas ):
        ''' The derived class must implement this method. Receives the canvas to draw on. '''
        
    def worldToScreenX( self, x ):
        ''' Converts world x to screen x coordinate. '''
        return screenconvert.worldToScreen( x, self.screenXCoefficient )
    
    def worldToScreenY( self, y ):
        ''' Converts world y to screen y coordinate. '''
        return screenconvert.worldToScreen( y, self.screenYCoefficient )