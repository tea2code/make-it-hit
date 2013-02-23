from common import tickable

class PostFrame( tickable.Tickable ):
    ''' This class executes tasks at the end of a frame. Mostly cleanup of calculated frame data. '''

    def tick( self, data ):
        ''' Implementation of Tickable.tick().
        
        Test:
        >>> import data.data
        >>> d = data.data.Data()
        >>> d.events.append( 1 )
        >>> len(d.events)
        1
        >>> p = PostFrame()
        >>> p.tick( d )
        >>> len(d.events)
        0
        '''
    
        # Clear events.
        del data.events[:]
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()