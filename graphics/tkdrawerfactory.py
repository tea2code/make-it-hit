from . import notdrawableerror
from . import tkcircledrawer
from data import circle

class TkDrawerFactory:
    ''' Factory for tk drawer classes. '''
    
    def createFrom( self, object ):
        ''' Tries to find drawer class for given object. Returns instance of TkDrawer.
        If no drawer is found throws NotDrawableError. '''
        
        # Circle.
        if isinstance( object, circle.Circle ):
            return tkcircledrawer.TkCircleDrawer( object.position.x, object.position.y, object.radius )
            
        # Unknown object. Can not be drawn.
        else:
            raise notdrawableerror.NotDrawableError( 'Not drawable object "{0}".'.format(object) )