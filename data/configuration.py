class Configuration:
    ''' This class represents the configuration. 
    
    Member:
    framesPerSecond -- The rate of frames per second which should be (int).
    forceScale -- Scaling factor for forces (float).
    levelDir -- Directory where levels can be found (string).
    levelExtension -- Extension of level files (string).
    menubarWidth -- Width of the in game menu bar (int).
    startTime -- Delay before a level begins in milliseconds (int).
    windowHeight -- Height of the window in pixel (int).
    windowTitle -- Title template for window title (string).
    windowWidth -- Width of the window in pixel (int).
    '''
    
    def __init__( self ):
        ''' Test:
        >>> c = Configuration()
        >>> c.framesPerSecond
        60
        >>> c.forceScale
        1
        >>> c.levelDir
        'levels'
        >>> c.levelExtension
        '.yaml'
        >>> c.menuBarWidth
        120
        >>> c.startTime
        1500
        >>> c.windowHeight
        768
        >>> c.windowTitle
        ''
        >>> c.windowWidth
        1024
        '''
        self.framesPerSecond = 60
        self.forceScale = 1
        self.levelDir = 'levels'
        self.levelExtension = '.yaml'
        self.menuBarWidth = 120
        self.startTime = 1500
        self.windowHeight = 768
        self.windowTitle = ''
        self.windowWidth = 1024
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()