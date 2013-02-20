from common import tickable
from data import vector2d
from data import victoryevent

class TkInput( tickable.Tickable ):
    ''' This class handles input events from tkinter. 
    
    Member:
    data -- The data object.
    forceScale -- Scaling factor for force vector.
    _active -- If true forces will be added.
    '''
    
    data = None
    forceScale = 1
    _active = True
    
    def __init__( self, data, window ):
        ''' Initializes input module with the data object and binds input event callbacks 
        to window. '''
        self.data = data
        window.bind( '<B1-Motion>', self.__mouseMotion )
        window.bind( '<ButtonPress-1>', self.__mousePressed )
        window.bind( '<ButtonRelease-1>', self.__mouseReleased )
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Checks for end of game. Should be executed just before any event cleanup. '''
        
        # Event handling:
        for event in data.events:
            # Victory events.
            if isinstance( event, victoryevent.VictoryEvent ):
                self._active = False
    
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
        
        if not self._active:
            return;
        
        # Calculate force vector.
        force = self.data.mousePosition - self.data.level.map.player.position
        force = force * self.forceScale
        self.data.level.map.player.addForce( force )
        
    def __storeMousePos( self, event ):
        ''' Stores the mouse position of an event in data. '''
        self.data.mousePosition.x = event.x
        self.data.mousePosition.y = event.y