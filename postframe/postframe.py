from common import tickable

class PostFrame( tickable.Tickable ):
    ''' This class executes tasks at the end of a frame. Mostly cleanup of calculated frame data. '''

    def tick( self, data ):
        ''' Implementation of Tickable.tick().'''
    
        # Clear events.
        del data.events[:]