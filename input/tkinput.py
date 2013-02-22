from common import tickable
from data import vector2d

class TkInput( tickable.Tickable ):
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
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Checks for end of game.'''
        
        # Event handling:
        for event in data.events:
            # Collision events.
            if isinstance( event, collisionevent.CollisionEvent ):
                data.points -= 1
            
            # Target events.
            elif isinstance( event, targetevent.TargetEvent ):
                data.points += event.target.points
                print( 'Points: {0}'.format(data.points) )
    
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
        
    def __storeMousePos( self, event ):
        ''' Stores the mouse position of an event in data. '''
        self.data.mousePosition.x = event.x
        self.data.mousePosition.y = event.y