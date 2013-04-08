from formulary import screenconvert

import random
import tkinter as tk
import webbrowser

class TkInput():
    ''' This class handles input events from tkinter. 
    
    Member:
    data -- The data object (data.data).
    _lastLevelSelection -- Set with last selection in level list (set).
    _levelList -- The level list (ListBox).
    _numLevelsInput -- Input field for number of levels to use (Entry).
    _shuffleCheckVar -- Result variable for shuffle check box (IntVar).
    _startBtn -- The button to start the game (Button).
    _startDelayEntry -- Input field for start delay (Entry).
    _windowHeightEntry -- Input field for window height (Entry).
    _windowWidthEntry -- Input field for window width (Entry).
    '''
    
    def __init__( self, data ):
        ''' Initializes input module with the data object. '''
        
        self.data = data
        self._levelList = None
        self._lastLevelSelection = {}
        self._numLevelsInput = None
        self._shuffleCheckVar = None
        self._startBtn = None
        self._startDelayEntry = None
        self._windowHeightEntry = None
        self._windowWidthEntry = None
    
    def bindConfigBtn( self, button ):
        ''' Bind the configuration button. '''
        button.config( command = lambda: self.__setState(self.data.STATES.MENU_CONFIG) )
    
    def bindConfigInputs( self, startDelayEntry, windowHeightEntry, windowWidthEntry ):
        ''' Bind input fields of configuration view. '''
        self._startDelayEntry = startDelayEntry
        self._windowHeightEntry = windowHeightEntry
        self._windowWidthEntry = windowWidthEntry
    
    def bindHelpBtn( self, button ):
        ''' Bind the help button. '''
        button.config( command = lambda: webbrowser.open(self.data.configuration.homepage) )
    
    def bindLevelList( self, levelList ):
        ''' Bind the level list. '''
        self._levelList = levelList
        self._levelList.bind( '<<ListboxSelect>>', self.__levelListChanged )
        self._lastLevelSelection = set( self._levelList.curselection() )
        self.__setNumberOfLevels()
    
    def bindMenuBtn( self, button ):
        ''' Bind a menu button. '''
        button.config( command = lambda: self.__setState(self.data.STATES.MENU_MAIN) )
    
    def bindNewGameBtn( self, button ):
        ''' Bind a new game button. '''
        button.config( command = lambda: self.__setState(self.data.STATES.MENU_NEW) )
    
    def bindNumLevelsInput( self, entry ):
        ''' Bind the input field for number of levels. '''
        self._numLevelsInput = entry
        self.__setNumberOfLevels()
    
    def bindQuitBtn( self, button ):
        ''' Bind a quit button. '''
        button.config( command = lambda: self.__setState(self.data.STATES.QUIT) )
    
    def bindRestartBtn( self, button ):
        ''' Bind a restart button. '''
        button.config( command = self.__restart )
    
    def bindSaveConfigBtn( self, button ):
        ''' Bind the save configuration button. '''
        if self._startDelayEntry:
            self.data.configuration.startTime = int( self._startDelayEntry.get() )
        if self._windowHeightEntry:
            self.data.configuration.windowHeight = int( self._windowHeightEntry.get() )
        if self._windowWidthEntry:
            self.data.configuration.windowWidth = int( self._windowWidthEntry.get() )
        
        self.__setState( self.data.STATES.MENU_MAIN )
    
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
        window.bind( '<B1-Motion>', self.__storeMousePos )
        window.bind( '<ButtonPress-1>', self.__mousePressed )
        window.bind( '<ButtonRelease-1>', self.__mouseReleased )
        window.bind_all( 'r', self.__restart )
    
    def __levelListChanged( self, event ):
        ''' Handles changes in level list. '''
        newSelection = set( self._levelList.curselection() )
        diff = newSelection.symmetric_difference( self._lastLevelSelection )
        if diff:
            # Use int() cause ListBox returns integer or string as return value.
            self.data.levelDetails = self._levelList.get( int(diff.pop()) )
            self.__setState( self.data.STATES.MENU_NEW_DETAILS )
        self._lastLevelSelection = newSelection
        
        if self._startBtn and not newSelection:
            self._startBtn.config( state = tk.DISABLED )
        elif self._startBtn and newSelection:
            self._startBtn.config( state = tk.NORMAL )
    
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
        force = force * self.data.configuration.forceScale
        self.data.level.map.player.addForce( force )
   
    def __restart( self, event = None ):
        ''' Restarts game. '''
        if self.data.state is not self.data.STATES.VICTORY:
            self.__setState( self.data.STATES.LOADING )

    def __setNumberOfLevels( self ):
        ''' Sets number of levels in input field. '''
        
        if not self._numLevelsInput:
            return
        
        if not self._levelList:
            return
        
        self._numLevelsInput.delete( 0, tk.END )
        self._numLevelsInput.insert( 0, self._levelList.size() )
       
    def __setState( self, state ):
        ''' Helper function to set state in lambda functions. '''
        self.data.state = state
       
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
            
        self.__setState( self.data.STATES.LOADING )
        
    def __storeMousePos( self, event ):
        ''' Stores the mouse position of an event in data. '''
        self.data.mousePosition.x = screenconvert.screenToWorld( event.x, 
                                                                 self.data.screenXCoefficient )
        self.data.mousePosition.y = screenconvert.screenToWorld( event.y, 
                                                                 self.data.screenYCoefficient )