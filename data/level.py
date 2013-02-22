class Level:
    ''' Class representing a level.
    
    Member:
    author -- The author (string).
    date -- Date of last update (string).
    description -- A brief description (string).
    map -- The map (data.map).
    name -- The name (string).
    timeLimit -- The time limit to solve the level in milliseconds (int).
    version -- The version (string).
    '''
    
    author = ''
    date = ''
    description = ''
    map = None
    name = ''
    timeLimit = 0 
    version = ''
    
    def __init__( self ):
        ''' Test:
        >>> l = Level()
        >>> l.author
        ''
        >>> l.date
        ''
        >>> l.description
        ''
        >>> l.map
        >>> l.name
        ''
        >>> l.timeLimit
        0
        >>> l.version
        ''
        '''
        
    def __str__( self ):
        ''' Test:
        >>> l = Level()
        >>> print( l )
        Level(author , date , description , map None, name , timeLimit 0, version )
        '''
        template = 'Level(author {0}, date {1}, description {2}, map {3}, name {4}, timeLimit {5}, version {6})'
        return template.format( self.author, self.date, self.description, self.map, self.name, self.timeLimit, self.version )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod( )