from . import collider
from . import collision
from formulary import pythagorean

import math

class CircleRectCollider( collider.Collider ):
    ''' Calculates collision between circle and rect. 
    
    Member:
    _circle -- The circle (data.circle).
    _rect -- The rect (data.rect).
    '''
    
    _circle = None
    _rect = None
    
    def __init__( self, circle, rect ):
        self._circle = circle
        self._rect = rect
    
    def collide( self ):
        ''' Calculates collision between a circle and a rect. Returns the resulting collision object. 
        
        Test:
        >>> from data import circle
        >>> from data import rect
        >>> c = circle.Circle()
        >>> c.position.x = -100
        >>> c.position.y = -100
        >>> c.radius = 10
        >>> r = rect.Rect()
        >>> r.angle = 10
        >>> r.height = 10
        >>> r.width = 10
        >>> r.position.x = 100
        >>> r.position.y = 100
        >>> collider = CircleRectCollider( c, r )
        >>> collider.collide().isCollided
        False
        >>> c = circle.Circle()
        >>> c.position.x = 10
        >>> c.position.y = 10
        >>> c.radius = 5
        >>> r = rect.Rect()
        >>> r.angle = -45
        >>> r.height = 10
        >>> r.width = 4.2
        >>> r.position.x = 14.95
        >>> r.position.y = 5.05
        >>> collider = CircleRectCollider( c, r )
        >>> collision = collider.collide()
        >>> collision.isCollided
        True
        >>> print( '{0:.2f}'.format(collision.x) )
        13.47
        >>> print( '{0:.2f}'.format(collision.y) )
        6.53
        '''
        
        # Keep rectangle static and rotate circle according to angle ("backwards" -> -angle).
        radianAngle = math.radians( -self._rect.angle )
        cos = math.cos( radianAngle )
        sin = math.sin( radianAngle )
        distX = self._circle.position.x - self._rect.position.x
        distY = self._circle.position.y - self._rect.position.y
        cx = cos * distX - sin * distY + self._rect.position.x
        cy = sin * distX + cos * distY + self._rect.position.y
        
        # Closest point.
        x = 0
        y = 0
        
        # Find the closest x-coordinate from center of circle.
        rectWidthHalf = self._rect.width * 0.5
        if cx < self._rect.position.x - rectWidthHalf:
            x = self._rect.position.x - rectWidthHalf
        elif cx > self._rect.position.x + rectWidthHalf:
            x = self._rect.position.x + rectWidthHalf
        else:
            x = cx
            
        # Find the closest y-coordinate from center of circle.
        rectHeightHalf = self._rect.height * 0.5
        if cy < self._rect.position.y - rectHeightHalf:
            y = self._rect.position.y - rectHeightHalf
        elif cy > self._rect.position.y + rectHeightHalf:
            y = self._rect.position.y + rectHeightHalf
        else:
            y = cy
            
        # Determine collision.
        isCollided = False
        distance = pythagorean.euclideanDistance( cx, cy, x, y )
        if distance < self._circle.radius:
            isCollided = True
        
        # Rotate result point back.
        radianAngle = math.radians( self._rect.angle )
        cos = math.cos( radianAngle )
        sin = math.sin( radianAngle )
        distX = x - self._rect.position.x
        distY = y - self._rect.position.y
        x = cos * distX - sin * distY + self._rect.position.x
        y = sin * distX + cos * distY + self._rect.position.y

        # Result.
        c = collision.Collision( isCollided )
        c.x = x
        c.y = y
        return c
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()