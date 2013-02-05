from common import application

import math

if __name__ == '__main__':
    app = application.Application()
    app.frameTime = 1/60
    app.loopTime = math.floor( app.frameTime * 100 )
    app.begin()