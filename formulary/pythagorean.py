import math

def euclideanDistance( x1, y1, x2, y2 ):
    ''' Calculates the euclidean distance between two points in second dimension.

    Test:
    >>> print( '{0:.4f}'.format(euclideanDistance(2, -1, -2, 2)) )
    5.0000
    '''
    a = math.fabs( x1 - x2 )
    b = math.fabs( y1 - y2 )
    c = solveC( a, b )
    return c
  
def solveC( a, b ):
    ''' Calculates c of the pythagorean theorem: c² = a² + b² 
    
    Test:
    >>> print( '{0:.2f}'.format(solveC(2, 5)) )
    5.39
    >>> print( '{0:.2f}'.format(solveC(45.563, 131.34)) )
    139.02
    '''
    return math.sqrt( (a * a) + (b * b) )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()