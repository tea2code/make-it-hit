from common import tickable
from graphics import tkborderdrawer
from graphics import tkdrawerfactory

import tkinter

class TkGraphics( tickable.Tickable ):
    ''' This class handles the visualization of the current state. 
    
    Member:
    canvas -- The canvas object (Canvas).
    window -- The window object (Tk).
    '''
    
    def __init__( self, data ):
        ''' The parameter data which contains the window settings. '''
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas( self.window, width = data.level.map.width, 
                                      height = data.level.map.height )
        self.canvas.config( background = 'white' )
        self.canvas.pack()
        
    def after( self, time, function ):
        ''' Calls function after time in milliseconds. '''
        self.canvas.after( time, function )
        
    def start( self ):
        ''' Starts drawing. '''
        self.window.mainloop()
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Draws the current state (data) on the canvas. '''
        
        # Reset everything.
        self.canvas.delete( tkinter.ALL )
        
        # Set window title with current frames per second.
        self.window.title( data.windowTitle.format(data.level.name, data.fps) )
        
        # Draw border.
        drawer = tkborderdrawer.TkBorderDrawer( data.level.map.border )
        drawer.draw( self.canvas )
        
        # Drawer factory.
        drawerFactory = tkdrawerfactory.TkDrawerFactory()
        
        # Draw objects.
        for object in data.level.map.objects:
            drawer = drawerFactory.createFrom( object )
            drawer.draw( self.canvas )
        
        # Draw targets.
        for target in data.level.map.targets:
            drawer = drawerFactory.createFrom( target.object )
            drawer.draw( self.canvas )
        
        # Draw player.
        drawer = drawerFactory.createFrom( data.level.map.player )
        drawer.draw( self.canvas )
        
        # Draw collisions.
        #for event in data.events:
        #    if isinstance( event, collisionevent.CollisionEvent ):
        #        drawer = tkcollisiondrawer.TkCollisionDrawer( event, drawerFactory )
        #        drawer.color = 'red'
        #        drawer.fill = 'red'
        #        drawer.line = 2
        #        drawer.draw( self.canvas )
        
        # Draw input vector.
        if data.mousePressed:
            self.canvas.create_line( data.level.map.player.position.x, 
                                     data.level.map.player.position.y, 
                                     data.mousePosition.x , data.mousePosition.y, 
                                     arrow = 'last', fill = 'blue' )