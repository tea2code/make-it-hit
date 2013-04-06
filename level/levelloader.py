from level import levelparserfactory

class LevelLoader():
    ''' Loads levels from files. '''
    
    def load( self, mapFileName ):
        ''' Loads the given level file. Throws xml.etree.ElementTree.ParseError or level.levelparsererror
        in case of an error. Returns the level object. '''
        
        extension = mapFileName[ mapFileName.rindex('.'): ]
        factory = levelparserfactory.LevelParserFactory()
        parser = factory.createFor( extension )
        return parser.parse( mapFileName )