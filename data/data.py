from common import vector2d

class Data:
    ''' This class represents all the data available in the game. This is equivalent to 
    the current state. 
    
    Member:
    deltaTime -- The time difference since the last step (float).
    level -- The level to play (data.level).
    time -- The accumulated time of all steps (float).
    '''

    deltaTime = 0
    level = None
    time = 0
    
    def __init__( self ):
        ''' Test: 
        >>> d = Data()
        >>> d.deltaTime
        0
        >>> d.level
        >>> d.time
        0
        '''
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()