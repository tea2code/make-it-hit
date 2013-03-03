from level import levelloader

class GameStarter:
    ''' Loads und initializes a game. '''

    def load( self, data, levelFile ):
        ''' Loads the level and initializes it. After this method call the game is ready 
        to start.'''
        levelLoader = levelloader.LevelLoader()
        data.level = levelLoader.load( levelFile )
        data.level.map.player.mass = 1
        data.screenXCoefficient = data.windowWidth / data.level.map.width
        data.screenYCoefficient = data.windowHeight / data.level.map.height
        data.state = data.STATES.PLAYING