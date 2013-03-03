from graphics import tkdrawer

class TkBorderDrawer( tkdrawer.TkDrawer ):
    ''' Draws the border of a map. 
    
    Member:
    mapHeight -- The height of the map (int).
    mapWidth -- The width of the map (int).
    width -- The width of the border (int).
    '''
    
    def __init__( self, mapHeight, mapWidth, width ):
        ''' Test:
        >>> t = TkBorderDrawer( 100, 200, 10 )
        >>> t.mapHeight
        100
        >>> t.mapWidth
        200
        >>> t.width
        10
        '''
        super().__init__()
        self.mapHeight = mapHeight
        self.mapWidth = mapWidth
        self.width = width
        
    def draw( self, canvas ):
        if self.width < 0:
            return
        
        x0 = self.worldToScreenX( self.width )
        y0 = self.worldToScreenY( self.width )
        x1 = self.worldToScreenX( self.mapWidth - self.width )
        y1 = self.worldToScreenY( self.mapHeight - self.width )
        canvas.create_rectangle( x0, y0, x1, y1,
                                 width = self.line, fill = self.fill, outline = self.color )
     
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()