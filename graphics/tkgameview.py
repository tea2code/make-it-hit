from formulary import screenconvert
from graphics import tkborderdrawer
from graphics import tkdrawerfactory
from graphics import viewhandler

import tkinter as tk

class TkGameView( viewhandler.ViewHandler ):
    ''' The in game view. 
    
    Member:
    canvas -- The canvas object (Canvas).
    menuBtn -- The button which leads back to the main menu (Button).
    restartBtn -- The restart button (Button).
    _barFrame -- The frame of the menu bar (Frame).
    _canvasFrame -- The frame of the canvas object (Frame).
    _descriptionLabel -- The description label (Label).
    _frame -- The main frame (Frame).
    _nameLabel -- The level name label (Label).
    _pointsLabel -- Label for points (Label).
    _spacers -- List of empty spacer labels (Label).
    _stateLabel -- Label to show the current state (Label).
    _timeLabel -- Label for rest game time (Label).
    '''
    
    def __init__( self, data, window ):
        ''' Inject canvas frame and menu frame in given window. Using data and menu bar width 
        for initial settings. '''

        menuBarWrapLength = data.configuration.menuBarWidth - 20

        self._frame = tk.Frame( window )
        self._frame.config( background = 'white' )

        # Create canvas on one side...
        self._canvasFrame = tk.Frame( self._frame )
        self._canvasFrame.pack( side = tk.LEFT )
        
        self.canvas = tk.Canvas( self._canvasFrame, height = data.configuration.windowHeight,
                                 width = data.configuration.windowWidth - data.configuration.menuBarWidth )
        self.canvas.config( background = 'white' )
        self.canvas.pack()
        
        # ...and the menu bar on the other.
        self._barFrame = tk.Frame( self._frame, width = data.configuration.menuBarWidth )
        self._barFrame.config( background = 'white' )
        self._barFrame.pack_propagate(0)
        self._barFrame.pack( side = tk.RIGHT, anchor = tk.N, fill = tk.Y, expand = 1 )
        
        # Add time and point labels to menu bar.
        self.spacers = []
        self.spacers.append( tk.Label(self._barFrame, background = 'white').pack() )
        
        self._timeLabel = tk.Label( self._barFrame, text = 'Time: -' )
        self._timeLabel.config( background = 'white' )
        self._timeLabel.pack()
        
        self._pointsLabel = tk.Label( self._barFrame, text = 'Points: -' )
        self._pointsLabel.config( background = 'white' )
        self._pointsLabel.pack()
        
        self._stateLabel = tk.Label( self._barFrame, text = 'Loading' )
        self._stateLabel.config( background = 'white', wraplength = menuBarWrapLength )
        self._stateLabel.pack()
        
        self.spacers.append( tk.Label(self._barFrame, background = 'white').pack() )
        
        self._nameLabel = tk.Label( self._barFrame, text = '' )
        self._nameLabel.config( background = 'white', font = {'weight': 'bold'},
                                wraplength = menuBarWrapLength )
        self._nameLabel.pack()
        
        self._descriptionLabel = tk.Label( self._barFrame, text = '' )
        self._descriptionLabel.config( background = 'white', justify = tk.LEFT,
                                       wraplength = menuBarWrapLength )
        self._descriptionLabel.pack()
        
        self.spacers.append( tk.Label(self._barFrame, background = 'white').pack() )
        self.spacers.append( tk.Label(self._barFrame, background = 'white').pack() )

        self.restartBtn = tk.Button( self._barFrame, text = 'Restart' )
        self.restartBtn.config( background = 'white', width = 10 )
        self.restartBtn.pack()
        
        self.spacers.append( tk.Label(self._barFrame, background = 'white').pack() )

        self.menuBtn = tk.Button( self._barFrame, text = 'Main Menu' )
        self.menuBtn.config( background = 'white', width = 10 )
        self.menuBtn.pack()
                
    def hide( self, data ):
        ''' Hide the game view. '''
        
        self._frame.pack_forget()
        
    def show( self, data ):
        ''' Show the given data in the in game view. '''
        
        self._frame.pack()
        
        if data.state is data.STATES.LOADING:
            return;
        
        # Reset everything.
        self.canvas.delete( tk.ALL )

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
            restTime = data.configuration.startTime
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
        
        # Update points.   
        self._pointsLabel.config( text = 'Points: ' + self.__formatPoints(data) )
        
        # Update time.
        if data.state in [data.STATES.PLAYING, data.STATES.STARTING]: 
            self._timeLabel.config( text = 'Time: ' + self.__formatTime(data) )
            
        # Update state label.
        if data.state is data.STATES.LOADING:
            self._stateLabel.config( text = 'Loading next level...' )
        
        elif data.state is data.STATES.STARTING:
            self._stateLabel.config( text = 'Starting level...' )
            
        elif data.state is data.STATES.PLAYING:
            self._stateLabel.config( text = 'Playing...' )
            
        elif data.state is data.STATES.VICTORY:
            self._stateLabel.config( text = 'Congratulations, you have won!' )
            
        elif data.state is data.STATES.GAMEOVER:
            self._stateLabel.config( text = 'Game Over, you lost!' )
            
        # Update level info.
        self._nameLabel.config( text = data.level.name )
        self._descriptionLabel.config( text = data.level.description )
            
        # Deactivate restart button if victory.
        if data.state is data.STATES.VICTORY:
            self.restartBtn.config( state = tk.DISABLED )
        else:
            self.restartBtn.config( state = tk.NORMAL )