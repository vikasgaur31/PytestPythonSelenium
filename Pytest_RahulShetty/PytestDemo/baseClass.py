import inspect
import logging

class baseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s, : %(levelname)s : %(name)s  : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # filehandler_object

        logger.setLevel(logging.DEBUG)

        #logger.debug('Debug statement is executed')
        return logger
