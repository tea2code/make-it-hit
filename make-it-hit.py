from common import application

import math

if __name__ == '__main__':
    framesPerSecond = 60
    forceScale = 100 # Anything between 30 and 60 seems to be right.
    windowTitle = 'Make It Hit - {0} (FPS: {1})'
    
    app = application.Application()
    app.fpsCounterMeasures = framesPerSecond
    app.frameTime = 1 / framesPerSecond
    app.forceScale = forceScale
    app.loopTime = math.floor( app.frameTime * 100 )
    app.windowHeight = 800
    app.windowTitle = windowTitle
    app.windowWidth = 900
    app.begin()