from common import application

if __name__ == '__main__':
    app = application.Application()
    app.configPath = 'config.yaml'
    app.defaultConfigPath = 'default-config.yaml'
    app.begin()