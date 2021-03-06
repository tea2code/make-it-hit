﻿from formulary import rotation
from graphics import tkdrawer

class TkRectDrawer( tkdrawer.TkDrawer ):
    ''' Drawer for rectangles.

    Member:
    angle -- The angle in degree of the rectangle (float).
    height -- The height of the rectangle (int).
    width -- The width of the rectangle (int).
    x -- The x-component of the center of the rectangle (int).
    y -- The y-component of the center of the rectangle (int).
    '''
    
    def __init__( self, angle, height, width, x, y ):
        ''' Initializes the rect drawer.
        
        Test:
        >>> r = TkRectDrawer( 1, 2, 3, 4, 5 )
        >>> r.angle
        1
        >>> r.height
        2
        >>> r.width
        3
        >>> r.x
        4
        >>> r.y
        5
        '''
        super().__init__()
        self.angle = angle
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def draw( self, canvas ):
        heightHalf = self.height * 0.5
        widthHalf = self.width * 0.5
        xPlus = widthHalf
        xMinus = -widthHalf
        yPlus = heightHalf
        yMinus = -heightHalf
        
        # Point 0.
        x0 = rotation.rotateX( xMinus, yMinus, self.angle ) + self.x
        y0 = rotation.rotateY( xMinus, yMinus, self.angle ) + self.y
        
        # Point 1.
        x1 = rotation.rotateX( xPlus, yMinus, self.angle ) + self.x
        y1 = rotation.rotateY( xPlus, yMinus, self.angle ) + self.y
        
        # Point 2.
        x2 = rotation.rotateX( xPlus, yPlus, self.angle ) + self.x
        y2 = rotation.rotateY( xPlus, yPlus, self.angle ) + self.y
        
        # Point 3.
        x3 = rotation.rotateX( xMinus, yPlus, self.angle ) + self.x
        y3 = rotation.rotateY( xMinus, yPlus, self.angle ) + self.y
        
        # Draw.
        x0 = self.worldToScreenX( x0 )
        y0 = self.worldToScreenY( y0 )
        x1 = self.worldToScreenX( x1 )
        y1 = self.worldToScreenY( y1 )
        x2 = self.worldToScreenX( x2 )
        y2 = self.worldToScreenY( y2 )
        x3 = self.worldToScreenX( x3 )
        y3 = self.worldToScreenY( y3 )
        canvas.create_polygon( x0, y0, x1, y1, x2, y2, x3, y3, 
                               width = self.line, fill = self.fill, outline = self.color )

if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()