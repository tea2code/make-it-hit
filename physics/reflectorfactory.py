from data import circle
from data import rect
from physics import circlecirclereflector
from physics import circlerectreflector

class NoReflectorError( Exception ):
    ''' Exception thrown if no reflector for the given objects was found. '''

class ReflectorFactory:
    ''' Factory of reflector objects. '''
    
    def createFrom( self, object1, object2 ):
        ''' Takes two objects and searches the fitting reflector. Raises NoReflectorError if no 
        reflector exists. Returns the reflector. 
        
        Test:
        >>> r = ReflectorFactory()
        >>> r.createFrom( circle.Circle(), rect.Rect() ) # doctest: +ELLIPSIS
        <...CircleRectReflector object at 0x...>
        >>> r.createFrom( circle.Circle(), circle.Circle() ) # doctest: +ELLIPSIS
        <...CircleCircleReflector object at 0x...>
        '''
        
        # Circle - Rect.
        if isinstance( object1, circle.Circle ) and isinstance( object2, rect.Rect ):
            return circlerectreflector.CircleRectReflector( object1, object2 )
         
        # Circle - Circle
        elif isinstance( object1, circle.Circle ) and isinstance( object2, circle.Circle ):
            return circlecirclereflector.CircleCircleReflector( object1, object2 )
         
        # Unknown objects. Can not be collided.
        else:
            raise NoReflectorError( 'No reflector object for "{0}" and "{1}" found.'.format(object1, object2) )
            
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()