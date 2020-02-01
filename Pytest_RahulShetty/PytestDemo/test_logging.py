import logging

def test_logging():

    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('C:\\Users\\vikgaur\\PycharmProjects\\PytestPythonSelFramework\\uitlities\\logfile.log')
    formatter = logging.Formatter("%(asctime)s, : %(levelname)s : %(name)s  : %(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler) #filehandler_object

    #logger.setLevel(logging.error)

    logger.debug('Debug statement is executed')
    logger.info('Info statement is executed')
    logger.warning('Warning statement is executed')
    logger.error('Error statement is executed')
    logger.critical('Critical statement is executed')