from . import reflector

import math

class CircleCircleReflector( reflector.Reflector ):
    ''' Calculates reflection between two circles. 
    
    Member:
    _circle1 -- The first circle (data.circle).
    _circle2 -- The second circle (data.circle).
    _x -- The x-component of the collision point (float).
    _y -- The y-component of the collision point (float).
    '''
    
    _circle1 = None
    _circle2 = None
    _x = 0
    _y = 0
    
    def __init__( self, circle1, circle2, x, y ):
        ''' The first circle is assumed to be moving and the second static. Reflection happens at 
        collision point (x, y). '''
        self._circle1 = circle1
        self._circle2 = circle2
        self._x = x
        self._y = y
    
    def reflect( self ):
        ''' Calculates reflection between two circles. Returns the resulting moment vector. 
        
        Test:
        >>> from data import circle
        >>> from data import vector2d
        >>> c1 = circle.Circle()
        >>> c1.position.x = -4
        >>> c1.position.y = 2
        >>> c1.radius = 2
        >>> c1.momentum = vector2d.Vector2d( 0, 2 )
        >>> c2 = circle.Circle()
        >>> c2.position.x = 0
        >>> c2.position.y = 2
        >>> c2.radius = 2
        >>> x = -2
        >>> y = 2
        >>> reflector = CircleCircleReflector( c1, c2, x, y )
        >>> x, y = reflector.reflect()
        >>> print( '{0:.2f}, {1:.2f}'.format(x, y) )
        -4.00, 2.00
        '''
        return 0, 0
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()