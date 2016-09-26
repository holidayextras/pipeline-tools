import os
from configparser import ConfigParser

# Use this to determine the config file directory
def check_config():
    WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
    CONFIG_FILE = WORKING_DIR + "/config"
    if __name__ != '__main__':
        import __main__
        if '__file__' not in dir(__main__):
            return CONFIG_FILE
        elif ('unittest' in __main__.__file__) or ('pycharm' in __main__.__file__):
            return CONFIG_FILE
        else:
            CONFIG_FILE = os.path.abspath(os.path.dirname(__main__.__file__)) \
                          + '/config'
    return CONFIG_FILE

CONFIG_FILE = check_config()

#  to enable testing we should make a dynamic path available
config = ConfigParser()
config.read(CONFIG_FILE)