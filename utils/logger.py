__maintainer__ = ['santosh.sharma']

import os
import logging


class Logger:

    path = os.getcwd()
    par_dir = os.path.abspath(os.path.join(path, os.pardir))
    log_dir = os.path.join(par_dir, "logs")
    filename = __file__.split("/")[-1].split(".")[0]

    @staticmethod
    def logger(filename,
               logger_name=__name__,
               log_level=logging.DEBUG,
               filemode='w',
               formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(name)s: %(message)s',
                                           datefmt='%d/%m/%Y %H:%M:%S')
               ):
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(filename, mode=filemode)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        return logger
