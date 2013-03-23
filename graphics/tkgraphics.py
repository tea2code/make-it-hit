from common import tickable
from graphics import gameview

import tkinter

class TkGraphics( tickable.Tickable ):
    ''' This class handles the visualization of the current state. 
    
    Member:
    canvas -- The canvas object (Canvas).
    restartBtn -- The restart button (Button).
    window -- The window object (Tk).
    _gameView -- The game view (GameView).
    '''
    
    def __init__( self, data ):
        ''' The parameter data which contains the window settings. '''
        
        # Create window.
        self.window = tkinter.Tk()
        self.window.config( background = 'white' )
        
        # Create game view.
        self._gameView = gameview.GameView( data, self.window )
        
    def after( self, time, function ):
        ''' Calls function after time in milliseconds. '''
        self.window.after( time, function )
     
    @property
    def canvas( self ):
        return self._gameView.canvas
    
    @property
    def restartBtn( self ):
        return self._gameView.restartBtn
        
    def start( self ):
        ''' Starts drawing. '''
        self.window.mainloop()
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Draws the current state (data) on the canvas. '''
        
        # Set window title with current frames per second.
        self.window.title( data.windowTitle.format(data.level.name, data.fps) )
        
        # Show game view.
        self._gameView.show( data )