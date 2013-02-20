from . import event

class VictoryEvent( event.Event ):
    ''' A victory event.'''
    
    def __init__( self ):
        ''' Test:
        >>> e = VictoryEvent()
        >>> e.type is event.Event.TYPES.VICTORY
        True
        '''         
        self.type = event.Event.TYPES.VICTORY
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()