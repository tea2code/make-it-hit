from common import tickable
from . import fpscounter

class Fps( tickable.Tickable ):
    ''' This class calculates the frame rate. 
    
    Member:
    fpsCounter -- The fps counter which does all the hard work (This class is just lazy).
    maxTickCounts -- Number of ticks before updating the data object.
    started -- Has the fps counter already started.
    tickCounter -- Number of ticks since the last update of the data object.
    '''

    fpsCounter = None
    maxTickCounts = 0
    started = False
    tickCounter = 0
    
    def __init__( self, maxTickCounts, measurementPoints ):
        ''' Test:
        >>> f = Fps( 10, 20 )
        >>> f.fpsCounter # doctest: +ELLIPSIS
        <...FpsCounter object at 0x...>
        >>> f.maxTickCounts
        10
        >>> f.started
        False
        >>> f.tickCounter
        0
        '''
        self.maxTickCounts = maxTickCounts
        self.fpsCounter = fpscounter.FpsCounter( measurementPoints )
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick(). '''
        
        if self.started == False:
            self.fpsCounter.start()
            self.started = True
        
        self.fpsCounter.tick()
        self.tickCounter += 1
        if self.tickCounter > self.maxTickCounts:
            data.fps = round( self.fpsCounter.fps() )
            self.tickCounter = 0
            
    def __str__( self ):
        ''' Test:
        >>> f = Fps( 20, 10 )
        >>> print(f)
        Fps(maxTickCounts 20, started False, tickCounter 0)
        '''
        return 'Fps(maxTickCounts {0}, started {1}, tickCounter {2})'.format(self.maxTickCounts, 
                                                                             self.started, 
                                                                             self.tickCounter)
            
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()