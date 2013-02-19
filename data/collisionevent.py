from . import event

class CollisionEvent( event.Event ):
    ''' A collision event. 
    
    Member:
    x -- The x-coordinate of the collision (int).
    y -- The y-coordinate of the collision (int).
    '''
    
    def __init__( self, x, y ):
        ''' Initializes the event with the coordinate. 
        
        Test:
        >>> e = CollisionEvent( 2, 6 )
        >>> e.type is event.Event.TYPES.COLLISION
        True
        >>> e.x
        2
        >>> e.y
        6
        '''         
        self.type = event.Event.TYPES.COLLISION
        self.x = x
        self.y = y
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()