import sys
from copy import deepcopy

sys.path.append("..")
from log.logger import logger


class test01:
    def __init__(self):
        self.a = 11
        self.b = 12


class test02:
    def __init__(self, test: test01):
        self.Test = deepcopy(test)

    def Run(self):
        self.Test.a = 111
        self.Test.b = 222


class test03:
    def __init__(self):
        logger.info("test03 init")

    def Run(self):
        logger.info(self.__class__.__name__)


class BaseCommand:
    def __init__(self):
        logger.info("BaseCommand init")

    def run(self):
        logger.info("BaseCommand run")


if __name__ == "__main__":
    t03 = test03()
    t03.Run()
    logger.info(t03.__class__.__name__)

    logger.info("===================")
    t01 = test01()
    logger.info(t01.__dict__)
    t02 = test02(t01)
    logger.info(t02.Test.a)
    logger.info(t02.Test.b)
    logger.info("===================")
    t02.Run()
    logger.info(t01.__dict__)
    logger.info(t02.Test.a)
    logger.info(t02.Test.b)
    logger.info("===================")
