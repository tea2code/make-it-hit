from . import circledrawer
from common import tickable
from data import circle

import tkinter

class TkGraphics( tickable.Tickable ):
    ''' This class handles the visualisation of the current state. 
    
    Member:
    canvas -- The canvas object.
    window -- The window object.
    '''
    
    window = None
    canvas = None
    
    def __init__( self, data ):
        ''' The parameter data which contains the window settings. '''
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas( self.window )
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
        
        # Draw players.
        for p in data.players:
            if isinstance( p, circle.Circle ):
                drawer = circledrawer.CircleDrawer( p.position.x, p.position.y, p.radius )
                drawer.draw( self.canvas )
            else:
                raise TypeError( 'Unknown player object "{0}" in data.'.format(p) )