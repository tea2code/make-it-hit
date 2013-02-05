import graphics.tkdrawer as tkdrawer

class CircleDrawer( tkdrawer.TkDrawer ):
    ''' Drawer for circles.

    Member:
    radius -- The radius of the circle (float).
    x -- The x-component of the position of the circle (float).
    y -- The y-component of the position of the circle (float).
    '''
    
    radius = 1
    x = 0
    y = 0
    
    def __init__( self, radius, x, y ):
        ''' Test:
        >>> c = CircleDrawer( 1, 2, 3 )
        >>> c.radius
        1
        >>> c.x
        2
        >>> c.y
        3
        '''
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