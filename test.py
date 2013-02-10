import common.application
import common.formulary
import common.timestepper
import data.circle
import data.data
import data.level
import data.map
import data.rect
import data.movable
import data.target
import data.vector2d
import graphics.tkcircledrawer
import level.levelparser

if __name__ == '__main__':
    import doctest
    doctest.testmod( common.application )
    doctest.testmod( common.formulary )
    doctest.testmod( common.timestepper )
    doctest.testmod( data.circle )
    doctest.testmod( data.data )
    doctest.testmod( data.level )
    doctest.testmod( data.map )
    doctest.testmod( data.rect )
    doctest.testmod( data.target )
    doctest.testmod( data.vector2d )
    doctest.testmod( data.movable ) # Should be after extending modules.
    doctest.testmod( graphics.tkcircledrawer )
    doctest.testmod( level.levelparser )