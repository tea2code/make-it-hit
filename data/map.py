class Map:
    ''' Represents a map object.
    
    Member:
    border -- The width of the border (float).
    height -- The height of the map (float).
    objects -- List of objects (data.movable).
    player -- The player object (data.movable).
    targets -- List of targets (data.movable).
    width -- The width of the map (float).
    '''
    
    border = 0
    height = 1
    objects = []
    player = None
    targets = []
    width = 1
    
    def __init__( self ):
        ''' Test:
        >>> m = Map()
        >>> m.border
        0
        >>> m.height
        1
        >>> len(m.objects)
        0
        >>> m.player
        >>> len(m.targets)
        0
        >>> m.width
        1
        '''
    
    def __str__( self ):
        ''' Test:
        >>> m = Map()
        >>> print( m )
        Map(border 0.00, height 1.00, objects [], player None, targets [], width 1.00)
        '''
        objects = ', '.join( [str(element) for element in self.objects] )
        targets = ', '.join( [str(element) for element in self.targets] )
        template = 'Map(border {0:.2f}, height {1:.2f}, objects [{2}], player {3}, targets [{4}], width {5:.2f})'
        return template.format( self.border, self.height, objects, self.player, targets, self.width )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod( )