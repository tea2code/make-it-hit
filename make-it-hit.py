from common import application

import math

if __name__ == '__main__':
    framesPerSecond = 60
    forceScale = 100
    windowTitle = 'Make It Hit - {0} (FPS: {1})'
    
    app = application.Application()
    app.fpsCounterMeasures = framesPerSecond
    app.frameTime = 1 / framesPerSecond
    app.forceScale = forceScale
    app.levelExtension = '.yaml'
    app.loopTime = math.floor( app.frameTime * 1000 )
    app.menuBarWidth = 120
    app.startTime = 1500
    app.windowHeight = 768
    app.windowTitle = windowTitle
    app.windowWidth = 1024
    app.begin()