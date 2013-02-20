from common import tickable
from data import collisionevent
from data import targetevent

class GameRules( tickable.Tickable ):
    ''' Controls the rules in a game. '''
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Checks the game rules.'''
        
        # Event handling:
        for event in data.events:
            # Collision events.
            if isinstance( event, collisionevent.CollisionEvent ):
                print( 'Collision at ({0}, {1}) with "{2}"'.format(event.x, event.y, event.object) )
            
            # Target events.
            elif isinstance( event, targetevent.TargetEvent ):
                print( 'Target hit at ({0}, {1}) with "{2}"'.format(event.x, event.y, event.target) )