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
    app.loopTime = math.floor( app.frameTime * 1000 )
    app.startTime = 2000
    app.windowHeight = 1000
    app.windowTitle = windowTitle
    app.windowWidth = 1000
    app.begin()