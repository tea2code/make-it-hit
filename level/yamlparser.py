from level import levelparser

import yaml  

class YamlParser(levelparser.LevelParser):
    ''' This parser creates a representation of a yaml map.  
    
    Constants:
    TAG_ANGLE -- Angle element.
    TAG_AUTHOR -- Author element.
    TAG_BORDER -- Border element.
    TAG_CIRCLE -- Circle element.
    TAG_DATE -- Date element.
    TAG_DESCRIPTION -- Description element.
    TAG_HEIGHT -- Height element.
    TAG_LEVEL -- Root/level element.
    TAG_MAP -- Map element.
    TAG_NAME -- Name element.
    TAG_OBJECTS -- Objects element.
    TAG_PARSER -- Parser version of this level.
    TAG_PLAYER -- Player element.
    TAG_POINTS -- Points element.
    TAG_RADIUS -- Radius element.
    TAG_RECT -- Rectangle element.
    TAG_TARGET -- Target element.
    TAG_TARGETS -- Targets element.
    TAG_TIMELIMIT -- Time limit element.
    TAG_VERSION -- Version element.
    TAG_WIDTH -- Width element.
    TAG_X -- X element.
    TAG_Y -- Y element.
    
    Member:
    level -- The resulting level object.
    supportedParser -- List of supported parser versions
    _errorInteger -- Text template for not an integer error.
    _errorMissing -- Text template for missing element error.
    '''
    
    TAG_ANGLE = 'angle'
    TAG_AUTHOR = 'author'
    TAG_BORDER = 'border'
    TAG_DATE = 'date'
    TAG_CIRCLE = 'circle'
    TAG_DESCRIPTION = 'description'
    TAG_HEIGHT = 'height'
    TAG_LEVEL = 'level'
    TAG_MAP = 'map'
    TAG_NAME = 'name'
    TAG_OBJECTS = 'objects'
    TAG_PARSER = 'parser'
    TAG_PLAYER = 'player'
    TAG_POINTS = 'points'
    TAG_RADIUS = 'radius'
    TAG_RECT = 'rect'
    TAG_TARGET = 'target'
    TAG_TARGETS = 'targets'
    TAG_TIMELIMIT = 'timelimit'
    TAG_VERSION = 'version'
    TAG_WIDTH = 'width'
    TAG_X = 'x'
    TAG_Y = 'y'

    def __init__( self ):
        ''' Test:
        >>> l = LevelParser()
        >>> l.level
        '''
        self.level = None
        self.supportedParser = ['2']
        self._errorInteger = 'Element "{0}" must be an integer.'
        self._errorMissing = 'Missing element "{0}".'
        
    def parse( self, fileName ):
        ''' Parses a level file. Throws YAMLError or level.levelparsererror. Returns the resulting level object. '''
        
        file = open( fileName, 'r' )
        raw = yaml.safe_load( file )
        print( raw )
        
        return self.level