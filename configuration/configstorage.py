from data import configuration

import os
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
        # Load default config file.
        config = self.__loadDefault()
        
        # Check if user config file exists.
        if not os.path.isfile( self._filePath ):
            return config
        
        # Load user config file.
        with open( self._filePath, 'r' ) as file:
            root = yaml.safe_load( file )
        
        if self.TAG_FORCE_SCALE in root:
            config.forceScale = root[self.TAG_FORCE_SCALE]
            
        if self.TAG_FRAMES_PER_SECOND in root:
            config.framesPerSecond = root[self.TAG_FRAMES_PER_SECOND]
        
        if self.TAG_LEVEL_DIR in root:
            config.levelDir = root[self.TAG_LEVEL_DIR]
        
        if self.TAG_LEVEL_EXTENSION in root:
            config.levelExtension = root[self.TAG_LEVEL_EXTENSION]
        
        if self.TAG_MENU_BAR_WIDTH in root:
            config.menuBarWidth = root[self.TAG_MENU_BAR_WIDTH]
        
        if self.TAG_START_TIME in root:
            config.startTime = root[self.TAG_START_TIME]
        
        if self.TAG_WINDOW_HEIGHT in root:
            config.windowHeight = root[self.TAG_WINDOW_HEIGHT]
        
        if self.TAG_WINDOW_TITLE in root:
            config.windowTitle = root[self.TAG_WINDOW_TITLE]
        
        if self.TAG_WINDOW_WIDTH in root:
            config.windowWidth = root[self.TAG_WINDOW_WIDTH]
            
        return config
        
    def save( self, config ):
        ''' Saves/Stores configuration. '''
        # Load default config to compare with current and save only changed values.
        defaultConfig = self.__loadDefault()
        
        root = {}
        
        if config.forceScale != defaultConfig.forceScale:
            root[self.TAG_FORCE_SCALE] = config.forceScale
            
        if config.framesPerSecond != defaultConfig.framesPerSecond:
            root[self.TAG_FRAMES_PER_SECOND] = config.framesPerSecond
            
        if config.levelDir != defaultConfig.levelDir:
            root[self.TAG_LEVEL_DIR] = config.levelDir
            
        if config.levelExtension != defaultConfig.levelExtension:
            root[self.TAG_LEVEL_EXTENSION] = config.levelExtension
            
        if config.menuBarWidth != defaultConfig.menuBarWidth:
            root[self.TAG_MENU_BAR_WIDTH] = config.menuBarWidth
            
        if config.startTime != defaultConfig.startTime:
            root[self.TAG_START_TIME] = config.startTime
            
        if config.windowHeight != defaultConfig.windowHeight:
            root[self.TAG_WINDOW_HEIGHT] = config.windowHeight
            
        if config.windowTitle != defaultConfig.windowTitle:
            root[self.TAG_WINDOW_TITLE] = config.windowTitle
            
        if config.windowWidth != defaultConfig.windowWidth:
            root[self.TAG_WINDOW_WIDTH] = config.windowWidth
            
        if root:
            with open( self._filePath, 'w' ) as file:
                yaml.dump( root, file, default_flow_style = False )
        
    def __loadDefault( self ):
        ''' Loads and returns default configuration. '''
        with open( self._defaultFilePath, 'r' ) as file:
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