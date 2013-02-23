from data import event

class TargetEvent( event.Event ):
    ''' A target hit event. 
    
    Member:
    target -- The target object hit (data.target).
    x -- The x-coordinate of the hit (int).
    y -- The y-coordinate of the hit (int).
    '''
    
    def __init__( self, target, x, y ):
        ''' Initializes the event with the coordinate. 
        
        Test:
        >>> e = TargetEvent( 'test', 2, 6 )
        >>> e.type is event.Event.TYPES.TARGET
        True
        >>> e.target
        'test'
        >>> e.x
        2
        >>> e.y
        6
        '''      
        super().__init__()
        self.type = event.Event.TYPES.TARGET
        self.target = target
        self.x = x
        self.y = y
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()