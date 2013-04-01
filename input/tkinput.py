from formulary import screenconvert

class TkInput():
    ''' This class handles input events from tkinter. 
    
    Member:
    data -- The data object.
    forceScale -- Scaling factor for force vector.
    '''
    
    def __init__( self, data ):
        ''' Initializes input module with the data object. '''
        
        self.data = data
        self.forceScale = 1
    
    def bindMenuBtn( self, btn ):
        ''' Bind a menu button. '''
        btn.config( command = self.__menuBtnPressed )
    
    def bindNewGameBtn( self, btn ):
        ''' Bind a new game button. '''
        btn.config( command = self.__newGameBtnPressed )
    
    def bindQuitBtn( self, btn ):
        ''' Bind a quit button. '''
        btn.config( command = self.__quitBtnPressed )
    
    def bindRestartBtn( self, btn ):
        ''' Bind a restart button. '''
        btn.config( command = self.__restartBtnPressed )
    
    def bindWindow( self, window ):
        ''' Binds the window/canvas which should receive mouse input. '''
        window.bind( '<B1-Motion>', self.__mouseMotion )
        window.bind( '<ButtonPress-1>', self.__mousePressed )
        window.bind( '<ButtonRelease-1>', self.__mouseReleased )
        window.bind_all( 'r', self.__restartKeyPressed )
    
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
        self.data.state = self.data.STATES.MENU_READ_LEVELS
   
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
        
    def __storeMousePos( self, event ):
        ''' Stores the mouse position of an event in data. '''
        self.data.mousePosition.x = screenconvert.screenToWorld( event.x, 
                                                                 self.data.screenXCoefficient )
        self.data.mousePosition.y = screenconvert.screenToWorld( event.y, 
                                                                 self.data.screenYCoefficient )