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
from CxeStart import CxeStart


class CxeConnect:
    def __init__(self):
        logger.info("CxeConnect init")

    def Run(self):
        logger.info("CxeConnect 开始")
        try:
            logger.info("main_window")
            main_window = auto.WindowControl(Name="CX-EtherCAT")
            logger.info(main_window.ClassName)
            if not main_window.Exists():
                raise Exception("main_window 定位失败")

            text_control_master_add_link = main_window.TextControl(Name="EtherCATSuite Master Unit")
            if not text_control_master_add_link.Exists():
                raise Exception("EtherCATSuite Master Unit 定位失败")
            text_control_master_add_link.Click()
            time.sleep(2)
            text_control_connect = main_window.ButtonControl(Name='连接')
            if not text_control_connect.Exists():
                raise Exception("连接 定位失败")
            text_control_connect.Click()
            time.sleep(10)

        except LookupError as e:
            logger.exception(e)
            # pass
        logger.info("CxeConnect 完成")
        time.sleep(1)


if __name__ == '__main__':
    # logger.info("Begin")
    # CxeStart = CxeStart()
    # CxeStart.Run()

    cxeConnect = CxeConnect()
    cxeConnect.Run()

    # main_window = auto.WindowControl(Name="CX-EtherCAT")
    # logger.info(main_window.ClassName)
    # main_window.SendKeys('{Ctrl}O', waitTime=0.5)
    # logger.info("End")
