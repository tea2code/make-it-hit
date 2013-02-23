import math

def floatEqual( a, b, epsilon ):
    ''' Compares to floats with a given epsilon. Normaly you should use 0.001.

    Test:
    >>> floatEqual( 0, 0, 0.001 )
    True
    >>> floatEqual( 0.0000, 0.0000, 0.001 )
    True
    >>> floatEqual( 1, 0, 0.001 )
    False
    >>> floatEqual( 0.0, 0.00001, 0.001 )
    False
    >>> floatEqual( 4.00001, 4.00001, 0.001 )
    True
    >>> floatEqual( 125352.00001, 125352.00001, 0.001 )
    True'''
    absA = math.fabs( a )
    absB = math.fabs( b )
    diff = math.fabs( a - b )

    # Shortcut, handles infinities.
    if a == b:
        return True
    # One or both are zero.
    elif a * b == 0:
        # Relative error is not meaningful here.
        return diff < (epsilon * epsilon)
    # Use relative error.
    else:
        return diff / (absA + absB) < epsilon

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