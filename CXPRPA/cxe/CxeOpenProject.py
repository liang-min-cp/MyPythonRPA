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


class CxeOpenProj:
    def __init__(self):
        self.Cxp_Program_Path = R"C:\Program Files (x86)\OMRON\CX-EtherCAT\CX-EtherCAT.exe"
        self.Cxp_Project_Path = R"C:\Users\min.liang\Desktop\temp\project.ecc"
        self.Name = "CxeOpenProj"
        self.PopenObj = None
        logger.info("CxeOpenProj init")

    def Run(self):
        logger.info("加载Proj 开始")
        try:
            logger.info("main_window")
            main_window = auto.WindowControl(Name="CX-EtherCAT")
            logger.info(main_window.ClassName)
            if main_window.Exists():
                main_window.SendKeys('{Ctrl}O', waitTime=0.1)
                time.sleep(2)
            else:
                raise Exception("Not Found main window")

            # tool_bar_control = main_window.ToolBarControl(ClassName='ToolbarWindow32')
            # logger.info(tool_bar_control.Name)
            # tool_bar_control.Click()
            # tool_bar_control.DoubleClick()
            split_btn_control = main_window.SplitButtonControl(Name='所有位置')
            split_btn_control.Click()
            time.sleep(1)
            edit_control_address = main_window.EditControl(Name='地址')
            edit_control_address.SendKeys(R"C:\Users\min.liang\Desktop\temp1", waitTime=0.1)
            edit_control_address.SendKeys('{Enter}', waitTime=0.1)

            logger.info("tool_bar_control DoubleClick Finished")

        except LookupError as e:
            logger.exception(e)
            # pass
        logger.info("启动CX-EtherCAT软件 完成")
        time.sleep(1)


if __name__ == '__main__':
    # logger.info("Begin")
    # CxeStart = CxeStart()
    # CxeStart.Run()

    cxeOpenProj = CxeOpenProj()
    cxeOpenProj.Run()

    # main_window = auto.WindowControl(Name="CX-EtherCAT")
    # logger.info(main_window.ClassName)
    # main_window.SendKeys('{Ctrl}O', waitTime=0.5)
    # logger.info("End")
