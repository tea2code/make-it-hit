from graphics import tkdrawer

class TkCircleDrawer( tkdrawer.TkDrawer ):
    ''' Drawer for circles.

    Member:
    radius -- The radius of the circle (float).
    x -- The x-component of the position of the circle (float).
    y -- The y-component of the position of the circle (float).
    '''
    
    def __init__( self, radius, x, y ):
        ''' Test:
        >>> c = TkCircleDrawer( 1, 2, 3 )
        >>> c.radius
        1
        >>> c.x
        2
        >>> c.y
        3
        '''
        super().__init__()
        self.radius = radius
        self.x = x
        self.y = y

    def draw( self, canvas ):
        x0 = self.worldToScreenX( self.x - self.radius )
        y0 = self.worldToScreenY( self.y - self.radius )
        x1 = self.worldToScreenX( self.x + self.radius )
        y1 = self.worldToScreenY( self.y + self.radius )
        canvas.create_oval( x0, y0, x1, y1, 
                            width = self.line, fill = self.fill, outline = self.color )

if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()