from level import xmlparser
from level import yamlparser

class NotParsableError( Exception ):
    ''' Exception thrown if a unknown file extension was given. '''

class LevelParserFactory:
    ''' Factory for level parsers. 
    
    Constants:
    EXT_XML -- Extension name for XML files.
    EXT_YAML -- Extension name for YAML files.
    '''
    
    EXT_XML = '.xml'
    EXT_YAML  = '.yaml'
    
    def createFor( self, fileExtension ):
        ''' Returns a level parser for the given file extension or throws not parsable error. '''
        
        if fileExtension == self.EXT_YAML:
            return yamlparser.YamlParser()
        
        elif fileExtension == self.EXT_XML:
            return xmlparser.XmlParser()
        
        else:
            raise NotParsableError( 'Unknown file extension "{}".'.format(fileExtension) )
            