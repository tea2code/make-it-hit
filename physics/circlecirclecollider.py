from . import collider
from . import collision

import math

class CircleCircleCollider( collider.Collider ):
    ''' Calculates collision between two circles. 
    
    Member:
    _circle1 -- The first circle (data.circle).
    _circle2 -- The second circle (data.circle).
    '''
    
    _circle1 = None
    _circle2 = None
    
    def __init__( self, circle1, circle2 ):
        self._circle1 = circle1
        self._circle2 = circle2
    
    def collide( self ):
        ''' Calculates collision between two circles. Returns the resulting collision object. 
        
        Test:
        >>> from data import circle
        >>> c1 = circle.Circle()
        >>> c1.position.x = -4
        >>> c1.position.y = 2
        >>> c1.radius = 1
        >>> c2 = circle.Circle()
        >>> c2.position.x = 0
        >>> c2.position.y = 2
        >>> c2.radius = 1
        >>> collider = CircleCircleCollider( c1, c2 )
        >>> collider.collide().isCollided
        False
        >>> c1.radius = 2
        >>> c2.radius = 2
        >>> collider = CircleCircleCollider( c1, c2 )
        >>> collision = collider.collide()
        >>> collision.isCollided
        True
        >>> print( '{0:.2f}'.format(collision.x) )
        -2.00
        >>> print( '{0:.2f}'.format(collision.y) )
        2.00
        '''
        vector = self._circle1.position - self._circle2.position
        distance = self._circle1.radius + self._circle2.radius

        isCollided = (vector.length() <= distance)
        
        if isCollided:
            pass
        
        c = collision.Collision( isCollided )
        return c
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()