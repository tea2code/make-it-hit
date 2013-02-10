import time
from collections import deque

class FpsCounter():
    ''' This class implements a counter which calculates the frames per second. 
    
    Member:
    maxNum -- Maximum number of stored measurements.
    measurements -- List of measurement points.
    _lastTime -- Previous timestamp.
    '''
    
    maxNum = 0
    measurements = deque([])
    _lastTime = 0
    
    def __init__( self, maxNum = 20 ):
        ''' Parameter maxNum gives the maximum number of stored measurements. 
        
        Test:
        >>> f = FpsCounter(42)
        >>> f.maxNum
        42
        >>> len(f.measurements)
        0
        >>> f._lastTime
        0
        '''
        self.maxNum = maxNum
        
    def fps( self ):
        ''' Calculates the frames per second returns it as a floating point number. 
        
        Test:
        >>> f = FpsCounter()
        >>> f.measurements.append( 10 )
        >>> f.measurements.append( 11 )
        >>> f.measurements.append( 12 )
        >>> round( f.fps(), 4 )
        0.0909
        '''
        sumM = sum( self.measurements )
        lenM = len( self.measurements )
        avgM =  sumM / lenM
        return 1 / avgM
        
    def start( self ):
        ''' Starts counter. '''
        self._lastTime = self.__time()
        
    def tick( self ):
        ''' Must be called every frame. 
        
        Test:
        >>> f = FpsCounter( 3 )
        >>> f.measurements.clear() # Prevent weird doctest (?) bug that measurements has already content.
        >>> len( f.measurements )
        0
        >>> f.tick()
        >>> len( f.measurements )
        1
        >>> f.tick()
        >>> len( f.measurements )
        2
        >>> f.tick()
        >>> len( f.measurements )
        3
        >>> f.tick()
        >>> len( f.measurements )
        3
        '''
        currentTime = self.__time()
        self.measurements.append( currentTime - self._lastTime )
        self._lastTime = currentTime
        
        if len(self.measurements) > self.maxNum:
            self.measurements.popleft()
        
    def __time( self ):
        return time.perf_counter()
        
    def __str__( self ):
        ''' Test:
        >>> f = FpsCounter()
        >>> print(f)
        FpsCounter(maxNum 20, measurements [], _lastTime 0.00)
        '''
        measurements = ", ".join( [str(element) for element in self.measurements]  )
        template = 'FpsCounter(maxNum {0}, measurements [{1}], _lastTime {2:.2f})'
        return template.format(self.maxNum, measurements, self._lastTime)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()