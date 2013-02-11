from . import movestate

class MoveHeun:
    ''' Integration for moveable objects with position x and velocity v. '''
    
    @staticmethod
    def integrate( state, h ):
        ''' Integrate using the heun method.

        Arguments:
        state -- The current state (MoveState).
        h -- The change in step number (float).
        
        Returns the new state.
        '''
    
        # yy_i+1 = y_i + h * f(t_i, y_i)
        eulerState = movestate.MoveState()
        eulerState.mass = state.mass
        eulerState.momentum = state.momentum + state.force * h
        
        # y_i+1 = y_i + (h/2) * (f(t_i, y_i) + f(t_i+1, yy_i+1))
        newState = movestate.MoveState()
        newState.momentum = eulerState.momentum
        newState.position = state.position + (state.velocity() + eulerState.velocity()) * (h / 2)
        return newState