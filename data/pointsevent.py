from data import event

class PointsEvent( event.Event ):
    ''' A points event. 
    
    Member:
    points -- The points. Can be negative or positive (int).
    '''
    
    def __init__( self, points ):
        ''' Initializes the event with the coordinate. 
        
        Test:
        >>> e = PointsEvent( 2 )
        >>> e.type is event.Event.TYPES.POINTS
        True
        >>> e.points
        2
        '''     
        super().__init__()
        self.type = event.Event.TYPES.POINTS
        self.points = points
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()