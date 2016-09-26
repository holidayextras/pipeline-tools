import logging
import os
from ConfigParser import ConfigParser


def check_config():
    WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
    CONFIG_FILE = WORKING_DIR + "/config"
    if __name__ != '__main__':
        import __main__
        if '__file__' not in dir(__main__):
            print('----> 1')
            return CONFIG_FILE
        elif ('unittest' in __main__.__file__) or ('pycharm' in __main__.__file__):
            print('----> 2')
            return CONFIG_FILE
        else:
            print('----> 3')
            CONFIG_FILE = os.path.abspath(os.path.dirname(__main__.__file__))\
                          + '/config'
    return CONFIG_FILE


def console_handler(log_level):
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # create formatter to hx standard
    formatter = logging.Formatter('%(asctime)s - %(name)s '
                                  '- %(levelname)s %(module)s:%(lineno)s '
                                  '%(funcName)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)

    return ch

CONFIG_FILE = check_config()
print(CONFIG_FILE)

#  to enable testing we should make a dynamic path available
config = ConfigParser()
config.read(CONFIG_FILE)


def init_a_logger():

    log_name = config.get('override', 'log_name')
    log_level = config.get('override', 'log_level')
    # create logger
    logger = logging.Logger(log_name)
    logger.setLevel(log_level)

    ch = console_handler(log_level)

    # add ch to logger
    logger.addHandler(ch)

    logger.debug('check')

    return logger
