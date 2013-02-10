from common import application

import math

if __name__ == '__main__':
    framesPerSecond = 60
    forceScale = 42 # Anything between 30 and 60 seems to be right.
    
    app = application.Application()
    app.frameTime = 1 / framesPerSecond
    app.forceScale = forceScale
    app.loopTime = math.floor( app.frameTime * 100 )
    app.begin()