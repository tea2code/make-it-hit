from data import vector2d
from data import circle
from data import level
from data import map
from data import rect
from data import target
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
        >>> l = YamlParser()
        >>> l.level
        '''
        self.level = None
        self.supportedParser = [2]
        self._errorInteger = 'Element "{0}" must be an integer.'
        self._errorMissing = 'Missing element "{0}".'
        
    def parse( self, fileName ):
        ''' Parses a level file. Throws YAMLError or level.levelparsererror. Returns the resulting level object. '''
        
        with open( fileName, 'r' ) as file:
            root = yaml.safe_load( file )
        
        # Validate root element.
        if self.TAG_LEVEL not in root:
            raise levelparser.LevelParserError( 'Root element must be of type "level".' )
        
        levelRoot = root[self.TAG_LEVEL]
        
        # Validate parser version.
        if levelRoot[self.TAG_PARSER] not in self.supportedParser:
            raise levelparser.LevelParserError( 'Unsupported level parser version "{0}".'.format(levelRoot[self.TAG_PARSER]) )
        
        self.__parseLevel( levelRoot )
        return self.level
    
    def __parseCircle( self, circleRoot ):
        ''' Parses circle and returns it. '''
        c = circle.Circle()
        c.position = self.__parseVector2d( circleRoot )
        c.radius = self.__readReqInteger( circleRoot, self.TAG_RADIUS )
        return c
    
    def __parseLevel( self, levelRoot ):
        ''' Parses the level. '''
        
        self.level = level.Level()
        
        # Author.
        self.level.author = self.__readString( levelRoot, self.TAG_AUTHOR, self.level.author )
        
        # Date.
        self.level.date = self.__readString( levelRoot, self.TAG_DATE, self.level.date )
        
        # Description.
        self.level.description = self.__readString( levelRoot, self.TAG_DESCRIPTION, self.level.description )
        
        # Name.
        self.level.name = self.__readReqString( levelRoot, self.TAG_NAME )
        
        # Time limit.
        self.level.timeLimit = self.__readReqInteger( levelRoot, self.TAG_TIMELIMIT )
        
        # Version.
        self.level.version = self.__readString( levelRoot, self.TAG_VERSION, self.level.version )
        
        # Map.
        self.__parseMap( self.__readReqObject(levelRoot, self.TAG_MAP) )
    
    def __parseMap( self, mapRoot ):
        ''' Parses the map. '''
        
        self.level.map = map.Map()
        
        # Border.
        self.level.map.border = self.__readReqInteger( mapRoot, self.TAG_BORDER )
        
        # Height.
        self.level.map.height = self.__readReqInteger( mapRoot, self.TAG_HEIGHT )
        
        # Width.
        self.level.map.width = self.__readReqInteger( mapRoot, self.TAG_WIDTH )
        
        # Objects.
        objects = []
        if self.TAG_OBJECTS in mapRoot:
            objects.extend( mapRoot[self.TAG_OBJECTS] )
        else:
            raise levelparser.LevelParserError( self._errorMissing.format(self.TAG_OBJECTS) )
        if objects:
            for o in objects:
                if self.TAG_CIRCLE in o:
                    self.level.map.objects.append( self.__parseCircle(o[self.TAG_CIRCLE]) )
                elif self.TAG_RECT in o:
                    self.level.map.objects.append( self.__parseRect(o[self.TAG_RECT]) )
        
        # Players.
        player = self.__readReqObject( mapRoot, self.TAG_PLAYER )
        playerObject = self.__readReqObject( player, self.TAG_CIRCLE )
        self.level.map.player = self.__parseCircle( playerObject )
        
        # Targets.
        targets = []
        if self.TAG_TARGETS in mapRoot:
            targets.extend( mapRoot[self.TAG_TARGETS] )
        else:
            raise levelparser.LevelParserError( self._errorMissing.format(self.TAG_TARGETS) )
        if targets:
            for t in targets:
                self.level.map.targets.append( self.__parseTarget(t[self.TAG_TARGET]) )
        else:
            raise levelparser.LevelParserError( self._errorMissing.format(self.TAG_TARGET) )
    
    def __parseTarget( self, targetRoot ):
        ''' Parses a target and returns it. '''
        t = target.Target()
        t.points = self.__readReqInteger( targetRoot, self.TAG_POINTS )
        if self.TAG_CIRCLE in targetRoot:
            t.object = self.__parseCircle( targetRoot[self.TAG_CIRCLE] )
        if self.TAG_RECT in targetRoot:
            t.object = self.__parseRect( targetRoot[self.TAG_RECT] )
        return t
        
    def __parseRect( self, rectRoot ):
        ''' Parses a rectangle and returns it. '''
        r = rect.Rect()
        r.angle = self.__readReqInteger( rectRoot, self.TAG_ANGLE )
        r.height = self.__readReqInteger( rectRoot, self.TAG_HEIGHT )
        r.width = self.__readReqInteger( rectRoot, self.TAG_WIDTH )
        r.position = self.__parseVector2d( rectRoot )
        return r
    
    def __parseVector2d( self, vectorRoot ):
        ''' Parses a vector and returns it. '''
        x = self.__readReqInteger( vectorRoot, self.TAG_X )
        y = self.__readReqInteger( vectorRoot, self.TAG_Y )
        return vector2d.Vector2d( x, y )
    
    def __readReqInteger( self, root, tag ):
        ''' Tries to read a required integer tag. Returns integer or raises error. '''
        if tag in root and isinstance( root[tag], int ):
            return root[tag]
        elif tag in root and not isinstance( root[tag], int ):
            raise levelparser.LevelParserError( self._errorInteger.format(tag) )
        else:
            raise levelparser.LevelParserError( self._errorMissing.format(tag) )
    
    def __readReqObject( self, root, tag ):
        ''' Tries to read a required object tag. Returns object or raises error. '''
        if tag in root:
            return root[tag]
        else:
            raise levelparser.LevelParserError( self._errorMissing.format(tag) )
    
    def __readReqString( self, root, tag ):
        ''' Tries to read a required string tag. Returns text or raises error. '''
        return self.__readReqObject( root, tag )
        
    def __readString( self, root, tag, default ):
        ''' Tries to read a not required string tag. Returns the text or the default value if not 
        found. '''
        if tag in root:
            return root[tag]
        else:
            return default
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()