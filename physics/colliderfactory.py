from . import circlecirclecollider
from . import circlerectcollider
from . import nocollidererror
from data import circle
from data import rect

class ColliderFactory:
    ''' Factory of collider objects. '''
    
    def createFrom( self, object1, object2 ):
        ''' Takes two objects and searches the fitting collider. Raises NoColliderError if no 
        collider exists. Returns the collider. 
        
        Test:
        >>> c = ColliderFactory()
        >>> c.createFrom( circle.Circle(), rect.Rect() ) # doctest: +ELLIPSIS
        <...CircleRectCollider object at 0x...>
        >>> c.createFrom( rect.Rect(), circle.Circle() ) # doctest: +ELLIPSIS
        <...CircleRectCollider object at 0x...>
        >>> c.createFrom( circle.Circle(), circle.Circle() ) # doctest: +ELLIPSIS
        <...CircleCircleCollider object at 0x...>
        '''
        
        # Circle - Rect.
        if isinstance( object1, circle.Circle ) and isinstance( object2, rect.Rect ):
            return circlerectcollider.CircleRectCollider( object1, object2 )
        elif isinstance( object1, rect.Rect ) and isinstance( object2, circle.Circle ):
            return circlerectcollider.CircleRectCollider( object2, object1 )
         
        # Circle - Circle
        elif isinstance( object1, circle.Circle ) and isinstance( object2, circle.Circle ):
            return circlecirclecollider.CircleCircleCollider( object1, object2 )
         
        # Unknown objects. Can not be collided.
        else:
            raise nocollidererror.NoColliderError( 'No collider object for "{0}" and "{1}" found.'.format(object1, object2) )
            
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()