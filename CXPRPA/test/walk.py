import os
import sys

sys.path.append("..")
from log.logger import logger


# # "CX-P.exe"
# find_path = os.walk()
# logger.info(find_path)

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)


# R"C:\Program Files (x86)\OMRON\CX-One\CX-Programmer\CX-P.exe"
#   C:\\Program Files (x86)\\OMRON\\CX-One\\CX-Programmer\\CX-P.exe

filepath = findfile("CX-P.exe", ":")
logger.info(filepath)
# res = filepath.split(':')
# logger.info("\\")
# res_path = filepath.replace(":", ":\\").replace("\\", "\\\\")
# logger.info(res_path)
# os.system(res_path)
