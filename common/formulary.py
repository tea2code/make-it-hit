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