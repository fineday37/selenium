import logging


def loggings():
    # 创建日志器
    logger = logging.getLogger()
    # 设置级别
    logger.setLevel(logging.INFO)
    # 指定日志显示的位置

    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 日志信息显示到控制台
    logger.addHandler(sh)
    # 创建文件处理器
    fh = logging.FileHandler('log.txt', encoding="utf-8")
    logger.addHandler(fh)
    # 日志生成时间，日志是正确的还是错误的，修改格式
    # 创建格式器，格式字符串,文件名，方法，日志级别,日志信息
    formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s")
    # 格式赋予控制台
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    return logger


if __name__ == '__main__':
    loggings().info("debug日志信息")

# logger.info("info日志信息")
# logger.debug("debug日志信息")
# logger.error("error日志信息")
# logger.critical("critical日志信息")
