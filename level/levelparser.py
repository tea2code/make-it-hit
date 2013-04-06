from abc import ABCMeta, abstractmethod  

class LevelParserError( Exception ):
    ''' Exception thrown if a required level element is empty, missing or has an not allowed 
    value. '''

class LevelParser(metaclass = ABCMeta):
    ''' Abstract class for level parser. '''
    
    @abstractmethod
    def parse( self, fileName ):
        ''' The derived class must implement this method. Parses the file represented by 
        the file name. Throws LevelParserError in case of error. '''
        