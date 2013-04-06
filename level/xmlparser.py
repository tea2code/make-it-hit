from data import vector2d
from data import circle
from data import level
from data import map
from data import rect
from data import target
from formulary import comparison
from level import levelparser

import xml.etree.ElementTree as et

class XmlParser(levelparser.LevelParser):
    ''' This parser creates a representation of a xml map. 
    
    Constants:
    ATTR_PARSER -- Parser version of this level.
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

    ATTR_PARSER = 'parser'
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
        self.supportedParser = ['1']
        self._errorInteger = 'Element "{0}" must be an integer.'
        self._errorMissing = 'Missing element "{0}".'
    
    def parse( self, fileName ):
        ''' Parses a level file. Throws xml.etree.ElementTree.ParseError or level.levelparsererror.
        Returns the resulting level object. '''
        
        # Read file and try to parse.
        tree = et.parse( fileName )
        root = tree.getroot()
        
        # Validate root element.
        if root.tag != self.TAG_LEVEL:
            raise error.LevelParserError( 'Root element must be of type "level". Got "{0}".'.format(root.tag) )
        
        # Validate parser version.
        if root.get(self.ATTR_PARSER) not in self.supportedParser:
            raise error.LevelParserError( 'Unsupported level parser version "{0}".'.format(root.get(self.ATTR_PARSER)) )
            
        self.__parseLevel( root )
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
        objectsElement = mapRoot.find( self.TAG_OBJECTS )
        objects = []
        if objectsElement is not None:
            objects.extend( objectsElement.findall(self.TAG_CIRCLE) )
            objects.extend( objectsElement.findall(self.TAG_RECT) )
        else:
            raise error.LevelParserError( self._errorMissing.format(self.TAG_OBJECTS) )
        if objects:
            for o in objects:
                if o.tag == self.TAG_CIRCLE:
                    self.level.map.objects.append( self.__parseCircle(o) )
                elif o.tag == self.TAG_RECT:
                    self.level.map.objects.append( self.__parseRect(o) )
        
        # Players.
        player = self.__readReqObject( mapRoot, self.TAG_PLAYER )
        playerObject = self.__readReqObject( player, self.TAG_CIRCLE )
        self.level.map.player = self.__parseCircle( playerObject )
        
        # Targets.
        targetsElement = mapRoot.find( self.TAG_TARGETS )
        targets = []
        if targetsElement is not None:
            targets.extend( targetsElement.findall(self.TAG_TARGET) )
        else:
            raise error.LevelParserError( self._errorMissing.format(self.TAG_TARGETS) )
        if targets:
            for t in targets:
                self.level.map.targets.append( self.__parseTarget(t) )
        else:
            raise error.LevelParserError( self._errorMissing.format(self.TAG_TARGET) )

    def __parseTarget( self, targetRoot ):
        ''' Parses a target and returns it. '''
        t = target.Target()
        t.points = self.__readReqInteger( targetRoot, self.TAG_POINTS )
        object = targetRoot.find( self.TAG_CIRCLE )
        if object is not None:
            t.object = self.__parseCircle( object )
        object = targetRoot.find( self.TAG_RECT )
        if object is not None:
            t.object = self.__parseRect( object )
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
        element = root.find( tag )
        if element is not None and comparison.stringIsInt( element.text ):
            return int( element.text )
        elif element is not None and not comparison.stringIsInt( element.text ):
            raise error.LevelParserError( self._errorInteger.format(tag) )
        else:
            raise error.LevelParserError( self._errorMissing.format(tag) )
    
    def __readReqObject( self, root, tag ):
        ''' Tries to read a required object tag. Returns object or raises error. '''
        element = root.find( tag )
        if element is not None:
            return element
        else:
            raise error.LevelParserError( self._errorMissing.format(tag) )
    
    def __readReqString( self, root, tag ):
        ''' Tries to read a required string tag. Returns text or raises error. '''
        element = root.find( tag )
        if element is not None:
            return element.text
        else:
            raise error.LevelParserError( self._errorMissing.format(tag) )
    
    def __readString( self, root, tag, default ):
        ''' Tries to read a not required string tag. Returns the text or the default value if not 
        found. '''
        element = root.find( tag )
        if element is not None:
            return element.text
        else:
            return default
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()