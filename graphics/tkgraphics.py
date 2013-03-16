from common import tickable
from formulary import screenconvert
from graphics import tkborderdrawer
from graphics import tkdrawerfactory

import tkinter

class TkGraphics( tickable.Tickable ):
    ''' This class handles the visualization of the current state. 
    
    Member:
    canvas -- The canvas object (Canvas).
    window -- The window object (Tk).
    _barFrame -- The frame of the menu bar (Frame).
    _canvasFrame -- The frame of the canvas object (Frame).
    _pointsLabel -- Label for points (Label).
    _timeLabel -- Label for rest game time (Label).
    '''
    
    def __init__( self, data ):
        ''' The parameter data which contains the window settings. '''
        
        # Create window.
        self.window = tkinter.Tk()
        self.window.config( background = 'white' )
        
        # Create canvas on one side...
        self._canvasFrame = tkinter.Frame( self.window )
        self._canvasFrame.pack( side = tkinter.LEFT )
        self.canvas = tkinter.Canvas( self._canvasFrame, height = data.windowHeight,
                                      width = data.windowWidth  )
        self.canvas.config( background = 'white' )
        self.canvas.pack()
        
        # ...and the menu bar on the other.
        self._barFrame = tkinter.Frame( self.window )
        self._barFrame.config( background = 'white' )
        self._barFrame.pack( side = tkinter.RIGHT, anchor = tkinter.N )
        
        # Add time and point labels to menu bar.
        self._timeLabel = tkinter.Label( self._barFrame, text = "Time: -" )
        self._timeLabel.config( background = 'white', padx = 10 )
        self._timeLabel.pack()
        self._pointsLabel = tkinter.Label( self._barFrame, text = "Points: -" )
        self._pointsLabel.config( background = 'white', padx = 10 )
        self._pointsLabel.pack()
        
    def after( self, time, function ):
        ''' Calls function after time in milliseconds. '''
        self.canvas.after( time, function )
        
    def start( self ):
        ''' Starts drawing. '''
        self.window.mainloop()
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Draws the current state (data) on the canvas. '''
        
        if data.state is data.STATES.LOADING:
            return;
        
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
        
        # Update menu bar.   
        self._pointsLabel.config( text = "Points: " + self.__formatPoints(data) )
        if data.state is data.STATES.PLAYING: 
            self._timeLabel.config( text = "Time: " + self.__formatTime(data) )
     
    def __formatPoints( self, data ):
        ''' Formats current points from data and returns it as a string. '''
        return '{}'.format( data.points )
     
    def __formatTime( self, data ):
        ''' Formats the current game time from data and returns it as a string. '''
        currentTime = (data.level.timeLimit / 1000)  - data.time
        currentTime = max( currentTime, 0 )
        return '{:.2f}s'.format( currentTime )
            
    def __initDrawer( self, drawer, data ):
        ''' Initializes drawer. '''
        drawer.screenXCoefficient = data.screenXCoefficient
        drawer.screenYCoefficient = data.screenYCoefficient