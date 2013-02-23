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
        canvas.create_oval( self.x - self.radius, self.y - self.radius, 
                            self.x + self.radius, self.y + self.radius, 
                            width = self.line, fill = self.fill, outline = self.color )

if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()