class Target:
    ''' Represents a target object.

    Member:
    object -- The visible object (data.movable).
    points -- The point value the player receives if he hits the target (int). 
    '''
    
    def __init__( self ):
        ''' Test:
        >>> t = Target()
        >>> t.object
        >>> t.points
        0
        '''
        self.object = None
        self.points = 0
        
    def __str__( self ):
        ''' Test:
        >>> t = Target()
        >>> print( t )
        Target(points 0, object None)
        '''
        template = 'Target(points {0}, object {1})'
        return template.format(self.points, self.object )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod( )