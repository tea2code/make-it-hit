from . import reflectionnotonlineerror
from . import reflector
from data import vector2d
from formulary import comparison
from formulary import vector

import math

class CircleCircleReflector( reflector.Reflector ):
    ''' Calculates reflection between two circles. 
    
    Member:
    _circle1 -- The first circle (data.circle).
    _circle2 -- The second circle (data.circle).
    '''
    
    _circle1 = None
    _circle2 = None
    
    def __init__( self, circle1, circle2,  ):
        ''' The first circle is assumed to be moving and the second static. Reflection happens at 
        collision point (x, y). '''
        self._circle1 = circle1
        self._circle2 = circle2
    
    def reflect( self, x, y ):
        ''' Calculates reflection between two circles. Returns the resulting momentum vector. 
        Raises ReflectionNotOnLineError if reflection is not on the line of the rect.
        Takes the position of the reflection point as argument.
        
        Test:
        >>> from data import circle
        >>> from data import vector2d
        >>> c1 = circle.Circle()
        >>> c1.position.x = -4
        >>> c1.position.y = 2
        >>> c1.radius = 2
        >>> c1.momentum = vector2d.Vector2d( 4, 2 )
        >>> c2 = circle.Circle()
        >>> c2.position.x = 0
        >>> c2.position.y = 2
        >>> c2.radius = 2
        >>> x = -2
        >>> y = 2
        >>> reflector = CircleCircleReflector( c1, c2 )
        >>> v = reflector.reflect( x, y )
        >>> print( '{0:.2f}, {1:.2f}'.format(v.x, v.y) )
        -4.00, 2.00
        '''
        
        # Move reflection point to origin.
        reflectionX = x - self._circle2.position.x
        reflectionY = y - self._circle2.position.y
        
        # Prepare comparison.
        epsilon = comparison.epsilon()
        
        # Default values are used it the tangent line is vertical.
        pointX1 = reflectionX
        pointY1 = -1
        pointX2 = reflectionX
        pointY2 = 1
        
        # Calculate tangent line y = mx + b
        if not comparison.floatEqual( reflectionY, 0, epsilon ):
            # Tangent line is perpendicular to the radius, so it's slope m will be a negative reciprocal
            # of the slope of the line intersecting the reflection point.
            m = -(reflectionX / reflectionY)
                
            # Find b with the slope and the reflection point. Default value is used if tangent line is 
            # horizontal.
            b = reflectionY
            if not comparison.floatEqual( reflectionX, 0, epsilon ):
                b = reflectionY / (m * reflectionX)
            
            # Calculate tangent line points left and right of reflection point.
            pointX1 = reflectionX - 1
            pointY1 = m * pointX1 + b 
            pointX2 = reflectionX + 1
            pointY2 = m * pointX2 + b 
        
        # Calculate result.
        x, y = vector.reflectAtLine( self._circle1.momentum.x, self._circle1.momentum.y,
                                     pointX1, pointY1, pointX2, pointY2 )
        return vector2d.Vector2d( x, y )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()