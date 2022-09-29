import sys
import time

sys.path.append("..")
from log.logger import logger
from models import ProcessAndResult
import uiautomation as auto


class CxpDeliverDown:
    def __init__(self, process_and_result: ProcessAndResult):
        logger.info('CxpConnectPlc __init__')
        self.processAndResult = process_and_result
        self.Name = "传输程序与设置"

    def Run(self):
        logger.info("传输程序与设置 开始处理")
        self.SetResult("OK")

        # 点击传送按钮，{Ctrl}T
        main_window = auto.WindowControl(ClassName=R'OMRON CX-Programmer', searchDepth=1)
        if main_window.Exists():
            main_window.SendKeys('{Ctrl}T', waitTime=2)
            logger.info("点击传送按钮，{Ctrl}T - 完成")
        else:
            logger.info("点击传送按钮，{Ctrl}T - 失败")

        #  点击 传送全部 按钮
        send_all_btn = main_window.ButtonControl(Name='传送全部', foundIndex=1)
        if send_all_btn.Exists(maxSearchSeconds=10):
            send_all_btn.Click()
            logger.info("点击【传送全部】按钮 - 完成")
        else:
            logger.info("点击【传送全部】按钮 - 失败")

        # 处理按钮 【传送所有数据到PLC想要继续吗？】
        confirm_send_all_to_plc_btn = main_window.ButtonControl(Name='是(Y)', foundIndex=1)
        if confirm_send_all_to_plc_btn.Exists():
            confirm_send_all_to_plc_btn.Click()
            logger.info("处理按钮 【传送所有数据到PLC想要继续吗？】 - 完成")
        else:
            logger.info("处理按钮 【传送所有数据到PLC想要继续吗？】 - 失败")

        confirm_again_send_all_to_plc_btn = main_window.ButtonControl(Name='是(Y)', foundIndex=1)
        if confirm_again_send_all_to_plc_btn.Exists():
            confirm_again_send_all_to_plc_btn.Click()
            logger.info("处理按钮 【此命令将影响所连接的PLC的状态，要继续吗？】 - 完成")
        else:
            logger.info("处理按钮 【此命令将影响所连接的PLC的状态，要继续吗？】 - 失败")

        # 【程序下载到PLC，下载成功，点击确定】按钮
        send_all_to_plc_ok_btn = main_window.ButtonControl(Name='确定', ClassName='Button', AutomationId='2')
        if send_all_to_plc_ok_btn.Exists():
            send_all_to_plc_ok_btn.Click()
            logger.info("处理按钮 【程序下载到PLC，下载成功，点击确定】按钮 - 完成")
        else:
            logger.info("处理按钮 【程序下载到PLC，下载成功，点击确定】按钮 - 失败")
        time.sleep(1)
        logger.info("传输程序与设置 完成")

    def SetResult(self, test_result):
        # 写入测量结果
        for Command in self.processAndResult.Commands:
            if Command.Command_Name == self.Name:
                Command.Test_Result = test_result
                break


if __name__ == '__main__':
    logger.info("Begin 传输程序与设置")

    logger.info('Finised 传输程序与设置')
