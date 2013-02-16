from . import reflector

import math

class CircleRectReflector( reflector.Reflector ):
    ''' Calculates reflection between a circle and a rectangle.
    
    Member:
    _circle -- The circle (data.circle).
    _rect -- The rectangle (data.rect).
    _x -- The x-component of the collision point (float).
    _y -- The y-component of the collision point (float).
    '''
    
    _circle = None
    _rect = None
    _x = 0
    _y = 0
    
    def __init__( self, circle, rect, x, y ):
        ''' The circle is assumed to be moving and the rect static. Reflection happens at 
        collision point (x, y). '''
        self._circle = circle
        self._rect = rect
        self._x = x
        self._y = y
    
    def reflect( self ):
        ''' Calculates reflection between two circles. Returns the resulting moment vector. 
        
        Test:
        >>> from data import circle
        >>> from data import rect
        >>> from data import vector2d
        >>> c = circle.Circle()
        >>> c.position.x = -4
        >>> c.position.y = 2
        >>> c.radius = 2
        >>> c.momentum = vector2d.Vector2d( 0, 2 )
        >>> r = rect.Rect()
        >>> r.position.x = 0
        >>> r.position.y = 2
        >>> r.width = 4
        >>> r.height = 4
        >>> x = -2
        >>> y = 2
        >>> reflector = CircleRectReflector( c, r, x, y )
        >>> x, y = reflector.reflect()
        >>> print( '{0:.2f}, {1:.2f}'.format(x, y) )
        -4.00, 2.00
        '''
        return 0, 0
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()