from common import timestepper
from data import data
from fps import fps
from graphics import tkgraphics
from input import tkinput

import argparse
import os

class Application:
    ''' Application/Main class.

    Member:
    fpsCounterMeasures -- Number of counts before the fps counter should update.
    forceScale -- Scaling factor for force input vectors (float).
    frameTime -- "Should be" time of one frame (float).
    loopTime -- The overall refreshing time of the main loop int milliseconds (int). 
    windowTitle -- Template for window title.
    _data -- The "global" data object (data.data).
    _fps -- The module responsible to count frames per second (fps.fps).
    _graphics -- The module responsible for visualizing the data (graphics.tkgraphics).
    _input -- The module responsible for user input (input.tkinput).
    _timestepper -- The frame ticker (common.timestepper).
    '''
    
    fpsCounterMeasures = 10
    frameTime = 0.1
    forceScale = 1.0
    loopTime = 100
    windowTitle = ''
    _data = None
    _fps = None
    _graphics = None
    _input = None
    _timestepper = None
    
    def __init__( self ):
        ''' Test:
        >>> a = Application()
        >>> a.fpsCounterMeasures
        10
        >>> a.frameTime
        0.1
        >>> a.forceScale
        1.0
        >>> a.loopTime
        100
        >>> a._data
        >>> a._fps
        >>> a._graphics
        >>> a._input
        >>> a._timestepper
        '''
        
    def begin( self ):
        ''' Start the application. '''
        
        # Read arguments.
        parser = argparse.ArgumentParser( description='Provide the level path as an argument.' )
        parser.add_argument( 'level' )
        args = parser.parse_args()
        
        # Check if level exits.
        if not os.path.exists( args.level ):
            raise FileNotFoundError( 'The level "'+args.level+'" was not found.' )
        
        # Initialize data.
        self._data = data.Data()
        self._data.windowTitle = self.windowTitle
        
        # Initialize fps counter.
        self._fps = fps.Fps( self.fpsCounterMeasures, 2 * self.fpsCounterMeasures )
        
        # Initialize graphics.
        self._graphics = tkgraphics.TkGraphics( self._data )
        
        # Initialize time stepper.
        self._timestepper = timestepper.Timestepper( self.frameTime, self.calculateNextState )
        self._timestepper.time = self.frameTime
        
        # Initialize and activate input module.
        self._input = tkinput.TkInput( self._data, self._graphics.window )
        self._input.forceScale = self.forceScale
        
        # Start.
        self._timestepper.start()
        self.__callNextState()
        self._graphics.start()
        
    def calculateNextState( self, t, dt ):
        ''' Callback function for the frame ticker. Executes all modules on the data. '''
        self._data.deltaTime = dt
        self._data.time = t
        self._fps.tick( self._data ) 
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