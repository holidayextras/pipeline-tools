import logging


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

pre_logger = logging.Logger('pre_logger')
pre_logger.setLevel('DEBUG')
pre_logger.addHandler(console_handler('DEBUG'))


def init_a_logger(log_name, log_level):

    # create logger
    logger = logging.Logger(log_name)
    logger.setLevel(log_level)

    ch = console_handler(log_level)

    # add ch to logger
    logger.addHandler(ch)

    logger.debug('check')

    return logger
