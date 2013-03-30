from graphics import viewhandler

import tkinter

class MenuView( viewhandler.ViewHandler ):
    ''' The in menu view.
    
    Member:
    backBtn -- The button which leads back to the main menu (Button).
    newGameBtn -- The new game button (Button).
    quitBtn -- The button to quit the game (Button).
    startBtn -- The button to start the game (Button).
    _frame -- The menu frame (Frame).
    _levelFrame -- The frame containing the level selection (Frame).
    _mainMenuFrame -- The frame of the main menu (Frame).
    _newMenuFrame -- The frame of the new game menu (Frame).
    _spacers -- List of empty spacer labels (Label).
    ''' 
    
    def __init__( self, data, window ):
        ''' Add menu to given window. '''
        
        self.spacers = []
        
        self._frame = tkinter.Frame( window, height = data.windowHeight,
                                     width = data.windowWidth )
        self._frame.config( background = 'white' )
        self._frame.pack_propagate(0)
        
        # Main Menu
        self._mainMenuFrame = tkinter.Frame( self._frame )
        self._mainMenuFrame.config( background = 'white' )
        
        self.newGameBtn = tkinter.Button( self._mainMenuFrame, text = 'New Game' )
        self.newGameBtn.config( background = 'white', width = 20 )
        self.newGameBtn.pack()
        
        self.spacers.append( tkinter.Label(self._mainMenuFrame, background = 'white').pack() )
        
        self.quitBtn = tkinter.Button( self._mainMenuFrame, text = 'Quit' )
        self.quitBtn.config( background = 'white', width = 20 )
        self.quitBtn.pack()
        
        # New Game Menu
        self._newMenuFrame = tkinter.Frame( self._frame )
        self._newMenuFrame.config( background = 'white' )
        
        self._levelFrame = tkinter.Frame( self._newMenuFrame )
        self._levelFrame.config( background = 'white' )
        self._levelFrame.pack( fill = tkinter.BOTH, expand = 1 )
        
        self.backBtn = tkinter.Button( self._newMenuFrame, text = 'Back' )
        self.backBtn.config( background = 'white', width = 10 )
        self.backBtn.pack( side = tkinter.LEFT )
        
        self.startBtn = tkinter.Button( self._newMenuFrame, text = 'Start' )
        self.startBtn.config( background = 'white', width = 10 )
        self.startBtn.pack( side = tkinter.RIGHT )
    
    def hide( self, data ):
        ''' Hides the menu. '''

        self._frame.pack_forget()
    
    def show( self, data ):
        ''' Shows the menu. '''
        
        self._frame.pack()
        
        if data.state is data.STATES.MENU_MAIN:
            self._newMenuFrame.pack_forget()
            self._mainMenuFrame.pack( side = tkinter.LEFT, fill = tkinter.X, expand = 1 )
            
        elif data.state is data.STATES.MENU_NEW:
            self._mainMenuFrame.pack_forget()
            self._newMenuFrame.pack( fill = tkinter.BOTH, expand = 1, padx = 10, pady = 10 )