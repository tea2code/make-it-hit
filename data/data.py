from data import vector2d
from common import enum

class Data:
    ''' This class represents all the data available in the game. This is equivalent to 
    the current state. 
    
    Constants:
    STATES -- Possible game states (enum).
    
    Member:
    deltaTime -- The time difference since the last step (float).
    events -- List of events in this frame (data.event).
    fps -- The current frame rate (int).
    level -- The level to play (data.level).
    levelDetails -- Name of the level to show details of (string).
    levelDir -- The level directory (string).
    levelExtension -- The file extension of level files with dot (string).
    levelList -- List of level paths to load next. Current is the first entry (string).
    mousePosition -- The current mouse position if pressed (data.vector2d).
    mousePressed -- True if mouse button is pressed (boolean).
    points -- Number of points (int).
    screenXCoefficient -- Coefficient for world to screen conversion in x direction (float).
    screenYCoefficient -- Coefficient for world to screen conversion in y direction (float).
    state -- The current game state (enum).
    startTime -- Time before level starts in milliseconds (int).
    time -- The accumulated time of all steps in seconds (float).
    windowHeight -- The height of the window (int).
    windowTitle -- Template for window title (string).
    windowWidth -- The width of the window (int).
    _borders -- List of rectangles representing the borders (data.rect). 
    '''
    
    STATES = enum.createSeq( 'MENU_MAIN', 'MENU_NEW', 'MENU_NEW_DETAILS', 
                             'LOADING', 'STARTING', 'PLAYING', 'VICTORY', 'GAMEOVER',
                             'QUIT', )
    
    def __init__( self ):
        ''' Test: 
        >>> d = Data()
        >>> d.deltaTime
        0
        >>> len(d.events)
        0
        >>> d.fps
        0
        >>> d.level
        >>> d.levelDetails
        ''
        >>> d.levelDir
        ''
        >>> d.levelExtension
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
        >>> d.startTime
        0
        >>> d.time
        0
        >>> d.windowHeight
        0
        >>> d.windowTitle
        ''
        >>> d.windowWidth
        0
        >>> len(d._borders)
        0
        '''
        self.deltaTime = 0
        self.events = []
        self.fps = 0
        self.level = None
        self.levelDetails = ''
        self.levelDir = ''
        self.levelExtension = ''
        self.levelList = []
        self.mousePosition = vector2d.Vector2d.nullVector()
        self.mousePressed = False
        self.points = 0
        self.screenXCoefficient = 1
        self.screenYCoefficient = 1
        self.state = None
        self.startTime = 0
        self.time = 0
        self.windowHeight = 0
        self.windowTitle = ''
        self.windowWidth = 0
        self._borders = []
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()