class LevelParserError( Exception ):
    ''' Exception thrown if a required level element is empty, missing or has an not allowed 
    value. '''