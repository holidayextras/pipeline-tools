import logging
import os
from ConfigParser import ConfigParser

WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
print(os.getcwdu())
print(os.path.dirname(os.path.realpath(__file__)))

if __name__ != '__main__':
    import __main__
    if '__file__' in dir(__main__):
        WORKING_DIR = os.path.abspath(os.path.dirname(__main__.__file__))
        if 'unittest' in WORKING_DIR:
            WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
print(WORKING_DIR)
CONFIG_FILE = WORKING_DIR + "/config"

#  to enable testing we should make a dynamic path available
config = ConfigParser()
config.read(CONFIG_FILE)


def init_a_logger():

    log_name = config.get('override', 'log_name')
    log_level = config.get('override', 'log_level')
    # create logger
    logger = logging.Logger(log_name)
    logger.setLevel(log_level)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # create formatter to hx standard
    formatter = logging.Formatter('%(asctime)s - %(name)s '
                                  '- %(levelname)s %(module)s:%(lineno)s '
                                  '%(funcName)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger