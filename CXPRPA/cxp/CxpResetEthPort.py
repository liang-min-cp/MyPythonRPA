import sys
import time

sys.path.append("..")
from log.logger import logger
from models import ProcessAndResult
import uiautomation as auto


class CxpResetEthPort:
    def __init__(self, process_and_result: ProcessAndResult):
        logger.info('CxpResetEthPort __init__')
        self.processAndResult = process_and_result
        self.Name = "重置以太网端口"

    def Run(self):
        logger.info("重置以太网端口 开始")
        self.SetResult("OK")
        main_window = auto.WindowControl(ClassName=R'OMRON CX-Programmer', searchDepth=1)
        main_window.SendKeys('{Ctrl}T', waitTime=0.1)
        logger.info("点击传送全部按钮 - 开始")
        time.sleep(2)
        send_all_btn = main_window.ButtonControl(Name='传送全部',  foundIndex=1)
        send_all_btn.Click()
        logger.info("传送所有数据到PLC想要继续吗？ - 点击按钮")
        time.sleep(1)
        confirm_send_all_to_plc_btn = main_window.ButtonControl(Name='是(Y)', foundIndex=1)
        confirm_send_all_to_plc_btn.Click()
        logger.info("此命令将影响所连接的PLC的状态，要继续吗？ - 点击按钮")
        time.sleep(1)
        confirm_again_send_all_to_plc_btn = main_window.ButtonControl(Name='是(Y)', foundIndex=1)
        confirm_again_send_all_to_plc_btn.Click()
        logger.info("下载成功，点击确定")
        time.sleep(5)
        send_all_to_plc_ok_btn = main_window.ButtonControl(Name='确定', foundIndex=1)
        send_all_to_plc_ok_btn.Click()
        time.sleep(2)
        logger.info("传输程序与设置 完成")

    def SetResult(self, test_result):
        # 写入测量结果
        for Command in self.processAndResult.Commands:
            if Command.Command_Name == self.Name:
                Command.Test_Result = test_result
                break


if __name__ == '__main__':
    logger.info("重置以太网端口 - 开始")
    main_window = auto.WindowControl(ClassName=R'OMRON CX-Programmer', searchDepth=1)
    logger.info(main_window.ClassName)
    plc_menuItemControl = main_window.MenuItemControl(Name='PLC',  foundIndex=1)

    plc_menuItemControl.Show()
    time.sleep(100)




