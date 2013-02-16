import common.application
import common.timestepper
import data.circle
import data.data
import data.level
import data.map
import data.rect
import data.movable
import data.target
import data.vector2d
import formulary.pythagorean
import formulary.rotation
import formulary.stringnumber
import formulary.vector
import fps.fps
import fps.fpscounter
import graphics.tkcircledrawer
import level.levelparser
import physics.circlecirclecollider
import physics.circlerectcollider
import physics.colliderfactory
import physics.movestate
import physics.circlerectreflector
import physics.circlecirclereflector

if __name__ == '__main__':
    import doctest
    doctest.testmod( common.application )
    doctest.testmod( common.timestepper )
    doctest.testmod( data.circle )
    doctest.testmod( data.data )
    doctest.testmod( data.level )
    doctest.testmod( data.map )
    doctest.testmod( data.rect )
    doctest.testmod( data.target )
    doctest.testmod( data.vector2d )
    doctest.testmod( data.movable ) # Should be after extending modules. TODO: Probably will be fixed with #31.
    doctest.testmod( formulary.pythagorean )
    doctest.testmod( formulary.rotation )
    doctest.testmod( formulary.stringnumber )
    doctest.testmod( formulary.vector )
    doctest.testmod( fps.fps )
    doctest.testmod( fps.fpscounter )
    doctest.testmod( graphics.tkcircledrawer )
    doctest.testmod( level.levelparser )
    doctest.testmod( physics.circlecirclecollider )
    doctest.testmod( physics.circlerectcollider )
    doctest.testmod( physics.colliderfactory )
    doctest.testmod( physics.movestate )
    doctest.testmod( physics.circlecirclereflector )
    doctest.testmod( physics.circlerectreflector )