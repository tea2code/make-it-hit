from . import notdrawableerror
from . import tkcircledrawer
from . import tkrectdrawer
from data import circle
from data import rect

class TkDrawerFactory:
    ''' Factory for tk drawer classes. '''
    
    def createFrom( self, object ):
        ''' Tries to find drawer class for given object. Returns instance of TkDrawer.
        If no drawer is found throws NotDrawableError. '''
        
        # Circle.
        if isinstance( object, circle.Circle ):
            return tkcircledrawer.TkCircleDrawer( object.radius, object.position.x, object.position.y )
        
        # Rectangle.
        elif isinstance( object, rect.Rect ):
            return tkrectdrawer.TkRectDrawer( object.angle, object.height, object.width, 
                                              object.position.x, object.position.y )
        
        # Unknown object. Can not be drawn.
        else:
            raise notdrawableerror.NotDrawableError( 'Not drawable object "{0}".'.format(object) )