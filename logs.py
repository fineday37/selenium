import logging
from logging.handlers import TimedRotatingFileHandler
import os
import datetime


def Format():
    time = datetime.datetime.now().strftime("%Y-%m-%d")
    test_log = logging.getLogger()
    test_log.setLevel(logging.ERROR)
    filename = os.path.join(os.path.dirname(__file__), "log " + time + " .txt")
    fh = TimedRotatingFileHandler(
        filename='1',
        when='S',
        encoding="GB2312",
        interval=1,
        backupCount=2
    )
    fh.suffix = '%Y-%m-%d_%H-%M-%S.log'
    sh = logging.StreamHandler()
    # test_log.addHandler(sh)
    # test_log.addHandler(fh)
    formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s")
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    if not test_log.handlers:
        test_log.addHandler(sh)
        test_log.addHandler(fh)
    return test_log


logger = Format()

if __name__ == '__main__':
    logger.info("合格")
    logger.info("合格")
    logger.error("不合格")
