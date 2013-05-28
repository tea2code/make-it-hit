from common import timestepper
from configuration import configstorage
from data import data
from fps import fps
from gamerules import gamerules
from graphics import tkgraphics
from input import tkinput
from physics import physics
from postframe import postframe
from sound import sound

import math

class Application:
    ''' Application/Main class.

    Member:
    configPath -- Path to user specific configuration file (string).
    data -- The "global" data object (data.data).
    defaultConfigPath -- Path to default configuration file (string).
    _configStorage -- The configuration storage system (ConfigStorage).
    _destroyed -- Flag indicating if the application is already quitting (boolean).
    _fps -- The module responsible to count frames per second (fps).
    _gamerules -- The module responsible for implementing game rules (gamerules.gamerules).
    _graphics -- The module responsible for visualizing the data (graphics.tkgraphics).
    _input -- The module responsible for user input (input.tkinput).
    _loopTime -- The overall refreshing time of the main loop int milliseconds (int). 
    _physics -- The module responsible for physics calculation (physics.physics).
    _postFrame -- The module responsible for after frame tasks (postframe.postframe).
    _sound -- The module responsible to play sound (sound.sound).
    _timestepper -- The frame ticker (common.timestepper).
    '''
    
    def __init__( self ):
        ''' Test:
        >>> a = Application()
        >>> a.configPath
        ''
        >>> a.defaultConfigPath
        ''
        >>> a.data # doctest: +ELLIPSIS
        <...Data object at 0x...>
        >>> a._destroyed
        False
        >>> a._fps
        >>> a._gamerules
        >>> a._graphics
        >>> a._input
        >>> a._loopTime
        100
        >>> a._physics
        >>> a._postFrame
        >>> a._sound
        >>> a._timestepper
        '''
        self.configPath = ''
        self.defaultConfigPath = ''
        self.data = data.Data()
        self._destroyed = False
        self._fps = None
        self._gamerules = None
        self._graphics = None
        self._input = None
        self._loopTime = 100
        self._physics = None
        self._postFrame = None
        self._sound = None
        self._timestepper = None
        
    def begin( self ):
        ''' Start the application. '''

        # Read configuration.
        self._configStorage = configstorage.ConfigStorage( self.defaultConfigPath, self.configPath )
        config = self._configStorage.load()

        # Initialize data.
        self.data.configuration = config
        self.data.state = self.data.STATES.MENU_MAIN
        
        frameTime = 1 / self.data.configuration.framesPerSecond
        self._loopTime = math.floor( frameTime * 1000 )
        
        # Initialize fps counter.
        self._fps = fps.Fps( self.data.configuration.framesPerSecond, 
                             2 * self.data.configuration.framesPerSecond )
        
        # Initialize game rules.
        self._gamerules = gamerules.GameRules( self.data )
        
        # Initialize graphics.
        self._graphics = tkgraphics.TkGraphics( self.data )
        self._graphics.window.protocol( 'WM_DELETE_WINDOW', self.__quit )
        
        # Initialize physics.
        self._physics = physics.Physics()
        
        # Initialize post frame.
        self._postFrame = postframe.PostFrame()
        
        self._sound = sound.Sound()
        
        # Initialize time stepper.
        self._timestepper = timestepper.Timestepper( frameTime, self.calculateNextState )
        self._timestepper.time = frameTime
        
        # Initialize and activate input module.
        self._input = tkinput.TkInput( self.data )
        self._input.bindConfigBtn( self._graphics.configBtn )
        self._input.bindConfigInputs( self._graphics.startDelayInput, 
                                      self._graphics.windowHeightInput, 
                                      self._graphics.windowWidthInput )
        self._input.bindHelpBtn( self._graphics.helpBtn )
        self._input.bindLevelList( self._graphics.levelList )
        self._input.bindMenuBtn( self._graphics.backFromConfigBtn )
        self._input.bindMenuBtn( self._graphics.backFromNewBtn )
        self._input.bindMenuBtn( self._graphics.menuBtn )
        self._input.bindNewGameBtn( self._graphics.newGameBtn )
        self._input.bindNumLevelsInput( self._graphics.numLevelsInput )
        self._input.bindQuitBtn( self._graphics.quitBtn )
        self._input.bindRestartBtn( self._graphics.restartBtn )
        self._input.bindSaveConfigBtn( self._graphics.saveConfigBtn )
        self._input.bindShuffleCheck( self._graphics.shuffleCheck )
        self._input.bindStartBtn( self._graphics.startBtn )
        self._input.bindWindow( self._graphics.canvas )

        # Start.
        self._timestepper.start()
        self.__callNextState()
        self._graphics.start()
        
    def calculateNextState( self, t, dt ):
        ''' Callback function for the frame ticker. Executes all modules on the data. '''
        
        if self.data.state is self.data.STATES.QUIT:
            self.__quit()
            return
        
        self._physics.tick( self.data )
        self._fps.tick( self.data ) 
        self._gamerules.tick( self.data )
        self._graphics.tick( self.data )
        self._sound.tick( self.data )
        self._postFrame.tick( self.data )
        
        self.data.deltaTime = dt
        self.data.time += dt
    
    def __callNextState( self ):
        ''' Return to main loop. '''
        self._graphics.after( self._loopTime, self.__nextState )
    
    def __nextState( self ):
        ''' Callback function for the main loop. '''
        self._timestepper.tick()    
        self.__callNextState()

    def __quit( self ):
        ''' Quit application and save configuration. '''
        if self._destroyed:
            return
        
        self._destroyed = True
        self._configStorage.save( self.data.configuration )
        self._graphics.window.destroy()

if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()