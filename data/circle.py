from data import movable

class Circle( movable.Movable ):
    ''' Class representing a circle. 
    
    Member:
    radius -- Radius of the circle (float).
    '''
    
    def __init__( self ):
        ''' Test:
        >>> c = Circle()
        >>> c.radius
        1
        '''
        super().__init__()
        self.radius = 1
        
    def __str__( self ):
        ''' Test:
        >>> c = Circle()
        >>> print(c)
        Circle(radius 1.00, Movable(colliding True, forces [], mass 0.00, momentum Vector2d(0.00, 0.00), position Vector2d(0.00, 0.00)))
        '''
        return 'Circle(radius {0:.2f}, {1})'.format( self.radius, super().__str__() )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()