from data import event

class CollisionEvent( event.Event ):
    ''' A collision event. 
    
    Member:
    object -- The object hit (data.movable).
    x -- The x-coordinate of the collision (int).
    y -- The y-coordinate of the collision (int).
    '''
    
    def __init__( self, object, x, y ):
        ''' Initializes the event with the coordinate. 
        
        Test:
        >>> e = CollisionEvent( 'test', 2, 6 )
        >>> e.type is event.Event.TYPES.COLLISION
        True
        >>> e.object
        'test'
        >>> e.x
        2
        >>> e.y
        6
        '''       
        super().__init__()
        self.type = event.Event.TYPES.COLLISION
        self.object = object
        self.x = x
        self.y = y
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()