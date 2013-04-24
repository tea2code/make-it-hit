class Target:
    ''' Represents a target object.

    Member:
    final -- If set to true the level will end if this target is hit (boolean).
    hit -- True if already hit else false (boolean).
    object -- The visible object (data.movable).
    points -- The point value the player receives if he hits the target (int). 
    '''
    
    def __init__( self ):
        ''' Test:
        >>> t = Target()
        >>> t.final
        True
        >>> t.hit
        False
        >>> t.object
        >>> t.points
        0
        '''
        self.final = True
        self.hit = False
        self.object = None
        self.points = 0
        
    def __str__( self ):
        ''' Test:
        >>> t = Target()
        >>> print( t )
        Target(final True, hit False, points 0, object None)
        '''
        template = 'Target(final {}, hit {}, points {}, object {})'
        return template.format(self.final, self.hit, self.points, self.object )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod( )