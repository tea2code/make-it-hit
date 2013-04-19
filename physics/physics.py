﻿from common import tickable
from data import collisionevent
from data import rect
from data import targetevent
from data import vector2d
from physics import colliderfactory
from physics import gravitation
from physics import moveheun
from physics import movestate
from physics import reflectorfactory

class Physics( tickable.Tickable ):
    ''' This class calculates the physical reactions of all objects. 
    
    Constants:
    GRAVITATIONAL_CONSTANT -- The gravitational constant (float). TODO: Move into configuration.
    
    Member:
    _colliderFactory -- Factory for colliders (physics.colliderfactory).
    _reflectorFactory -- Factory for reflectors (physics.reflectorfactory).
    '''
    
    GRAVITATIONAL_CONSTANT = 6.67384 * 10**2 # Not the correct value but for scaling purpose we use it.

    def __init__( self ):
        self._colliderFactory = colliderfactory.ColliderFactory()
        self._reflectorFactory = reflectorfactory.ReflectorFactory()
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Calculates the physic on all objects. '''
    
        if data.state not in [data.STATES.PLAYING, data.STATES.VICTORY, data.STATES.GAMEOVER]:
            return;
    
        player = data.level.map.player
    
        # Add gravitation forces to player.
        grav = gravitation.Gravitation( self.GRAVITATIONAL_CONSTANT )
        for o in data.level.map.objects:
            direction = o.position - player.position;
            force = grav.calcForce( player.mass, o.mass, direction.length() )
            forceVector = direction * force
            player.addForce( forceVector )
    
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
        events = self.__interact( player, self.__borders(data) )
        data.events.extend( events )
        
        # Interaction of player with objects.
        events = self.__interact( player, data.level.map.objects )
        data.events.extend( events )
        
        # Check if player hits target.
        for target in data.level.map.targets:
            collider = self._colliderFactory.createFrom( player, target.object )
            collision = collider.collide()
            if collision.isCollided:
                event = targetevent.TargetEvent( target, collision.x, collision.y )
                data.events.append( event )

    def __borders( self, data ):
        ''' Calculates a list of rectangles representing the borders. '''
        border = data.level.map.border
        height = data.level.map.height
        width = data.level.map.width
        
        borders = []
        
        # Left.
        left = rect.Rect()
        left.position = vector2d.Vector2d( border / 2, height / 2 )
        left.height = height
        left.width = border
        borders.append( left )
        
        # Top.
        top = rect.Rect()
        top.position = vector2d.Vector2d( width / 2, border / 2 )
        top.height = border
        top.width = width
        borders.append( top )
        
        # Right.
        right = rect.Rect()
        right.position = vector2d.Vector2d( width - border / 2, height / 2 )
        right.height = height
        right.width = border
        borders.append( right )
        
        # Bottom.
        bottom = rect.Rect()
        bottom.position = vector2d.Vector2d( width / 2, height - border / 2 )
        bottom.height = border
        bottom.width = width
        borders.append( bottom )   
        
        return borders
        
    def __interact( self, player, objects ):
        ''' Calculates interaction of player with objects. Returns list of events.'''
        events = []
        for mapObject in objects:
            collider = self._colliderFactory.createFrom( player, mapObject )
            collision = collider.collide()
            if collision.isCollided:
                reflector = self._reflectorFactory.createFrom( player, mapObject )
                player.momentum = reflector.reflect( collision.x, collision.y )
                event = collisionevent.CollisionEvent( mapObject, collision.x, collision.y )
                events.append( event )
        return events