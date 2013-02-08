class Map:
    ''' Represents a map object.
    
    Member:
    border -- The width of the border (float).
    height -- The height of the map (float).
    objects -- List of objects (data.movable).
    players -- List of players (data.movable).
    targets -- List of targets (data.movable).
    width -- The width of the map (float).
    '''
    
    border = 0
    height = 1
    objects = []
    players = []
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
        >>> len(m.players)
        0
        >>> len(m.targets)
        0
        >>> m.width
        1
        '''
    
    def __str__( self ):
        ''' Test:
        >>> m = Map()
        >>> print( m )
        Map(border 0.00, height 1.00, objects [], players [], targets [], width 1.00)
        '''
        objects = ', '.join( [str(element) for element in self.objects] )
        players = ', '.join( [str(element) for element in self.players] )
        targets = ', '.join( [str(element) for element in self.targets] )
        template = 'Map(border {0:.2f}, height {1:.2f}, objects [{2}], players [{3}], targets [{4}], width {5:.2f})'
        return template.format( self.border, self.height, objects, players, targets, self.width )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod( )