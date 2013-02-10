from data import vector2d

class TkInput():
    ''' This class handles input events from tkinter. 
    
    Member:
    data -- The data object.
    forceScale -- Scaling factor for force vector.
    '''
    
    data = None
    forceScale = 1
    
    def __init__( self, data, window ):
        ''' Initializes input module with the data object and binds input event callbacks 
        to window. '''
        self.data = data
        window.bind( '<B1-Motion>', self.__mouseMotion )
        window.bind( '<ButtonPress-1>', self.__mousePressed )
        window.bind( '<ButtonRelease-1>', self.__mouseReleased )
    
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
        
        # Check if level already exists.
        if self.data.level is None:
            return
        
        # Calculate force vector.
        force = self.data.mousePosition - self.data.level.map.player.position
        force = force * self.forceScale
        self.data.level.map.player.addForce( force )
        
    def __storeMousePos( self, event ):
        ''' Stores the mouse position of an event in data. '''
        self.data.mousePosition.x = event.x
        self.data.mousePosition.y = event.y