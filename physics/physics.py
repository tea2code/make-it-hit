from . import moveheun
from . import movestate
from common import tickable

class Physics( tickable.Tickable ):
    ''' This class calculates the physical reactions of all objects. '''

    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Calculates the physic on all objects. '''
    