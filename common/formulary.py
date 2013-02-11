import math

def euclideanDistance( x1, y1, x2, y2 ):
    ''' Calculates the euclidean distance between two points in second dimension.

    Test:
    >>> print( '{0:.4f}'.format(euclideanDistance(2, -1, -2, 2)) )
    5.0000
    '''
    a = math.fabs( x1 - x2 )
    b = math.fabs( y1 - y2 )
    c = math.sqrt( (a * a) + (b * b) )
    return c
    
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

def stringIsFloat( string ):
    ''' Checks if a string is a integer.

    Test: 
    >>> stringIsFloat( '1' )
    True
    >>> stringIsFloat( '1427' )
    True
    >>> stringIsFloat( '-1' )
    True
    >>> stringIsFloat( '-1427' )
    True
    >>> stringIsFloat( '1.0' )
    True
    >>> stringIsFloat( '1337.536' )
    True
    >>> stringIsFloat( '-153.0563' )
    True
    >>> stringIsFloat( 'abc' )
    False
    >>> stringIsFloat( '1a' )
    False
    >>> stringIsFloat( '1,31434' )
    False
    >>> stringIsFloat( '1.341a' )
    False
    >>> stringIsFloat( '1314.142.' )
    False
    '''
    try:
        float( string )
        return True
    except ValueError:
        return False

def stringIsInt( string ):
    ''' Checks if a string is a integer.

    Test: 
    >>> stringIsInt( '1' )
    True
    >>> stringIsInt( '1427' )
    True
    >>> stringIsInt( '-1' )
    True
    >>> stringIsInt( '-1427' )
    True
    >>> stringIsInt( '1.0' )
    False
    >>> stringIsInt( '-1.0' )
    False
    >>> stringIsInt( 'abc' )
    False
    >>> stringIsInt( '1a' )
    False
    '''
    try:
        int( string )
        return True
    except ValueError:
        return False
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()