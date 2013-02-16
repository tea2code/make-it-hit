import math

def rotateX( x, y, angle ):
    ''' Rotates the x-component of a coordinate using the angle (degree). Positiv direction is 
    counterclock wise.

    Test:
    >>> print( '{0:.2f}'.format(rotateX(0, 1, 90)) )
    -1.00
    >>> print( '{0:.2f}'.format(rotateX(0, 1, 180)) )
    -0.00
    '''
    angleRadian = math.radians( angle )
    return x * math.cos( angleRadian ) - y * math.sin( angleRadian )
    
def rotateY( x, y, angle ):
    ''' Rotates the y-component of a coordinate using the angle (degree). Positiv direction is 
    counterclock wise.

    Test:
    >>> print( '{0:.2f}'.format(rotateY(0, 1, 90)) )
    0.00
    >>> print( '{0:.2f}'.format(rotateY(0, 1, 180)) )
    -1.00
    '''
    angleRadian = math.radians( angle )
    return y * math.cos( angleRadian ) + x * math.sin( angleRadian )
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()