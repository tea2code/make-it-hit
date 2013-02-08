from . import movable

class Rect( movable.Movable ):
    ''' Class representing a rectangle. 
    
    Member:
    angle -- The angle in degree of the rect (float).
    height -- The height of the rect (float).
    width -- The width of the rect (float).
    '''
    angle = 0
    height = 1
    width = 1
    
    def __init__( self ):
        ''' Test: 
        >>> r = Rect()
        >>> r.angle
        0
        >>> r.height
        1
        >>> r.width
        1
        '''
        super().__init__()
        
    def __str__( self ):
        ''' Test:
        >>> r = Rect()
        >>> print( r )
        Rect(angle 0.00, height 1.00, width 1.00, Movable(forces [], mass 0.00, momentum Vector2d(0.00, 0.00), position Vector2d(0.00, 0.00)))
        '''
        template = 'Rect(angle {0:.2f}, height {1:.2f}, width {2:.2f}, {3})'
        return template.format(self.angle, self.height, self.width, super().__str__() )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod( )