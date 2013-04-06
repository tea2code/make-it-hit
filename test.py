import common.application
import common.enum
import common.timestepper
import data.circle
import data.collisionevent
import data.configuration
import data.data
import data.event
import data.level
import data.map
import data.movable
import data.pointsevent
import data.rect
import data.target
import data.targetevent
import data.vector2d
import formulary.comparison
import formulary.pythagorean
import formulary.rotation
import formulary.vector
import formulary.screenconvert
import fps.fps
import fps.fpscounter
import graphics.tkborderdrawer
import graphics.tkcircledrawer
import graphics.tkcollisiondrawer
import graphics.tkrectdrawer
import level.xmlparser
import level.yamlparser
import physics.circlecirclecollider
import physics.circlerectreflector
import physics.circlerectcollider
import physics.circlecirclereflector
import physics.colliderfactory
import physics.collision
import physics.movestate
import physics.reflectorfactory
import postframe.postframe

if __name__ == '__main__':
    import doctest
    doctest.testmod( common.application )
    doctest.testmod( common.enum )
    doctest.testmod( common.timestepper )
    doctest.testmod( data.circle )
    doctest.testmod( data.collisionevent )
    doctest.testmod( data.configuration )
    doctest.testmod( data.data )
    doctest.testmod( data.event )
    doctest.testmod( data.level )
    doctest.testmod( data.map )
    doctest.testmod( data.movable )
    doctest.testmod( data.pointsevent )
    doctest.testmod( data.rect )
    doctest.testmod( data.target )
    doctest.testmod( data.targetevent )
    doctest.testmod( data.vector2d )
    doctest.testmod( formulary.comparison )
    doctest.testmod( formulary.pythagorean )
    doctest.testmod( formulary.rotation )
    doctest.testmod( formulary.vector )
    doctest.testmod( formulary.screenconvert )
    doctest.testmod( fps.fps )
    doctest.testmod( fps.fpscounter )
    doctest.testmod( graphics.tkborderdrawer )
    doctest.testmod( graphics.tkcircledrawer )
    doctest.testmod( graphics.tkcollisiondrawer )
    doctest.testmod( graphics.tkrectdrawer )
    doctest.testmod( level.xmlparser )
    doctest.testmod( level.yamlparser )
    doctest.testmod( physics.circlecirclecollider )
    doctest.testmod( physics.circlecirclereflector )
    doctest.testmod( physics.circlerectcollider )
    doctest.testmod( physics.circlerectreflector )
    doctest.testmod( physics.colliderfactory )
    doctest.testmod( physics.collision )
    doctest.testmod( physics.movestate )
    doctest.testmod( physics.reflectorfactory )
    doctest.testmod( postframe.postframe )

