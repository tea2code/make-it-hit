from common import tickable

class GameRules( tickable.Tickable ):
    ''' Controls the rules in a game. '''
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Checks the game rules.'''
        