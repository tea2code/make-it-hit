from common import application
from common import errorhandler

import sys

if __name__ == '__main__':
    
    errHandler = errorhandler.ErrorHandler()
    errHandler.register()

    app = application.Application()
    errHandler.data.append( app.data )
    
    app.configPath = 'config.yaml'
    app.defaultConfigPath = 'default-config.yaml'
    app.begin()