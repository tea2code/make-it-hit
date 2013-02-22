from level import levelparser

class LevelLoader():
    ''' Loads levels from files. '''
    
    def load( self, mapFile ):
        ''' Loads the given level file. Throws xml.etree.ElementTree.ParseError or level.levelparsererror
        in case of an error. Returns the level object. '''
        parser = levelparser.LevelParser()
        return parser.parse( mapFile )
        