﻿class Collision:
    ''' Represents a collision result object.

    Member:
    isCollided -- True if collision occured else false (boolean).
    x -- The x-component of the point of collision (int).
    y -- The y-component of the point of collision (int).
    '''

    def __init__( self, isCollided ):
        ''' Initialize object.
        
        Test:
        >>> c = Collision( True )
        >>> c.isCollided
        True
        >>> c.x
        0
        >>> c.y
        0
        '''
        self.isCollided = isCollided
        self.x = 0
        self.y = 0
        
    def __str__( self ):
        ''' Test:
        >>> c = Collision( True )
        >>> print(c)
        Collision(isCollided True, x 0.00, y 0.00)
        '''
        template = 'Collision(isCollided {0}, x {1:.2f}, y {2:.2f})'
        return template.format(self.isCollided, self.x, self.y)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()