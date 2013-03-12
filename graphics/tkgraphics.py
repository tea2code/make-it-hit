from common import tickable
from formulary import screenconvert
from graphics import tkborderdrawer
from graphics import tkdrawerfactory

import tkinter

class TkGraphics( tickable.Tickable ):
    ''' This class handles the visualization of the current state. 
    
    Member:
    canvas -- The canvas object (Canvas).
    menuBarWidth -- The width of the menu bar (int).
    window -- The window object (Tk).
    _barFrame -- The frame of the menu bar (Frame).
    _canvasFrame -- The frame of the canvas object (Frame).
    '''
    
    def __init__( self, data ):
        ''' The parameter data which contains the window settings. '''
        
        self.menuBarWidth = 100
        data.screenXCoefficient = (data.windowWidth - self.menuBarWidth) / data.level.map.width
        data.screenYCoefficient = data.windowHeight / data.level.map.height
        
        self.window = tkinter.Tk()
        
        self._canvasFrame = tkinter.Frame( self.window )
        self.canvas = tkinter.Canvas( self._canvasFrame, height = data.windowHeight,
                                      width = data.windowWidth - self.menuBarWidth  )
        self.canvas.config( background = 'white' )
        self.canvas.pack()
        self._canvasFrame.pack( side = tkinter.LEFT )
        
        self._barFrame = tkinter.Frame( self.window, height = data.windowHeight,
                                        width = self.menuBarWidth )
        self._barFrame.pack( side = tkinter.RIGHT )
        
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
        drawer = tkborderdrawer.TkBorderDrawer( data.level.map.height, data.level.map.width, 
                                                data.level.map.border )
        self.__initDrawer( drawer, data )
        drawer.draw( self.canvas )
        
        # Drawer factory.
        drawerFactory = tkdrawerfactory.TkDrawerFactory()
        
        # Draw objects.
        for object in data.level.map.objects:
            drawer = drawerFactory.createFrom( object )
            self.__initDrawer( drawer, data )
            drawer.draw( self.canvas )
        
        # Draw targets.
        for target in data.level.map.targets:
            drawer = drawerFactory.createFrom( target.object )
            self.__initDrawer( drawer, data )
            drawer.draw( self.canvas )
            x = drawer.worldToScreenX( target.object.position.x )
            y = drawer.worldToScreenY( target.object.position.y )
            self.canvas.create_text( x, y, text = '{0}'.format(target.points), fill = drawer.color )
        
        # Draw player.
        drawer = drawerFactory.createFrom( data.level.map.player )
        self.__initDrawer( drawer, data )
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
            color = 'blue'
            x0 = screenconvert.worldToScreen( data.level.map.player.position.x, data.screenXCoefficient )
            y0 = screenconvert.worldToScreen( data.level.map.player.position.y, data.screenYCoefficient )
            x1 = screenconvert.worldToScreen( data.mousePosition.x, data.screenXCoefficient )
            y1 = screenconvert.worldToScreen( data.mousePosition.y, data.screenYCoefficient )
            self.canvas.create_line( x0, y0, x1, y1, arrow = 'last', fill = color, width = 2 )
            
    def __initDrawer( self, drawer, data ):
        ''' Initializes drawer. '''
        drawer.screenXCoefficient = data.screenXCoefficient
        drawer.screenYCoefficient = data.screenYCoefficient