from . import vector2d

class Data:
    ''' This class represents all the data available in the game. This is equivalent to 
    the current state. 
    
    Member:
    deltaTime -- The time difference since the last step (float).
    fps -- The current frame rate (int).
    level -- The level to play (data.level).
    mousePosition -- The current mouse position if pressed.
    mousePressed -- True if mouse button is pressed.
    time -- The accumulated time of all steps (float).
    windowTitle -- Template for window title.
    '''

    deltaTime = 0
    fps = 0
    level = None
    mousePosition = vector2d.Vector2d.nullVector()
    mousePressed = False
    time = 0
    windowTitle = ''
    
    def __init__( self ):
        ''' Test: 
        >>> d = Data()
        >>> d.deltaTime
        0
        >>> d.fps
        0
        >>> d.level
        >>> d.mousePosition.x == 0 and d.mousePosition.y == 0
        True
        >>> d.mousePressed
        False
        >>> d.time
        0
        >>> d.windowTitle
        ''
        '''
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()