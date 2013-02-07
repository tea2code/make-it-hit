import common.application
import common.timestepper
import common.vector2d
import data.circle
import data.data
import data.movable
import data.rect
import data.target
import graphics.tkcircledrawer

if __name__ == '__main__':
    import doctest
    doctest.testmod( common.application )
    doctest.testmod( common.timestepper )
    doctest.testmod( common.vector2d )
    doctest.testmod( data.circle )
    doctest.testmod( data.data )
    doctest.testmod( data.rect )
    doctest.testmod( data.target )
    doctest.testmod( data.movable ) # Should be after extending modules.
    doctest.testmod( graphics.tkcircledrawer )