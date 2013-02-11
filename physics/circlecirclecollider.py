from . import collider

class CircleCircleCollider( collider.Collider ):
    ''' Calculates collision between two circles. 
    
    Member:
    _circle1 -- The first circle (data.circle).
    _circle2 -- The second circle (data.circle).
    '''
    
    _circle1 = None
    _circle2 = None
    
    def __init__( self, circle1, circle2 ):
        self._circle1 = circle1
        self._circle2 = circle2
    
    def collide( self ):
        