from graphics import viewhandler

import tkinter

class MenuView( viewhandler.ViewHandler ):
    ''' The in menu view.
    
    Member:
    newGameBtn -- The new game button (Button).
    visible -- True if view is visible else false (boolean).
    quitBtn -- The button to quit the game (Button).
    _frame -- The menu frame (Frame).
    _spacers -- List of empty spacer labels (Label).
    ''' 
    
    def __init__( self, data, window ):
        ''' Add menu to given window. '''
        
        self.spacers = []
        
        self._frame = tkinter.Frame( window, height = data.windowHeight,
                                     width = data.windowWidth )
        self._frame.config( background = 'white', pady = data.windowHeight / 2 - 50 ) # TODO pady to center is hacky.
        self._frame.pack_propagate(0)
        
        self._menuFrame = tkinter.Frame( self._frame )
        self._menuFrame.config( background = 'white' )
        self._menuFrame.pack()
        
        self.newGameBtn = tkinter.Button( self._menuFrame, text = 'New Game' )
        self.newGameBtn.config( background = 'white', width = 20 )
        self.newGameBtn.pack()
        
        self.spacers.append( tkinter.Label(self._menuFrame, background = 'white').pack() )
        
        self.quitBtn = tkinter.Button( self._menuFrame, text = 'Quit' )
        self.quitBtn.config( background = 'white', width = 20 )
        self.quitBtn.pack()
        
        self.visible = False
    
    def hide( self, data ):
        ''' Hides the menu. '''
        
        if self.visible:
            self.visible = False
            self._frame.pack_forget()
    
    def show( self, data ):
        ''' Shows the menu. '''
        
        if not self.visible:
            self.visible = True
            self._frame.pack()