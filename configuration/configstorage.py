from data import configuration

import yaml

class ConfigStorage():
    ''' Class to load and save configuration. It uses a default configuration which can be 
    overridden by a specific configuration. 
    
    Constants:
    TAG_FORCE_SCALE -- Force scale element.
    TAG_FRAMES_PER_SECOND -- Frames per second element.
    TAG_LEVEL_DIR -- Level directory element.
    TAG_LEVEL_EXTENSION -- Level extension element.
    TAG_MENU_BAR_WIDTH -- Menu bar width element.
    TAG_START_TIME -- Start time element.
    TAG_WINDOW_HEIGHT -- Window height element.
    TAG_WINDOW_TITLE --Window title element.
    TAG_WINDOW_WIDTH -- Window width element.
    
    Member:
    defaultFilePath -- The path of the default configuration file (string). 
    filePath -- The path of the specific configuration file (string) .
    '''
    
    TAG_FORCE_SCALE = 'forceScale'
    TAG_FRAMES_PER_SECOND = 'framesPerSecond'
    TAG_LEVEL_DIR = 'levelDir'
    TAG_LEVEL_EXTENSION = 'levelExtension'
    TAG_MENU_BAR_WIDTH = 'menuBarWidth'
    TAG_START_TIME = 'startTime'
    TAG_WINDOW_HEIGHT = 'windowHeight'
    TAG_WINDOW_TITLE = 'windowTitle'
    TAG_WINDOW_WIDTH = 'windowWidth'
    
    def __init__( self, defaultFilePath, filePath ):
        ''' Set default file and override file. '''
        self._defaultFilePath = defaultFilePath
        self._filePath = filePath
    
    def load( self ):
        ''' Loads and returns the configuration. '''
        return self.__loadDefault()
        
    def save( self, configuration ):
        ''' Saves/Stores configuration. '''
        pass
        
    def __loadDefault( self ):
        ''' Loads and returns default configuration. '''
        file = open( self._defaultFilePath, 'r' )
        root = yaml.safe_load( file )
        
        config = configuration.Configuration()
        config.forceScale = root[self.TAG_FORCE_SCALE]
        config.framesPerSecond = root[self.TAG_FRAMES_PER_SECOND]
        config.levelDir = root[self.TAG_LEVEL_DIR]
        config.levelExtension = root[self.TAG_LEVEL_EXTENSION]
        config.menuBarWidth = root[self.TAG_MENU_BAR_WIDTH]
        config.startTime = root[self.TAG_START_TIME]
        config.windowHeight = root[self.TAG_WINDOW_HEIGHT]
        config.windowTitle = root[self.TAG_WINDOW_TITLE]
        config.windowWidth = root[self.TAG_WINDOW_WIDTH]
        return config