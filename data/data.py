from common import vector2d

class Data:
    ''' This class represents all the data available in the game. This is equivalent to 
    the current state. 
    
    Member:
    players -- List of player objects (data.movable).
    '''

    players = []
    
    def __init__( self ):
        ''' Test: 
        >>> d = Data()
        >>> len(d.players)
        0
        '''
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()