from common import timestepper
from configuration import configstorage
from data import configuration
from data import data
from fps import fps
from gamerules import gamerules
from graphics import tkgraphics
from input import tkinput
from physics import physics
from postframe import postframe

import math

class Application:
    ''' Application/Main class.

    Member:
    configPath -- Path to user specifig configuration file (string).
    defaultConfigPath -- Path to default configuration file (string).
    _data -- The "global" data object (data.data).
    _fps -- The module responsible to count frames per second (fps).
    _gamerules -- The module responsible for implementing game rules (gamerules.gamerules).
    _graphics -- The module responsible for visualizing the data (graphics.tkgraphics).
    _input -- The module responsible for user input (input.tkinput).
    _loopTime -- The overall refreshing time of the main loop int milliseconds (int). 
    _physics -- The module responsible for physics calculation (physics.physics).
    _postFrame -- The module responsible for after frame tasks (postframe.postframe).
    _timestepper -- The frame ticker (common.timestepper).
    '''
    
    def __init__( self ):
        ''' Test:
        >>> a = Application()
        >>> a.configPath
        ''
        >>> a.defaultConfigPath
        ''
        >>> a._data
        >>> a._fps
        >>> a._gamerules
        >>> a._graphics
        >>> a._input
        >>> a._loopTime
        100
        >>> a._physics
        >>> a._postFrame
        >>> a._timestepper
        '''
        self.configPath = ''
        self.defaultConfigPath = ''
        self._data = None
        self._fps = None
        self._gamerules = None
        self._graphics = None
        self._input = None
        self._loopTime = 100
        self._physics = None
        self._postFrame = None
        self._timestepper = None
        
    def begin( self ):
        ''' Start the application. '''

        # Read configuration.
        configStorage = configstorage.ConfigStorage( self.defaultConfigPath, self.configPath )
        config = configStorage.load()

        # Initialize data.
        self._data = data.Data()
        self._data.configuration = config
        self._data.state = self._data.STATES.MENU_MAIN
        
        frameTime = 1 / self._data.configuration.framesPerSecond
        self._loopTime = math.floor( frameTime * 1000 )
        
        # Initialize fps counter.
        self._fps = fps.Fps( self._data.configuration.framesPerSecond, 
                             2 * self._data.configuration.framesPerSecond )
        
        # Initialize game rules.
        self._gamerules = gamerules.GameRules( self._data )
        
        # Initialize graphics.
        self._graphics = tkgraphics.TkGraphics( self._data )
        
        # Initialize physics.
        self._physics = physics.Physics()
        
        # Initialize post frame.
        self._postFrame = postframe.PostFrame()
        
        # Initialize time stepper.
        self._timestepper = timestepper.Timestepper( frameTime, self.calculateNextState )
        self._timestepper.time = frameTime
        
        # Initialize and activate input module.
        self._input = tkinput.TkInput( self._data )
        self._input.bindLevelList( self._graphics.levelList )
        self._input.bindMenuBtn( self._graphics.backFromNewBtn )
        self._input.bindMenuBtn( self._graphics.menuBtn )
        self._input.bindNewGameBtn( self._graphics.newGameBtn )
        self._input.bindNumLevelsInput( self._graphics.numLevelsInput )
        self._input.bindQuitBtn( self._graphics.quitBtn )
        self._input.bindRestartBtn( self._graphics.restartBtn )
        self._input.bindShuffleCheck( self._graphics.shuffleCheck )
        self._input.bindStartBtn( self._graphics.startBtn )
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
        self._graphics.after( self._loopTime, self.__nextState )
    
    def __nextState( self ):
        ''' Callback function for the main loop. '''
        self._timestepper.tick()    
        self.__callNextState()

if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()