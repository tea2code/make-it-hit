from data import vector2d

def screenToWorld( coordinate, coefficient ):
    ''' Converts screen coordinate (int) to world coordinate (float) using the given 
    coefficient. The coefficient is the world to screen coefficient which will be converted.
    
    Test:
    >>> print( '{:.2f}'.format(screenToWorld(3.75, 0.625)) )
    6.00
    '''
    return coordinate / coefficient

def screenToWorldCoord( x, y, coefficientX, coefficientY ):
    ''' Converts screen coordinates (int) to world coordinates (float) using the given 
    coefficients. The coefficient is the world to screen coefficient which will be converted.
    
    Test:
    >>> x,y = screenToWorldCoord(3.75, 3.33, 0.625, 0.667)
    >>> print( '{:.2f}'.format(x) )
    6.00
    >>> print( '{:.2f}'.format(y) )
    4.99
    '''
    return screenToWorld( x, coefficientX ), screenToWorld( y, coefficientY )

def screenToWorldVector( vector, coefficientX, coefficientY ):
    ''' Converts screen coordinates (vector2d) to world coordinates (vector2d) using the 
    given coefficients. The coefficient is the world to screen coefficient which will be converted.
    
    Test:
    >>> v = screenToWorldVector(vector2d.Vector2d(3.75, 3.33), 0.625, 0.667)
    >>> print( '{:.2f}'.format(v.x) )
    6.00
    >>> print( '{:.2f}'.format(v.y) )
    4.99
    '''
    x = screenToWorld( vector.x, coefficientX )
    y = screenToWorld( vector.y, coefficientY )
    return vector2d.Vector2d( x, y )

def worldToScreen( coordinate, coefficient ):
    ''' Converts world coordinate (float) to screen coordinate (int) using the given 
    coefficient. The coefficient is the world to screen coefficient.
    
    Test:
    >>> print( '{:.2f}'.format(worldToScreen(6, 0.625)) )
    4.00
    '''
    return round(coordinate * coefficient)
  
def worldToScreenCoord( x, y, coefficientX, coefficientY ):
    ''' Converts world coordinates (float) to screen coordinates (int) using the given 
    coefficients. The coefficient is the world to screen coefficient.
    
    Test:
    >>> x,y = worldToScreenCoord(6.00, 4.99, 0.625, 0.667)
    >>> print( '{:.2f}'.format(x) )
    4.00
    >>> print( '{:.2f}'.format(y) )
    3.00
    '''
    return worldToScreen( x, coefficientX ), worldToScreen( y, coefficientY )
    
def worldToScreenVector( vector, coefficientX, coefficientY ):
    ''' Converts world coordinates (vector2d) to screen coordinates (vector2d) using the 
    given coefficients. The coefficient is the world to screen coefficient.
    
    Test:
    >>> v = worldToScreenVector(vector2d.Vector2d(6, 4.99), 0.625, 0.667)
    >>> print( '{:.2f}'.format(v.x) )
    4.00
    >>> print( '{:.2f}'.format(v.y) )
    3.00
    '''
    x = worldToScreen( vector.x, coefficientX )
    y = worldToScreen( vector.y, coefficientY )
    return vector2d.Vector2d( x, y )
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()