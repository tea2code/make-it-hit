from data import vector2d
from common import enum

class Data:
    ''' This class represents all the data available in the game. This is equivalent to 
    the current state. 
    
    Constants:
    STATES -- Possible game states (enum).
    
    Member:
    configuration -- The configuration (Configuration).
    deltaTime -- The time difference since the last step (float).
    events -- List of events in this frame (data.event).
    fps -- The current frame rate (int).
    level -- The level to play (data.level).
    levelDetails -- Name of the level to show details of (string).
    levelList -- List of level paths to load next. Current is the first entry (string).
    mousePosition -- The current mouse position if pressed (data.vector2d).
    mousePressed -- True if mouse button is pressed (boolean).
    points -- Number of points (int).
    screenXCoefficient -- Coefficient for world to screen conversion in x direction (float).
    screenYCoefficient -- Coefficient for world to screen conversion in y direction (float).
    state -- The current game state (enum).
    time -- The accumulated time of all steps in seconds (float).
    _borders -- List of rectangles representing the borders (data.rect). 
    '''
    
    STATES = enum.createSeq( 'MENU_MAIN', 'MENU_NEW', 'MENU_NEW_DETAILS', 
                             'LOADING', 'STARTING', 'PLAYING', 'VICTORY', 'GAMEOVER',
                             'QUIT', )
    
    def __init__( self ):
        ''' Test: 
        >>> d = Data()
        >>> d.configuration
        >>> d.deltaTime
        0
        >>> len(d.events)
        0
        >>> d.fps
        0
        >>> d.level
        >>> d.levelDetails
        ''
        >>> len(d.levelList)
        0
        >>> d.mousePosition.x == 0 and d.mousePosition.y == 0
        True
        >>> d.mousePressed
        False
        >>> d.points
        0
        >>> d.screenXCoefficient
        1
        >>> d.screenYCoefficient
        1
        >>> d.state
        >>> d.time
        0
        >>> len(d._borders)
        0
        '''
        self.configuration = None
        self.deltaTime = 0
        self.events = []
        self.fps = 0
        self.level = None
        self.levelDetails = ''
        self.levelList = []
        self.mousePosition = vector2d.Vector2d.nullVector()
        self.mousePressed = False
        self.points = 0
        self.screenXCoefficient = 1
        self.screenYCoefficient = 1
        self.state = None
        self.time = 0
        self._borders = []
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()