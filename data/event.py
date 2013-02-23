from abc import ABCMeta  
from common import enum

class Event(metaclass = ABCMeta):
    ''' Base class for event objects.
    
    Constants:
    TYPES -- Possible event types (enum).
    
    Member:
    type -- The type of the event.
    '''
    
    TYPES = enum.createSeq( 'COLLISION', 'POINTS', 'TARGET' )
    
    def __init__( self ):
        ''' 
        
        Test:
        >>> e = Event()
        >>> e.type
        >>> e.type = Event.TYPES.TARGET
        >>> e.type is Event.TYPES.TARGET
        True
        >>> e.type is Event.TYPES.COLLISION
        False
        '''
        self.type = None
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()