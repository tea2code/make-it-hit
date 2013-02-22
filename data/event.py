from abc import ABCMeta  
from common import enum

class Event(metaclass = ABCMeta):
    ''' Base class for event objects.
    
    Member:
    type -- The type of the event.
    '''
    
    TYPES = enum.createSeq( 'COLLISION', 'POINTS', 'TARGET' )
    
    def __init__( self ):
        ''' 
        
        Test:
        >>> e = Event()
        >>> e.type = Event.TYPES.TARGET
        >>> e.type is Event.TYPES.TARGET
        True
        >>> e.type is Event.TYPES.COLLISION
        False
        '''
                
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()