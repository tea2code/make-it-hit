def createSeq(*sequential, **named):
    ''' Creates enum from given keys and adds sequential, numeric value beginning at 0. 
    
    Test:
    >>> enums = createSeq( 'A', 'B', 'C' )
    >>> enums.A
    0
    >>> enums.C
    2
    >>> enums.B
    1
    '''
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

def createFrom( **enums ):
    ''' Creates enum from given key-value-pairs. 
    
    Test:
    >>> enums = createFrom( ONE=1, TWO=2, THREE='three' )
    >>> enums.ONE
    1
    >>> enums.THREE
    'three'
    >>> enums.TWO
    2
    '''
    return type('Enum', (), enums)
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()