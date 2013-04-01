﻿from common import tickable
from graphics import gameview
from graphics import menuview

import tkinter as tk

class TkGraphics( tickable.Tickable ):
    ''' This class handles the visualization of the current state. 
    
    Member:
    canvas -- The canvas object (Canvas).
    restartBtn -- The restart button (Button).
    window -- The window object (Tk).
    _gameView -- The game view (GameView).
    _menuView -- The menu view (MenuView).
    '''
    
    def __init__( self, data ):
        ''' The parameter data which contains the window settings. '''
        
        # Create window.
        self.window = tk.Tk()
        self.window.config( background = 'white' )
        
        # Create views.
        self._gameView = gameview.GameView( data, self.window )
        self._menuView = menuview.MenuView( data, self.window )
        
    @property
    def backFromNewBtn( self ):
        return self._menuView.backBtn
        
    @property
    def canvas( self ):
        return self._gameView.canvas
    
    @property 
    def menuBtn( self ):
        return self._gameView.menuBtn
    
    @property 
    def newGameBtn( self ):
        return self._menuView.newGameBtn
    
    @property 
    def quitBtn( self ):
        return self._menuView.quitBtn
    
    @property
    def restartBtn( self ):
        return self._gameView.restartBtn
        
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
        self.window.title( data.windowTitle.format(viewDescription, data.fps) )
        
        if data.state in [data.STATES.MENU_MAIN, data.STATES.MENU_READ_LEVELS, data.STATES.MENU_NEW]:
            self._gameView.hide( data )
            self._menuView.show( data )
        else:
            self._menuView.hide( data )
            self._gameView.show( data )