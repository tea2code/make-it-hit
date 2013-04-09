from common import tickable
from graphics import tkgameview
from graphics import tkmenuview

import tkinter as tk

class TkGraphics( tickable.Tickable ):
    ''' This class handles the visualization of the current state. 
    
    Member:
    backFromConfigBtn -- The button which leads back from config menu to the main menu (Button).
    backFromNewBtn -- The button which leads back to the main menu (Button).
    canvas -- The canvas object (Canvas).
    configBtn -- The button which opens the configuration menu (Button).
    helpBtn -- The button which opens the help menu (Button).
    levelList -- The list box containing all levels (ListBox).
    menuBtn -- The button which leads back to the main menu (Button).
    newGameBtn -- The new game button (Button).
    numLevelsInput -- Input field for number of levels to use (Entry).
    quitBtn -- The button to quit the game (Button).
    restartBtn -- The restart button (Button).
    saveConfigBtn -- The button to save the config (Button).
    shuffleCheck -- A random check box to indicate if the level list should be shuffled (Checkbutton).
    startBtn -- The button to start the game (Button).
    startDelayInput -- Input field for start delay (Entry).
    window -- The window object (Tk).
    windowHeightInput -- Input field for window height (Entry).
    windowWidthInput -- Input field for window width (Entry).
    _gameView -- The game view (GameView).
    _menuView -- The menu view (MenuView).
    '''
    
    def __init__( self, data ):
        ''' Parameters contain the data object with the window settings and the width of the 
        menu bar. '''
        
        # Create window.
        self.window = tk.Tk()
        self.window.config( background = 'white' )
        
        # Create views.
        self._gameView = tkgameview.TkGameView( data, self.window )
        self._menuView = tkmenuview.TkMenuView( data, self.window )
    
    def __getattr__( self, name ):
        ''' Implemented to give access to view properties. '''
        if hasattr( self._gameView, name ):
            return getattr( self._gameView, name )
        elif hasattr( self._menuView, name ):
            return getattr( self._menuView, name )
        else:
            raise AttributeError( 'Attribute "{}" not found.'.format(name) )
        
    def after( self, time, function ):
        ''' Calls function after time in milliseconds. '''
        self.window.after( time, function )
        
    def start( self ):
        ''' Starts drawing. '''
        self.window.mainloop()
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Draws the current state (data) on the canvas. '''
        
        if data.state is data.STATES.QUIT:
            return
        
        viewDescription = 'Menu'
        if data.level:
            viewDescription = data.level.name
        self.window.title( data.configuration.windowTitle.format(viewDescription, data.fps) )
        
        if data.state in [data.STATES.MENU_MAIN, data.STATES.MENU_NEW, data.STATES.MENU_CONFIG]:
            self._gameView.hide( data )
            self._menuView.show( data )
        else:
            self._menuView.hide( data )
            self._gameView.show( data )