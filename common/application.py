from common import timestepper
from data import data
from fps import fps
from gamerules import gamerules
from graphics import tkgraphics
from input import tkinput
from physics import physics
from postframe import postframe

import argparse

class Application:
    ''' Application/Main class.

    Member:
    fpsCounterMeasures -- Number of counts before the fps counter should update.
    forceScale -- Scaling factor for force input vectors (float).
    frameTime -- "Should be" time of one frame (float).
    levelExtension -- The file extension of level files with dot (string).
    loopTime -- The overall refreshing time of the main loop int milliseconds (int). 
    startTime -- Time before level starts in milliseconds (int).
    windowHeight -- The height of the window (int).
    windowTitle -- Template for window title.
    windowWidth -- The width of the window (int).
    _data -- The "global" data object (data.data).
    _fps -- The module responsible to count frames per second (fps).
    _gamerules -- The module responsible for implementing game rules (gamerules.gamerules).
    _graphics -- The module responsible for visualizing the data (graphics.tkgraphics).
    _input -- The module responsible for user input (input.tkinput).
    _physics -- The module responsible for physics calculation (physics.physics).
    _postFrame -- The module responsible for after frame tasks (postframe.postframe).
    _timestepper -- The frame ticker (common.timestepper).
    '''
    
    def __init__( self ):
        ''' Test:
        >>> a = Application()
        >>> a.fpsCounterMeasures
        10
        >>> a.forceScale
        1.0
        >>> a.frameTime
        0.1
        >>> a.levelExtension
        '.yaml'
        >>> a.loopTime
        100
        >>> a.startTime
        0
        >>> a.windowHeight
        0
        >>> a.windowTitle
        ''
        >>> a.windowWidth
        0
        >>> a._data
        >>> a._fps
        >>> a._gamerules
        >>> a._graphics
        >>> a._input
        >>> a._physics
        >>> a._postFrame
        >>> a._timestepper
        '''
        self.fpsCounterMeasures = 10
        self.forceScale = 1.0
        self.frameTime = 0.1
        self.levelExtension = '.yaml'
        self.loopTime = 100
        self.startTime = 0
        self.windowHeight = 0
        self.windowTitle = ''
        self.windowWidth = 0
        self._data = None
        self._fps = None
        self._gamerules = None
        self._graphics = None
        self._input = None
        self._physics = None
        self._postFrame = None
        self._timestepper = None
        
    def begin( self ):
        ''' Start the application. '''
        
        # Read arguments.
        parser = argparse.ArgumentParser( description = 'Provide the level directory as an argument.' )
        parser.add_argument( 'levelDir')
        args = parser.parse_args()
        
        # Initialize data.
        self._data = data.Data()
        self._data.levelDir = args.levelDir
        self._data.state = self._data.STATES.MENU_MAIN
        self._data.startTime = self.startTime
        self._data.windowHeight = self.windowHeight
        self._data.windowTitle = self.windowTitle
        self._data.windowWidth = self.windowWidth
        
        # Initialize fps counter.
        self._fps = fps.Fps( self.fpsCounterMeasures, 2 * self.fpsCounterMeasures )
        
        # Initialize game rules.
        self._gamerules = gamerules.GameRules( self._data )
        
        # Initialize graphics.
        self._graphics = tkgraphics.TkGraphics( self._data )
        
        # Initialize physics.
        self._physics = physics.Physics()
        
        # Initialize post frame.
        self._postFrame = postframe.PostFrame()
        
        # Initialize time stepper.
        self._timestepper = timestepper.Timestepper( self.frameTime, self.calculateNextState )
        self._timestepper.time = self.frameTime
        
        # Initialize and activate input module.
        self._input = tkinput.TkInput( self._data )
        self._input.forceScale = self.forceScale
        self._input.bindLevelList( self._graphics.levelList )
        self._input.bindMenuBtn( self._graphics.backFromNewBtn )
        self._input.bindMenuBtn( self._graphics.menuBtn )
        self._input.bindNewGameBtn( self._graphics.newGameBtn )
        self._input.bindQuitBtn( self._graphics.quitBtn )
        self._input.bindRestartBtn( self._graphics.restartBtn )
        self._input.bindWindow( self._graphics.canvas )
        
        # Start.
        self._timestepper.start()
        self.__callNextState()
        self._graphics.start()
        
    def calculateNextState( self, t, dt ):
        ''' Callback function for the frame ticker. Executes all modules on the data. '''
        
        if self._data.state is self._data.STATES.QUIT:
            self._graphics.window.destroy()
            return
        
        self._physics.tick( self._data )
        self._fps.tick( self._data ) 
        self._gamerules.tick( self._data )
        self._graphics.tick( self._data )
        self._postFrame.tick( self._data )
        
        self._data.deltaTime = dt
        self._data.time += dt
    
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