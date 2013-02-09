﻿from common import vector2d
from data import circle
from data import level
from data import map
from data import rect
from data import target
from level import levelparsererror as error

import xml.etree.ElementTree as Et

class LevelParser():
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
    TAG_PLAYERS -- Players element.
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
    
    level -- The resulting level object.
    supportedParser -- List of supported parser versions
    
    _errorMissing -- Text template for missing element errors.
    '''

    ATTR_PARSER = 1
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
    TAG_PLAYERS = 'players'
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
    
    level = None
    supportedParser = [1]
    
    _errorInteger = 'Element "{0}" must be an integer.'
    _errorMissing = 'Missing element "{0}".'

    def __init__( self ):
        ''' Test:
        >>> l = LevelParser()
        >>> l.level
        '''
    
    def parse( self, file ):
        ''' Parses a level file. Throws xml.etree.ElementTree.ParseError or level.levelparsererror.
        Returns the resulting level object. '''
        
        # Read file and try to parse.
        tree = Et.parse( file )
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
        circle = circle.Circle()
        circle.position = self.__parseVector2d( circleRoot )
        circle.radius = self.__readReqInteger( circleRoot, self.TAG_RADIUS )
        return circle
    
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
        self.level.timelimit = self.__readReqInteger( levelRoot, self.TAG_TIMELIMIT )
        
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
            objects.extend( objectsElement.findall(self.TAG_RECT) )
        else:
            raise error.LevelParserError( self._errorMissing.format(self.TAG_OBJECTS) )
        if objects:
            for object in objects:
                self.level.map.objects.append( self.__parseRect(object) )
        else:
            raise error.LevelParserError( self._errorMissing.format(self.TAG_OBJECTS) )
        
        # Players.
        playersElement = mapRoot.find( self.TAG_PLAYERS )
        players = []
        if playersElement is not None:
            players.extend( playersElement.findall(self.TAG_CIRCLE) )
        else:
            raise error.LevelParserError( self._errorMissing.format(self.TAG_PLAYERS) )
        if players:
            for player in players:
                self.level.map.players.append( self.__parseCircle(player) )
        else:
            raise error.LevelParserError( self._errorMissing.format(self.TAG_PLAYERS) )
        
        # Targets.
        targetsElement = mapRoot.find( self.TAG_TARGETS )
        targets = []
        if targetsElement is not None:
            targets.extend( targetsElement.findall(self.TAG_TARGET) )
        else:
            raise error.LevelParserError( self._errorMissing.format(self.TAG_TARGETS) )
        if targets:
            for target in targets:
                self.level.map.targets.append( self.__parseTarget(target) )
        else:
            raise error.LevelParserError( self._errorMissing.format(self.TAG_TARGET) )

    def __parseTarget( self, targetRoot ):
        ''' Parses a target and returns it. '''
        target = target.Target()
        target.points = self.__readReqInteger( targetRoot, self.TAG_POINTS )
        object = targetRoot.find( self.TAG_CIRCLE )
        if object is not None:
            target.object = self.__parseCircle( object )
        object = targetRoot.find( self.TAG_RECT )
        if object is not None:
            target.object = self.__parseRect( object )
        return target
        
    def __parseRect( self, rectRoot ):
        ''' Parses a rectangle and returns it. '''
        rect = rect.Rect()
        rect.angle = self.__readReqInteger( rectRoot, self.TAG_ANGLE )
        rect.height = self.__readReqInteger( rectRoot, self.TAG_HEIGHT )
        rect.width = self.__readReqInteger( rectRoot, self.TAG_WIDTH )
        rect.position = self.__parseVector2d( rectRoot )
        return rect
    
    def __parseVector2d( self, vectorRoot ):
        ''' Parses a vector and returns it. '''
        x = self.__readReqInteger( vectorRoot, self.TAG_X )
        y = self.__readReqInteger( vectorRoot, self.TAG_Y )
        return vector2d.Vector2d( x, y )
    
    def __readReqInteger( self, root, tag ):
        ''' Tries to read a required integer tag. Returns integer or raises error. '''
        element = root.find( tag )
        if element is not None and element.text.isdigit():
            return int( element.text )
        elif element is not None and not element.text.isdigit():
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