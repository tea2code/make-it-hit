from common import tickable
from data import collisionevent
from data import targetevent

class GameRules( tickable.Tickable ):
    ''' Controls the rules in a game.'''
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Checks the game rules.'''
        
        if data.state is not data.STATES.PLAYING:
            return
        
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
                
                print( 'Points: {0}'.format(data.points) )        
                
        # Check rest time.
        if timeMs >= data.level.timeLimit:
            data.state = data.STATES.GAMEOVER
      
            template = 'Game Over. You are out of time after {0:.2f} seconds. Time limit was ' \
                       '{1:.2f} seconds.'
            print( template.format(data.time, data.level.timeLimit / 1000) )        