from formulary import screenconvert

import random
import tkinter as tk

class TkInput():
    ''' This class handles input events from tkinter. 
    
    Member:
    data -- The data object (data.data).
    forceScale -- Scaling factor for force vector (float).
    _lastLevelSelection -- Set with last selection in level list (set).
    _levelList -- The level list (ListBox).
    _numLevelsInput -- Input field for number of levels to use (Entry).
    _shuffleCheckVar -- Result variable for shuffle check box (IntVar).
    _startBtn -- The button to start the game (Button).
    '''
    
    def __init__( self, data ):
        ''' Initializes input module with the data object. '''
        
        self.data = data
        self.forceScale = 1
        self._levelList = None
        self._lastLevelSelection = {}
        self._numLevelsInput = None
        self._shuffleCheckVar = None
        self._startBtn = None
    
    def bindLevelList( self, levelList ):
        ''' Bind the level list. '''
        self._levelList = levelList
        self._levelList.bind( '<<ListboxSelect>>', self.__levelListChanged )
        self._lastLevelSelection = set( self._levelList.curselection() )
        self.__setNumberOfLevels()
    
    def bindMenuBtn( self, button ):
        ''' Bind a menu button. '''
        button.config( command = self.__menuBtnPressed )
    
    def bindNewGameBtn( self, button ):
        ''' Bind a new game button. '''
        button.config( command = self.__newGameBtnPressed )
    
    def bindNumLevelsInput( self, input ):
        ''' Bind the input field for number of levels. '''
        self._numLevelsInput = input
        self.__setNumberOfLevels()
    
    def bindQuitBtn( self, button ):
        ''' Bind a quit button. '''
        button.config( command = self.__quitBtnPressed )
    
    def bindRestartBtn( self, button ):
        ''' Bind a restart button. '''
        button.config( command = self.__restartBtnPressed )
    
    def bindShuffleCheck( self, checkBox ):
        ''' Bind check box for shuffling. '''
        self._shuffleCheckVar = tk.IntVar()
        self._shuffleCheckVar.set( 1 )
        checkBox.config( variable = self._shuffleCheckVar )
    
    def bindStartBtn( self, button ):
        ''' Bind the start button. '''
        self._startBtn = button
        self._startBtn.config( command = self.__startBtnPressed )
    
    def bindWindow( self, window ):
        ''' Binds the window/canvas which should receive mouse input. '''
        window.bind( '<B1-Motion>', self.__mouseMotion )
        window.bind( '<ButtonPress-1>', self.__mousePressed )
        window.bind( '<ButtonRelease-1>', self.__mouseReleased )
        window.bind_all( 'r', self.__restartKeyPressed )
    
    def __levelListChanged( self, event ):
        ''' Handles changes in level list. '''
        newSelection = set( self._levelList.curselection() )
        diff = newSelection.symmetric_difference( self._lastLevelSelection )
        if diff:
            # Use int() cause ListBox returns integer or string as return value.
            self.data.levelDetails = self._levelList.get( int(diff.pop()) )
            self.data.state = self.data.STATES.MENU_NEW_DETAILS
        self._lastLevelSelection = newSelection
        
        if self._startBtn and not newSelection:
            self._startBtn.config( state = tk.DISABLED )
        elif self._startBtn and newSelection:
            self._startBtn.config( state = tk.NORMAL )
    
    def __menuBtnPressed( self ):
        ''' Handles pressing the main menu button. '''
        self.data.state = self.data.STATES.MENU_MAIN
    
    def __mouseMotion( self, event ):
        ''' Handles mouse motion while button is pressed. '''
        self.__storeMousePos( event )
    
    def __mousePressed( self, event ):
        ''' Handles mouse button pressed event. '''
        self.data.mousePressed = True
        self.__storeMousePos( event )
    
    def __mouseReleased( self, event ):
        ''' Handles mouse button pressed event. '''
        self.data.mousePressed = False

        if self.data.state is not self.data.STATES.PLAYING:
            return
        
        # Calculate force vector.
        force = self.data.mousePosition - self.data.level.map.player.position
        force = force * self.forceScale
        self.data.level.map.player.addForce( force )
   
    def __newGameBtnPressed( self ):
        ''' Handles pressing the new game button. '''
        self.data.state = self.data.STATES.MENU_NEW
   
    def __quitBtnPressed( self ):
        ''' Handles pressing the quit button. '''
        self.data.state = self.data.STATES.QUIT
   
    def __restart( self ):
        ''' Restarts game. '''
        if self.data.state is not self.data.STATES.VICTORY:
            self.data.state = self.data.STATES.LOADING
   
    def __restartBtnPressed( self ):
        ''' Handles pressing the restart button. '''
        self.__restart()
        
    def __restartKeyPressed( self, event ):
        ''' Handles pressing the restart key. '''
        self.__restart()
       
    def __setNumberOfLevels( self ):
        ''' Sets number of levels in input field. '''
        
        if not self._numLevelsInput:
            return
        
        if not self._levelList:
            return
        
        self._numLevelsInput.delete( 0, tk.END )
        self._numLevelsInput.insert( 0, self._levelList.size() )
       
    def __startBtnPressed( self ):
        ''' Handles pressing the start button. '''
        
        selection = self._levelList.curselection()
        if not selection:
            return
        
        levels = []
        for index in map( int, selection ):
            levels.append( self._levelList.get(index) )
        self.data.levelList = levels
        
        if self._shuffleCheckVar and self._shuffleCheckVar.get():
            random.shuffle( self.data.levelList )
            
            try:
                end = int( self._numLevelsInput.get() )
                self.data.levelList = self.data.levelList[ 0:end ]
            except Exception as e:
                print( e )
            
        self.data.state = self.data.STATES.LOADING
        
    def __storeMousePos( self, event ):
        ''' Stores the mouse position of an event in data. '''
        self.data.mousePosition.x = screenconvert.screenToWorld( event.x, 
                                                                 self.data.screenXCoefficient )
        self.data.mousePosition.y = screenconvert.screenToWorld( event.y, 
                                                                 self.data.screenYCoefficient )