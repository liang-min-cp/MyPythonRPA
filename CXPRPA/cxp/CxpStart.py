import os
import sys
import subprocess
import time
import uiautomation as auto
import signal
import psutil

sys.path.append("..")
from log.logger import logger
from models import ProcessAndResult
import pyautogui as gui


class CxpStart:
    def __init__(self, process_and_result: ProcessAndResult):
        self.Cxp_Program_Path = R"C:\Program Files (x86)\OMRON\CX-One\CX-Programmer\CX-P.exe"
        self.processAndResult = process_and_result
        self.Cxp_Project_Path = process_and_result.Cxp_File_Path
        self.Name = "启动CXP"
        self.PopenObj = None
        logger.info("BaseCommand init")

    def Run(self):
        # 判断当前系统有CXP进程，先Kill
        logger.info("检查CXP进程")
        for prc in psutil.process_iter():
            if prc.name().lower() == "cx-p.exe":
                os.kill(prc.pid, signal.SIGILL)
                logger.info("发现进程:{0}, {1}，杀死".format(prc.name(), str(prc.pid)))

        logger.info("启动Cxp软件 开始")
        #  启动Cxp软件
        self.PopenObj = subprocess.Popen([self.Cxp_Program_Path, self.Cxp_Project_Path])
        # 处理试用弹窗
        try:
            logger.info("Begin 处理试用弹窗")

            trial_info_Wnd = auto.WindowControl(ClassName='#32770', searchDepth=2)

            ######################
            # auto.WaitForExist()
            # testControl = auto.WindowControl(ClassName='#327asa', searchDepth=2)
            # if testControl.Exists():
            #     logger.info("testControl Exists")
            # else:
            #     logger.info("testControl not Exists")
            # time.sleep(100)
            ###########################

            if trial_info_Wnd.Exists():
                logger.info(trial_info_Wnd.Name)  # CX-Programmer v9.7
                text_element = trial_info_Wnd.TextControl(AutomationId='65535')  # 获取弹框元素，window是我们上一步获取的主界面对象
                alert_info = text_element.Name
                logger.info(alert_info)
                if alert_info.__contains__("这是仅用于评价的未注册的全功能版本"):
                    btn = trial_info_Wnd.ButtonControl(AutomationId='2')
                    btn.Click()
            logger.info("处理试用弹窗 - 完成")

            ####################################
            # 窗口最大化
            # time.sleep(1)
            main_window = auto.WindowControl(ClassName=R'OMRON CX-Programmer', searchDepth=1)
            if main_window.Exists():
                main_window.Maximize()
                logger.info("窗口最大化 - 完成")
            else:
                logger.info("窗口最大化 - 失败")

        except LookupError as e:
            logger.exception(e)
            # pass
        logger.info("启动Cxp软件 完成")
        time.sleep(1)

    def SetResult(self, test_result):
        # 写入测量结果
        for Command in self.processAndResult.Commands:
            if Command.Command_Name == self.Name:
                Command.Test_Result = test_result
                break

    # if type(listExecutionCommand) is CxpClose:
    #     listExecutionCommand.PopenObj = listExecutionCommands[0].PopenObj
    #     logger.info("CxpClose PopenObj is Ready")

    def Kill(self):
        if self.PopenObj is not None:
            logger.info("PopenObj Kill")
            self.PopenObj.kill()
        else:
            logger.info("PopenObj closed failed: PopenObj is null ")


if __name__ == '__main__':
    logger.info("Begin Start CXP")
    cxpStart = CxpStart(R"E:\liangmin_oms\TC16\Input Process Data Invalid Error.cxp")
    cxpStart.Run()
    time.sleep(100)
    cxpStart.Kill()
