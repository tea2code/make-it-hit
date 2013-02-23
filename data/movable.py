from abc import ABCMeta
from data import vector2d

class Movable(metaclass = ABCMeta):
    ''' This abstract class represents a movable object. 
    
    Members:
    mass -- The mass of the object (float).
    momentum -- The momentum of the object (common.vector2d).
    position -- The position of the object (common.vector2d).
    _forces -- List of force vectors (common.vector2d).
    '''
    
    def __init__( self ):
        ''' Test:
        >>> m = Movable()
        >>> m.mass
        0
        >>> m.position.x == 0 and m.position.y == 0
        True
        >>> m.momentum.x == 0 and m.momentum.y == 0
        True
        >>> m._forces
        []
        '''
        self.mass = 0
        self.position = vector2d.Vector2d.nullVector()
        self.momentum = vector2d.Vector2d.nullVector()
        self._forces = []
    
    def addForce( self, force ):
        ''' Adds force to object (Vector2d). Returns this.

        Test:
        >>> m = Movable()
        >>> m.addForce( vector2d.Vector2d(1, 2) )
        >>> m._forces[0].x == 1 and m._forces[0].y == 2
        True
        '''
        self._forces.append( force )
        
    def clearForces( self ):
        ''' Removes all forces.

        Test:
        >>> m = Movable()
        >>> m.clearForces() # doctest: +ELLIPSIS
        >>> m.addForce( vector2d.Vector2d(1, 2) ) # doctest: +ELLIPSIS
        >>> len(m._forces)
        1
        >>> m.clearForces()
        >>> len(m._forces)
        0
        '''
        del self._forces[:]
        
    def sumForces( self ):
        ''' Calculates the sum of all forces and returns it. 
        
        Test:
        >>> m = Movable()
        >>> m.addForce( vector2d.Vector2d(1, 0) )
        >>> m.addForce( vector2d.Vector2d(0, 2) )
        >>> m.addForce( vector2d.Vector2d(3, 3) )
        >>> v = m.sumForces()
        >>> v.x == 4 and v.y == 5
        True
        '''
        sum = vector2d.Vector2d.nullVector()
        for force in self._forces:
            sum += force
        return sum
        
    def stop( self ):
        ''' Stops the object.

        Test:
        >>> m = Movable()
        >>> m.addForce( vector2d.Vector2d(1, 2) ) # doctest: +ELLIPSIS
        >>> m.momentum = vector2d.Vector2d(3, 2) # doctest: +ELLIPSIS
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
        self.momentum = vector2d.Vector2d.nullVector()
        
    def __str__( self ):
        ''' Test:
        >>> m = Movable()
        >>> print(m)
        Movable(forces [], mass 0.00, momentum Vector2d(0.00, 0.00), position Vector2d(0.00, 0.00))
        '''
        forces = ', '.join( [str(element) for element in self._forces] )
        template = 'Movable(forces [{0}], mass {1:.2f}, momentum {2}, position {3})'
        return template.format(forces, self.mass, self.momentum, self.position)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()