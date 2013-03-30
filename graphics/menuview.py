from graphics import viewhandler

import tkinter

class MenuView( viewhandler.ViewHandler ):
    ''' The in menu view.
    
    Member:
    backBtn -- The button which leads back to the main menu (Button).
    configBtn -- The button which opens the configuration menu (Button).
    newGameBtn -- The new game button (Button).
    quitBtn -- The button to quit the game (Button).
    startBtn -- The button to start the game (Button).
    _frame -- The menu frame (Frame).
    _frames -- List of frames which are not needed later (Frame).
    _levelList -- The list box containing all levels (ListBox).
    _mainMenuFrame -- The frame of the main menu (Frame).
    _newMenuFrame -- The frame of the new game menu (Frame).
    _scrollbar -- The scrollbar for the level list (Scrollbar).
    _spacers -- List of empty spacer labels (Label).
    ''' 
    
    def __init__( self, data, window ):
        ''' Add menu to given window. '''
        
        self._frames = []
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
        
        self.configBtn = tkinter.Button( self._mainMenuFrame, text = 'Configuration', state = tkinter.DISABLED )
        self.configBtn.config( background = 'white', width = 20 )
        self.configBtn.pack()
        
        self.spacers.append( tkinter.Label(self._mainMenuFrame, background = 'white').pack() )
        
        self.quitBtn = tkinter.Button( self._mainMenuFrame, text = 'Quit' )
        self.quitBtn.config( background = 'white', width = 20 )
        self.quitBtn.pack()
        
        # New Game Menu
        self._newMenuFrame = tkinter.Frame( self._frame )
        self._newMenuFrame.config( background = 'white' )
        
        levelFrame = tkinter.Frame( self._newMenuFrame )
        levelFrame.config( background = 'white' )
        levelFrame.pack( anchor = tkinter.W, fill = tkinter.Y, expand = 1 )
        self._frames.append( levelFrame )
        
        levelSelectionFrame = tkinter.Frame( levelFrame )
        levelSelectionFrame.config( background = 'white' )
        levelSelectionFrame.pack( side = tkinter.LEFT, 
                                  fill = tkinter.Y, expand = 1 )
        self._frames.append( levelSelectionFrame )
        
        self._scrollbar = tkinter.Scrollbar( levelSelectionFrame, orient = tkinter.VERTICAL )
        self._levelList = tkinter.Listbox( levelSelectionFrame, selectmode = tkinter.MULTIPLE, 
                                           width = 50, yscrollcommand = self._scrollbar.set )
        self._scrollbar.config( command = self._levelList.yview )
        self._levelList.pack( side = tkinter.LEFT, fill = tkinter.Y, expand = 1 )
        self._scrollbar.pack( fill = tkinter.Y, expand = 1 )
        
        spacerFrame = tkinter.Frame( levelFrame )
        spacerFrame.config( background = 'white', width = 30 )
        spacerFrame.pack( side = tkinter.LEFT )
        self._frames.append( spacerFrame )
        
        self._titleLabel = tkinter.Label( levelFrame, text = '<Title>' )
        self._titleLabel.config( background = 'white', font = (None, 16, 'bold') )
        self._titleLabel.pack( anchor = tkinter.N, side = tkinter.LEFT )
        
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
        
        self._frame.pack( side = tkinter.LEFT, fill = tkinter.BOTH, expand = 1 )
        
        if data.state is data.STATES.MENU_MAIN:
            self._newMenuFrame.pack_forget()
            self._mainMenuFrame.pack( side = tkinter.LEFT, fill = tkinter.X, expand = 1 )
            
        elif data.state in [data.STATES.MENU_NEW, data.STATES.MENU_NEW_DETAILS]:
            self._mainMenuFrame.pack_forget()
            self._newMenuFrame.pack( fill = tkinter.BOTH, expand = 1, padx = 10, pady = 10 )
            
            if not self._levelList.size():
                for level in data.levelList:
                    self._levelList.insert( tkinter.END, level )
                self._levelList.selection_set( 0, self._levelList.size() - 1 )