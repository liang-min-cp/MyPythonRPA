import os
import sys
import subprocess
import time
import uiautomation as auto
import signal
import psutil
import pythoncom

sys.path.append("..")
from log.logger import logger
from models import ProcessAndResult
import pyautogui as gui


class CxeStart:
    def __init__(self):
        self.Cxp_Program_Path = R"C:\Program Files (x86)\OMRON\CX-EtherCAT\CX-EtherCAT.exe"
        self.Cxp_Project_Path = R"C:\Users\min.liang\Desktop\temp\project.ecc"
        self.Name = "启动CXP"
        self.PopenObj = None
        logger.info("CxeStart init")

    def Run(self):

        # os.system(f"attrib -r {self.Cxp_Program_Path}")
        # 判断当前系统有CXE进程，先Kill
        logger.info("检查CXE进程")
        for prc in psutil.process_iter():
            if prc.name().lower() == "cx-ethercat.exe":
                os.kill(prc.pid, signal.SIGILL)
                logger.info("发现进程:{0}, {1}，杀死".format(prc.name(), str(prc.pid)))

        logger.info("启动Cxe软件 开始")
        #  启动Cxp软件

        self.PopenObj = subprocess.Popen([self.Cxp_Program_Path, self.Cxp_Project_Path])
        time.sleep(6)
        # 处理试用弹窗
        try:
            logger.info("main_window")
            main_window = auto.WindowControl(Name="CX-EtherCAT")
            logger.info(main_window.ClassName)
            if main_window.Exists():
                main_window.Maximize()
                logger.info("窗口最大化 - 完成")
            else:
                logger.info("窗口最大化 - 失败")

        except LookupError as e:
            logger.exception(e)
            # pass
        logger.info("启动CX-EtherCAT软件 完成")
        time.sleep(1)

    def Kill(self):
        if self.PopenObj is not None:
            logger.info("PopenObj Kill")
            self.PopenObj.kill()
        else:
            logger.info("PopenObj closed failed: PopenObj is null ")


if __name__ == '__main__':
    logger.info("Begin Start CXE")
    cxeStart = CxeStart()
    cxeStart.Run()
    time.sleep(100)
    cxeStart.Kill()
