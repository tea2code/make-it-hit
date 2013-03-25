from graphics import viewhandler

import tkinter

class MenuView( viewhandler.ViewHandler ):
    ''' The in menu view.
    
    Member:
    newBtn -- The new game button (Button).
    visible -- True if view is visible else false (boolean).
    _frame -- The menu frame (Frame).
    ''' 
    
    def __init__( self, data, window ):
        ''' Add menu to given window. '''
        
        self._frame = tkinter.Frame( window, height = data.windowHeight,
                                     width = data.windowWidth )
        self._frame.config( background = 'white' )
        self._frame.pack_propagate(0)
        
        self.newBtn = tkinter.Button( self._frame, text = 'New Game' )
        self.newBtn.config( background = 'white', padx = 10 )
        self.newBtn.pack()
        
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