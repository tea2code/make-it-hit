from graphics import tkdrawer

class TkBorderDrawer( tkdrawer.TkDrawer ):
    ''' Draws the border of a map. 
    
    Member:
    width -- The width of the border.
    '''
    
    def __init__( self, width ):
        ''' Constructor which sets the width of the border.

        Test:
        >>> t = TkBorderDrawer( 10 )
        >>> t.width
        10
        '''
        super().__init__()
        self.width = width
        
    def draw( self, canvas ):
        if self.width < 0:
            return
        
        x0 = self.width
        y0 = self.width
        x1 = int( canvas.cget('width') ) - self.width
        y1 = int( canvas.cget('height') ) - self.width
        canvas.create_rectangle( x0, y0, x1, y1,
                                 width = self.line, fill = self.fill, outline = self.color )
     
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()