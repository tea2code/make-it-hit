from abc import ABCMeta
from common import vector2d

class Movable(metaclass = ABCMeta):
    ''' This abstract class represents a movable object. 
    
    Members:
    mass -- The mass of the object (float).
    momentum -- The momentum of the object (common.vector2d).
    position -- The position of the object (common.vector2d).
    
    _forces -- List of force vectors (common.vector2d).
    '''
    
    mass = 0
    momentum = None
    position = None
    
    _forces = []
    
    def __init__( self ):
        ''' Test:
        >>> m = Movable()
        >>> m._forces
        []
        >>> m.mass
        0
        >>> m.position.x == 0 and m.position.y == 0
        True
        >>> m.momentum.x == 0 and m.momentum.y == 0
        True
        '''
        self.momentum = vector2d.Vector2d.nullVector()
        self.position = vector2d.Vector2d.nullVector()
    
    def addForce( self, force ):
        ''' Adds force to object (Vector2d). Returns this.

        Test:
        >>> m = Movable()
        >>> m.addForce( vector2d.Vector2d(1, 2) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m._forces[0].x == 1 and m._forces[0].y == 2
        True
        '''
        self._forces.append( force )
        return self
        
    def clearForces( self ):
        ''' Removes all forces. Returns this. 

        Test:
        >>> m = Movable()
        >>> m.clearForces() # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.addForce( vector2d.Vector2d(1, 2) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> len(m._forces)
        1
        >>> len(m.clearForces()._forces)
        0
        '''
        del self._forces[:]
        return self
        
    def sumForces( self ):
        ''' Calculates the sum of all forces and returns it. 
        
        Test:
        >>> m = Movable()
        >>> m.addForce( vector2d.Vector2d(1, 0) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.addForce( vector2d.Vector2d(0, 2) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.addForce( vector2d.Vector2d(3, 3) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> v = m.sumForces()
        >>> v.x == 4 and v.y == 5
        True
        '''
        sum = vector2d.Vector2d.nullVector()
        for force in self._forces:
            sum += force
        return sum
        
    def setMass( self, mass ):
        ''' Sets mass (float). Returns this. 
        
        Test:
        >>> m = Movable()
        >>> m.setMass( 1 ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.mass
        1
        '''
        self.mass = mass
        return self
        
    def setMomentum( self, momentum ):
        ''' Sets the momentum (Vector2d). Returns this. 
        
        Test:
        >>> m = Movable()
        >>> m.setMomentum( vector2d.Vector2d(2, 3) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.momentum.x == 2 and m.momentum.y == 3
        True
        '''
        self.momentum = momentum
        return self
        
    def setPosition( self, position ):
        ''' Sets the position (Vector2d). Returns this. 
        
        Test:
        >>> m = Movable()
        >>> m.setPosition( vector2d.Vector2d(2, 3) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.position.x == 2 and m.position.y == 3
        True
        '''
        self.position = position
        return self
        
    def setPositionX( self, x ):
        ''' Sets the x component of the position. Returns this. 
        
        Test:
        >>> m = Movable()
        >>> m.setPositionX( 2 ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.position.x == 2 and m.position.y == 0
        True
        '''
        self.position.x = x
        return self
    
    def setPositionY( self, y ):
        ''' Sets the y component of the position. Returns this. 
        
        Test:
        >>> m = Movable()
        >>> m.setPositionY( 2 ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.position.x == 0 and m.position.y == 2
        True
        '''
        self.position.y = y
        return self
        
    def stop( self ):
        ''' Stops the object.

        Test:
        >>> m = Movable()
        >>> m.addForce( vector2d.Vector2d(1, 2) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.setMomentum( vector2d.Vector2d(3, 2) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> len(m._forces)
        1
        >>> m.momentum.x == 3 and m.momentum.y == 2
        True
        >>> m.stop()
        >>> len(m._forces)
        0
        >>> m.momentum.x == 0 and m.momentum.y == 0
        True
        '''
        self.clearForces()
        self.setMomentum( vector2d.Vector2d.nullVector() )
        
    def __str__( self ):
        ''' Test:
        >>> m = Movable()
        >>> print(m)
        Movable(forces [], mass 0.00, momentum Vector2d(0.00, 0.00), position Vector2d(0.00, 0.00))
        '''
        forces = ", ".join( [str(element) for element in self._forces]  )
        template = 'Movable(forces [{0}], mass {1:.2f}, momentum {2}, position {3})'
        return template.format(forces, self.mass, self.momentum, self.position)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()