
import logging


def get_logger():
    # Create and configure logger
    logging.basicConfig(filename="/tmp/django.log",
                        format='%(asctime)s\t %(message)s',
                        filemode='w')

    # Creating an object
    logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    return logger