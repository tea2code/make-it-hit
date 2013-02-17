from . import colliderfactory
from . import moveheun
from . import movestate
from . import reflectorfactory
from common import tickable
from data import rect
from data import vector2d

class Physics( tickable.Tickable ):
    ''' This class calculates the physical reactions of all objects. 
    
    Member:
    _colliderFactory -- Factory for colliders (physics.colliderfactory).
    _reflectorFactory -- Factory for reflectors (physics.reflectorfactory).
    '''

    def __init__( self ):
        self._colliderFactory = colliderfactory.ColliderFactory()
        self._reflectorFactory = reflectorfactory.ReflectorFactory()
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Calculates the physic on all objects. '''
    
        # Check if level already exists.
        if data.level is None:
            return
    
        player = data.level.map.player
    
        # Move player.
        state = movestate.MoveState()
        state.force = player.sumForces()
        player.clearForces()
        state.mass = player.mass
        state.momentum = player.momentum
        state.position = player.position
        
        newState = moveheun.MoveHeun.integrate( state, data.deltaTime )
        player.momentum = newState.momentum
        player.position = newState.position
        
        # Interaction of player with borders.
        self.__interact( player, self._borders(data) )
        
        # Interaction of player with objects.
        self.__interact( player, data.level.map.objects )

    def __borders( self, data ):
        ''' Calculates a list of rectangles representing the borders. '''
        if not data._borders:
            border = data.level.map.border
            height = data.level.height
            width = data.level.width
            
            # Left.
            left = rect.Rect()
            left.position = vector2d.Vector2d( border / 2, height / 2 )
            left.height = height
            left.width = border
            data._borders.append( left )
            
            # Top.
            top = rect.Rect()
            top.position = vector2d.Vector2d( width / 2, border / 2 )
            top.height = border
            top.width = width
            data._borders.append( top )
            
            # Right.
            right = rect.Rect()
            right.position = vector2d.Vector2d( width - border / 2, height / 2 )
            right.height = height
            right.width = border
            data._borders.append( right )
            
            # Bottom.
            bottom = rect.Rect()
            bottom.position = vector2d.Vector2d( width / 2, height - border / 2 )
            bottom.height = border
            bottom.width = width
            data._borders.append( bottom )            
        
        return data._borders
        
    def __interact( self, player, objects ):
        ''' Calculates interaction of player with objects. '''
        for object in objects:
            collider = self._colliderFactory.createFrom( player, object )
            collision = collider.collide()
            if collision.isCollided:
                reflector = self._reflectorFactory.createFrom( player, object )
                player.momentum = reflector.reflect( collision.x, collision.y )