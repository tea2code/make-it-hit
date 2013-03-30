from common import tickable
from data import collisionevent
from data import targetevent
from gamerules import gamestarter

import os

class GameRules( tickable.Tickable ):
    ''' Controls the rules in a game.'''
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Checks the game rules.'''
        
        if data.state is data.STATES.PLAYING:
            self.__playing( data )  
        
        elif data.state is data.STATES.STARTING:
            self.__starting( data )
        
        elif data.state is data.STATES.LOADING:
            self.__loading( data )
            
        elif data.state is data.STATES.MENU_READ_LEVELS:
            self.__readLevels( data )
            
    def __loading( self, data ):
        ''' Handles loading state of game. '''  
        # Initialize game.
        gameStarter = gamestarter.GameStarter()
        gameStarter.load( data, data.levelList[0] )
        
    def __playing( self, data ):
        ''' Handles playing state of game. ''' 
        
        timeMs = data.time * 1000
        
        # Event handling:
        for event in data.events:
            # Collision events.
            if isinstance( event, collisionevent.CollisionEvent ):
                data.points += 2
            
            # Target events.
            elif isinstance( event, targetevent.TargetEvent ):
                data.points += event.target.points
                data.points += round( (data.level.timeLimit - timeMs) * 0.005 )
                data.state = data.STATES.VICTORY   
                  
                data.levelList.pop( 0 )
                if data.levelList:
                    data.state = data.STATES.LOADING  
                
        # Check rest time.
        if timeMs >= data.level.timeLimit:
            data.state = data.STATES.GAMEOVER    
    
    def __readLevels( self, data ):
        ''' Reads the level list. '''
        
        del data.levelList[:]
        
        if not data.levelDir.endswith('/'):
            data.levelDir += '/'
            
        for file in os.listdir(data.levelDir):
            file = data.levelDir + file
            if file.endswith( data.levelExtension ):
                data.levelList.append( file )

        data.state = data.STATES.MENU_NEW
            
    def __starting( self, data ):
        ''' Handles starting state of game. '''
        
        if data.time * 1000 >= data.startTime:
            data.time = 0
            data.state = data.STATES.PLAYING