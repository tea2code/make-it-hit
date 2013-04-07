from common import tickable
from graphics import tkgameview
from graphics import tkmenuview

import tkinter as tk

class TkGraphics( tickable.Tickable ):
    ''' This class handles the visualization of the current state. 
    
    Member:
    backFromNewBtn -- The button which leads back to the main menu (Button).
    canvas -- The canvas object (Canvas).
    levelList -- The list box containing all levels (ListBox).
    menuBtn -- The button which leads back to the main menu (Button).
    newGameBtn -- The new game button (Button).
    numLevelsInput -- Input field for number of levels to use (Entry).
    quitBtn -- The button to quit the game (Button).
    restartBtn -- The restart button (Button).
    shuffleCheck -- A random check box to indicate if the level list should be shuffled (Checkbutton).
    startBtn -- The button to start the game (Button).
    window -- The window object (Tk).
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
        
    @property
    def backFromNewBtn( self ):
        return self._menuView.backBtn
        
    @property
    def canvas( self ):
        return self._gameView.canvas
    
    @property
    def configBtn( self ):
        return self._menuView.configBtn
    
    @property
    def levelList( self ):
        return self._menuView.levelList
    
    @property 
    def menuBtn( self ):
        return self._gameView.menuBtn
    
    @property 
    def newGameBtn( self ):
        return self._menuView.newGameBtn
    
    @property
    def numLevelsInput( self ):
        return self._menuView.numLevelsInput
    
    @property 
    def quitBtn( self ):
        return self._menuView.quitBtn
    
    @property
    def restartBtn( self ):
        return self._gameView.restartBtn
        
    @property
    def shuffleCheck( self ):
        return self._menuView.shuffleCheck
    
    @property
    def startBtn( self ):
        return self._menuView.startBtn
        
    def after( self, time, function ):
        ''' Calls function after time in milliseconds. '''
        self.window.after( time, function )
        
    def start( self ):
        ''' Starts drawing. '''
        self.window.mainloop()
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Draws the current state (data) on the canvas. '''
        
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