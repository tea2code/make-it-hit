from common import tickable
from formulary import screenconvert
from graphics import tkborderdrawer
from graphics import tkdrawerfactory

import tkinter

class TkGraphics( tickable.Tickable ):
    ''' This class handles the visualization of the current state. 
    
    Member:
    canvas -- The canvas object (Canvas).
    restartBtn -- The restart button (Button).
    window -- The window object (Tk).
    _barFrame -- The frame of the menu bar (Frame).
    _canvasFrame -- The frame of the canvas object (Frame).
    _pointsLabel -- Label for points (Label).
    _spacers -- List of empty spacer labels (Label).
    _stateLabel -- Label to show the current state (Label).
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
        self.spacers = []
        self.spacers.append( tkinter.Label(self._barFrame, background = 'white').pack() )
        
        self._timeLabel = tkinter.Label( self._barFrame, text = 'Time: -' )
        self._timeLabel.config( background = 'white', padx = 30 )
        self._timeLabel.pack()
        
        self._pointsLabel = tkinter.Label( self._barFrame, text = 'Points: -' )
        self._pointsLabel.config( background = 'white', padx = 30 )
        self._pointsLabel.pack()
        
        self._stateLabel = tkinter.Label( self._barFrame, text = 'Loading' )
        self._stateLabel.config( background = 'white' )
        self._stateLabel.pack()
        
        self.spacers.append( tkinter.Label(self._barFrame, background = 'white').pack() )

        self.restartBtn = tkinter.Button( self._barFrame, text = 'Restart' )
        self.restartBtn.config( background = 'white', padx = 10 )
        self.restartBtn.pack()
        
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

        self.__drawMap( data )
        self.__drawInput( data )
        self.__showControls( data )

    
    def __drawInput( self, data ):
        ''' Draw user interaction. '''
        # Draw input vector.
        
        if data.mousePressed and data.state in [data.STATES.STARTING, data.STATES.PLAYING]:
            color = 'blue'
            x0 = screenconvert.worldToScreen( data.level.map.player.position.x, data.screenXCoefficient )
            y0 = screenconvert.worldToScreen( data.level.map.player.position.y, data.screenYCoefficient )
            x1 = screenconvert.worldToScreen( data.mousePosition.x, data.screenXCoefficient )
            y1 = screenconvert.worldToScreen( data.mousePosition.y, data.screenYCoefficient )
            self.canvas.create_line( x0, y0, x1, y1, arrow = 'last', fill = color, width = 2 )
     
    def __drawMap( self, data ):
        ''' Draws map. '''
        # Draw border.
        drawer = tkborderdrawer.TkBorderDrawer( data.level.map.height, data.level.map.width, 
                                                data.level.map.border )
        self.__initDrawer( drawer, data )
        drawer.draw( self.canvas )
        
        # Drawer factory.
        drawerFactory = tkdrawerfactory.TkDrawerFactory()
        
        # Draw objects.
        for mapObject in data.level.map.objects:
            drawer = drawerFactory.createFrom( mapObject )
            self.__initDrawer( drawer, data )
            drawer.draw( self.canvas )
        
        # Draw targets.
        for target in data.level.map.targets:
            drawer = drawerFactory.createFrom( target.object )
            self.__initDrawer( drawer, data )
            drawer.draw( self.canvas )
            x = drawer.worldToScreenX( target.object.position.x )
            y = drawer.worldToScreenY( target.object.position.y )
            self.canvas.create_text( x, y, text = target.points, fill = drawer.color )
        
        # Draw player.
        drawer = drawerFactory.createFrom( data.level.map.player )
        self.__initDrawer( drawer, data )
        drawer.draw( self.canvas )
     
    def __formatPoints( self, data ):
        ''' Formats current points from data and returns it as a string. '''
        return '{}'.format( data.points )
     
    def __formatTime( self, data ):
        ''' Formats the current game time from data and returns it as a string. '''
        
        restTime = data.level.timeLimit
        if data.state is data.STATES.STARTING:
            restTime = data.startTime
        restTime /= 1000
        
        currentTime = restTime  - data.time
        currentTime = max( currentTime, 0 )
        return '{:.2f}s'.format( currentTime )
            
    def __initDrawer( self, drawer, data ):
        ''' Initializes drawer. '''
        drawer.screenXCoefficient = data.screenXCoefficient
        drawer.screenYCoefficient = data.screenYCoefficient
        
    def __showControls( self, data ):
        ''' Show window elements and controls. '''
        
        # Set window title with current frames per second.
        self.window.title( data.windowTitle.format(data.level.name, data.fps) )
        
        # Update menu bar.   
        self._pointsLabel.config( text = 'Points: ' + self.__formatPoints(data) )
        
        if data.state in [data.STATES.PLAYING, data.STATES.STARTING]: 
            self._timeLabel.config( text = 'Time: ' + self.__formatTime(data) )
            
        if data.state is data.STATES.LOADING:
            self._stateLabel.config( text = 'Loading next level...' )
        
        elif data.state is data.STATES.STARTING:
            self._stateLabel.config( text = 'Starting level...' )
            
        elif data.state is data.STATES.PLAYING:
            self._stateLabel.config( text = 'Playing...' )
            
        elif data.state is data.STATES.VICTORY:
            self._stateLabel.config( text = 'Congratulations,\n you have won!' )
            
        elif data.state is data.STATES.GAMEOVER:
            self._stateLabel.config( text = 'Game Over,\n you lost!' )