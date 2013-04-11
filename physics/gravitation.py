class Gravitation:
    ''' Calculates gravitational force between two objects according to Newton's law of universal 
    gravitation. 
    
    Constants:
    GRAVITATIONAL_CONSTANT -- The gravitational constant (float).
    '''
    
    GRAVITATIONAL_CONSTANT = 6.67384 * 10**-11
    
    def calcForce( self, mass1, mass2, distance ):
        ''' Calculate gravitational force using F = G * (m1 * m2) / r^2
        
        Test:
        >>> g = Gravitation()
        >>> result = g.calcForce( 3530001000, 201820000, 725 )
        >>> print( '{:.2f}'.format(result) )
        90.46
        '''
        return self.GRAVITATIONAL_CONSTANT * (mass1 * mass2) / distance**2
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()