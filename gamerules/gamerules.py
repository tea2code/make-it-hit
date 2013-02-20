from common import tickable
from data import collisionevent
from data import targetevent
from data import victoryevent

class GameRules( tickable.Tickable ):
    ''' Controls the rules in a game. 
    
    Member:
    _active -- Stops handling events if false.
    '''
    
    _active = True
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Checks the game rules.'''
        
        if not self._active:
            return
        
        # Event handling:
        for event in data.events:
            # Collision events.
            if isinstance( event, collisionevent.CollisionEvent ):
                data.points -= 5
            
            # Target events.
            elif isinstance( event, targetevent.TargetEvent ):
                data.points += event.target.points
                print( 'Points: {0}'.format(data.points) )
                
                data.events.append( victoryevent.VictoryEvent() )
                self._active = False
        