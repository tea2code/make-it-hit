from common import timestepper
from data import data
from graphics import tkgraphics

class Application:
    ''' Application/Main class.

    Member:
    frameTime -- "Should be" time of one frame (float).
    loopTime -- The overall refreshing time of the main loop int milliseconds (int). 
    _data -- The "global" data object (Data).
    _graphics -- The module responsible for visualizing the data (Graphics).
    _timestepper -- The frame ticker (TimeStepper).
    '''
    
    frameTime = 0.1
    loopTime = 100
    _graphics = None
    _data = None
    _timestepper = None
    
    def __init__( self ):
        ''' Test:
        >>> a = Application()
        >>> a.frameTime
        0.1
        >>> a.loopTime
        100
        >>> a._graphics
        >>> a._data
        >>> a._timestepper
        '''
        
    def begin( self ):
        ''' Start the application. '''
        # Initialize data.
        self._data = data.Data()
        
        # Initialize graphics.
        self._graphics = tkgraphics.TkGraphics( self._data )
        
        # Initialize time stepper.
        self._timestepper = timestepper.Timestepper( self.frameTime, self.calculateNextState )
        self._timestepper.time = self.frameTime
        
        # Start.
        self._timestepper.start()
        self.__callNextState()
        self._graphics.start()
        
    def calculateNextState( self, t, dt ):
        ''' Callback function for the frame ticker. Executes all modules on the data. '''
        self._data.deltaTime = dt
        self._data.time = t
        self._graphics.tick( self._data )
    
    def __callNextState( self ):
        ''' Return to main loop. '''
        self._graphics.after( self.loopTime, self.__nextState )
    
    def __nextState( self ):
        ''' Callback function for the main loop. '''
        self._timestepper.tick()    
        self.__callNextState()

if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()