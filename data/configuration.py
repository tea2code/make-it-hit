class Configuration:
    ''' This class represents the configuration. 
    
    Member:
    forceScale -- Scaling factor for forces (float).
    framesPerSecond -- The rate of frames per second which should be (int).
    homepage -- Url of the homepage (string).
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
        >>> c.forceScale
        100
        >>> c.framesPerSecond
        60
        >>> c.homepage
        ''
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
        'Make It Hit - {0} (FPS: {1})'
        >>> c.windowWidth
        1024
        '''
        self.forceScale = 100
        self.framesPerSecond = 60
        self.homepage = ''
        self.levelDir = 'levels'
        self.levelExtension = '.yaml'
        self.menuBarWidth = 120
        self.startTime = 1500
        self.windowHeight = 768
        self.windowTitle = 'Make It Hit - {0} (FPS: {1})'
        self.windowWidth = 1024
     
    def __str__( self ):
        template = 'Configuration(forceScale {}, framesPerSecond {}, homepage {}, levelDir {}, ' \
                   'levelExtension {}, menuBarWidth {}, startTime {}, windowHeight {}, ' \
                   'windowTitle {}, windowWidth {})'
        return template.format( self.forceScale, self.framesPerSecond, self.homepage, self.levelDir,
                                self.levelExtension, self.menuBarWidth, self.startTime, 
                                self.windowHeight, self.windowTitle, self.windowWidth )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()