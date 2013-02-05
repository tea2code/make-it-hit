from common import vector2d

class Data:
    ''' This class represents all the data available in the game. This is equivalent to 
    the current state. 
    
    Member:
    deltaTime -- The time difference since the last step (float).
    players -- List of player objects (data.movable).
    time -- The accumulated time of all steps (float).
    '''

    deltaTime = 0
    players = []
    time = 0
    
    def __init__( self ):
        ''' Test: 
        >>> d = Data()
        >>> d.deltaTime
        0
        >>> len(d.players)
        0
        >>> d.time
        0
        '''
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()