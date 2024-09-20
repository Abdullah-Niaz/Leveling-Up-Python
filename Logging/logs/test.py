from loggers import logging


def add(a, b):
    '''This fucntion is adding up two numbers'''
    logging.debug("This function is performing addition of two")
    return a + b


logging.debug("Addition function has been called")
add(20, 30)
