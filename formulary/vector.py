﻿from formulary import comparison
from formulary import pythagorean

import math

def reflectAtLine( x1, y1, x2, y2, x3, y3 ):
    ''' Reflects vector 1 at the line between vectors 2 and 3. Returns the x-component 
    and y-component of the reflected vector in this order: reflectAtLine() => x, y

    Parameter:
    x1 -- The x-coordinate of the vector to reflect.
    y1 -- The y-coordinate of the vector to reflect.
    x2 -- The x-coordinate of the first point of the line.
    y2 -- The y-coordinate of the first point of the line.
    x3 -- The x-coordinate of the second point of the line.
    y3 -- The y-coordinate of the second point of the line.
    
    Test:
    >>> x, y = reflectAtLine( -2, -7, -2, 3, 4, -2 )
    >>> print( '{0:.2f}, {1:.2f}'.format(x, y) )
    6.52, 3.23
    >>> x, y = reflectAtLine( -4, 2, 0, -2, 0, 2 )
    >>> print( '{0:.2f}, {1:.2f}'.format(x, y) )
    4.00, 2.00
    '''
    # Vector between both points aka the line.
    dx = x3 - x2
    dy = y3 - y2
    
    # Calculate normal with unit length.
    length = pythagorean.solveC( dy, dx )
    nx = -dy
    ny = dx

    if not comparison.floatEqual( length, 0, 0.00001 ):
        nx /= length
        ny /= length
    
    # Dot product of vector 1 and normal.
    dotProduct = x1 * nx + y1 * ny
    
    # The reflected vector.
    x = x1 - 2 * nx * dotProduct
    y = y1 - 2 * ny * dotProduct
    
    return x, y
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()