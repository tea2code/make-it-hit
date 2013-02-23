from graphics import tkdrawer

class TkCollisionDrawer( tkdrawer.TkDrawer ):
    ''' Drawer for collisions.

    Member:
    drawerFactory -- A instance of a drawer factory (graphics.tkdrawerfactory)
    event -- The collision event (data.collisionevent)
    '''
    
    def __init__( self, event, drawerFactory ):
        ''' Initializes the drawer with the collision event and a drawer factory for the collision
        object.
        
        Test:
        >>> r = TkCollisionDrawer( None, None )
        >>> r.drawerFactory
        >>> r.event
        '''
        super().__init__()
        self.drawerFactory = drawerFactory
        self.event = event

    def draw( self, canvas ):
        # Draw collision object.
        drawer = self.drawerFactory.createFrom( self.event.object )
        drawer.color = self.color
        drawer.fill = self.fill
        drawer.line = self.line
        drawer.draw( canvas )
        
        # Draw collision point marker.
        canvas.create_line( self.event.x - 10, self.event.y,
                            self.event.x + 10, self.event.y, 
                            width = self.line, fill = self.fill )
        canvas.create_line( self.event.x, self.event.y - 10, 
                            self.event.x, self.event.y + 10, 
                            width = self.line, fill = self.fill )
        
        

if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()