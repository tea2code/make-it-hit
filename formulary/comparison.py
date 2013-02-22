import math
import sys

def epsilon():
    ''' Epsilon value you should use for comparison of floats. '''
    return sys.float_info.epsilon

def floatEqual( a, b, epsilon ):
    ''' Compares to floats with a given epsilon. Normaly you should use epsilon().

    Test:
    >>> floatEqual( 0, 0, epsilon() )
    True
    >>> floatEqual( 0.0000, 0.0000, epsilon() )
    True
    >>> floatEqual( 1, 0, epsilon() )
    False
    >>> floatEqual( 0.0, 0.00001, epsilon() )
    False
    >>> floatEqual( 4.00001, 4.00001, epsilon() )
    True
    >>> floatEqual( 125352.00001, 125352.00001, epsilon() )
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