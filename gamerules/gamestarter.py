from level import levelloader

class GameStarter:
    ''' Loads und initializes a game. '''

    def load( self, data, levelFile ):
        ''' Loads the level and initializes it. After this method call the game is ready 
        to start.'''
        levelLoader = levelloader.LevelLoader()
        
        data.events = []
        data.level = levelLoader.load( levelFile )
        data.level.map.player.mass = 1
        data.points = 0
        data.screenXCoefficient = data.windowWidth / data.level.map.width
        data.screenYCoefficient = data.windowHeight / data.level.map.height
        data.state = data.STATES.STARTING
        data.time = 0