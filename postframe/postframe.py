﻿from common import tickable

class PostFrame( tickable.Tickable ):
    ''' This class executes tasks at the end of a frame. Mostly cleanup of calculated frame data. '''

    def tick( self, data ):
        ''' Implementation of Tickable.tick().
        
        Test:
        >>> import data.data
        >>> d = data.data.Data()
        >>> d.collisionEvents.append( 1 )
        >>> d.targetEvents.append( 1 )
        >>> len(d.events)
        1
        >>> len(d.targetEvents)
        1
        >>> p = PostFrame()
        >>> p.tick( d )
        >>> len(d.collisionEvents)
        0
        >>> len(d.targetEvents)
        0
        '''
    
        # Clear events.
        del data.collisionEvents[:]
        del data.targetEvents[:]
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()