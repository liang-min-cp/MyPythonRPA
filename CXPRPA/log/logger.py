# -*- coding:utf-8 -*-
import os
import logging.handlers
import sys

logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

# 处理器
# 1.标准输出
sh = logging.StreamHandler()
# sh.setLevel(logging.INFO)

# 2.文件输出
cur_path = os.path.abspath(os.path.dirname(__file__))
log_path = cur_path.split("CXPRPA")[0] + "\\CXPRPA\\log"
logger_path = log_path + "\\logger.log"

full_path_old = sys.argv[0]
full_path_old_list = full_path_old.split(R"/")
full_path_old_list[full_path_old_list.__len__() - 1] = R"log/logger.log"
logger_path_new = R"/".join(full_path_old_list)

# fh = logging.FileHandler(filename=logger_path, mode='a')
fh = logging.handlers.RotatingFileHandler(logger_path_new, maxBytes=1024 * 1024 * 10, backupCount=5
                                          , encoding='utf-8')  # 最大10M , encoding='utf-8'
# fh.setLevel(logging.INFO)

# 格式器
fmt = logging.Formatter(fmt="%(asctime)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s")

# 给处理器设置格式
sh.setFormatter(fmt)
fh.setFormatter(fmt)


# 记录器设置处理器
logger.addHandler(sh)
logger.addHandler(fh)

if __name__ == '__main__':
    iCount = 0
    while iCount < sys.maxsize:
        # 打印日志代码
        logger.debug("This is  DEBUG of logger !!")
        logger.info("This is  INFO of logger !!")
        logger.warning("This is  WARNING of logger !!")
        logger.error("This is  ERROR of logger !!")
        logger.critical("This is  CRITICAL of logger !!")
        break
