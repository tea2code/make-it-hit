from . import collider

class CircleRectCollider( collider.Collider ):
    ''' Calculates collision between circle and rect. 
    
    Member:
    _circle -- The circle (data.circle).
    _rect -- The rect (data.rect).
    '''
    
    _circle = None
    _rect = None
    
    def __init__( self, circle, rect ):
        self._circle = circle
        self._rect = rect
    
    def collide( self ):
        