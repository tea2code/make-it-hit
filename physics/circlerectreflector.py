from data import vector2d
from formulary import pythagorean as py
from formulary import rotation
from formulary import vector
from physics import reflector

class CircleRectReflector( reflector.Reflector ):
    ''' Calculates reflection between a circle and a rectangle.
    
    Member:
    _circle -- The circle (data.circle).
    _rect -- The rectangle (data.rect).
    '''
    
    def __init__( self, circle, rect ):
        ''' The circle is assumed to be moving and the rect static. Reflection happens at 
        reflection point (x, y). 
        
        Test:
        >>> c = CircleRectReflector(None, None)
        >>> c._circle
        >>> c._rect
        '''
        super().__init__()
        self._circle = circle
        self._rect = rect
    
    def reflect( self, x, y ):
        ''' Calculates reflection between two circles. Returns the resulting momentum vector. 
        Takes the position of the reflection point as argument.
        
        Test:
        >>> from data import circle
        >>> from data import rect
        >>> from data import vector2d
        >>> c = circle.Circle()
        >>> c.position.x = -4
        >>> c.position.y = 2
        >>> c.radius = 2
        >>> c.momentum = vector2d.Vector2d( 4, 2 )
        >>> r = rect.Rect()
        >>> r.position.x = 0
        >>> r.position.y = 2
        >>> r.width = 4
        >>> r.height = 4
        >>> x = -2
        >>> y = 2
        >>> reflector = CircleRectReflector( c, r )
        >>> v = reflector.reflect( x, y )
        >>> print( '{0:.2f}, {1:.2f}'.format(v.x, v.y) )
        -4.00, 2.00
        '''
        # Calculate values of all four points of the rectangle without rotation.
        heightHalf = self._rect.height * 0.5
        widthHalf = self._rect.width * 0.5
        xPlus = widthHalf
        xMinus = -widthHalf
        yPlus = heightHalf
        yMinus = -heightHalf

        # Rotate reflection point back and move to origin.
        rotatedX = rotation.rotateX( x - self._rect.position.x, 
                                     y - self._rect.position.y, 
                                     -self._rect.angle )
        rotatedY = rotation.rotateY( x - self._rect.position.x, 
                                     y - self._rect.position.y,
                                     -self._rect.angle )
        
        # Prepare comparison.
        pointX1 = 0
        pointY1 = 0
        pointX2 = 0
        pointY2 = 0
        
        left, up, right = range(3)
        dists = []
        dists.append( py.pointToLineDistance(rotatedX, rotatedY, xMinus, yMinus, xMinus, yPlus) )
        dists.append( py.pointToLineDistance(rotatedX, rotatedY, xMinus, yPlus,  xPlus,  yPlus) )
        dists.append( py.pointToLineDistance(rotatedX, rotatedY, xPlus,  yMinus, xPlus,  yPlus) )
        dists.append( py.pointToLineDistance(rotatedX, rotatedY, xMinus, yMinus, xPlus,  yMinus) )
        line = dists.index( min(dists) )

        # Left.
        if line is left:
            pointX1 = xMinus
            pointY1 = yMinus
            pointX2 = xMinus
            pointY2 = yPlus
        # Up.
        elif line is up:
            pointX1 = xMinus
            pointY1 = yPlus
            pointX2 = xPlus
            pointY2 = yPlus
        # Right.
        elif line is right:
            pointX1 = xPlus
            pointY1 = yMinus
            pointX2 = xPlus
            pointY2 = yPlus
        # Down.
        else:
            pointX1 = xMinus
            pointY1 = yMinus
            pointX2 = xPlus
            pointY2 = yMinus
            
        # Rotate line points.
        rotatedX1 = rotation.rotateX( pointX1, pointY1, self._rect.angle ) + self._rect.position.x
        rotatedY1 = rotation.rotateY( pointX1, pointY1, self._rect.angle ) + self._rect.position.y
        rotatedX2 = rotation.rotateX( pointX2, pointY2, self._rect.angle ) + self._rect.position.x
        rotatedY2 = rotation.rotateY( pointX2, pointY2, self._rect.angle ) + self._rect.position.y
        
        # Calculate result.
        x, y = vector.reflectAtLine( self._circle.momentum.x, self._circle.momentum.y,
                                     rotatedX1, rotatedY1, rotatedX2, rotatedY2 )
        return vector2d.Vector2d( x, y )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()