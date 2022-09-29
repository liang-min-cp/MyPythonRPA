import sys
import time

sys.path.append("..")

from fins.FinsBase import FinsBase
from models.SysConfig import SysConfigModel
from log.logger import logger
from models import ProcessAndResult
import uiautomation as auto
from exceptions.ConnectError import ConnectError


class CxpConnectPlc:
    def __init__(self, sys_config_model: SysConfigModel, process_and_result: ProcessAndResult):
        logger.info('CxpConnectPlc __init__')
        self.processAndResult = process_and_result
        self.sysConfigModel = sys_config_model
        self.Name = "建立连接"

    def Run(self):
        logger.info("建立连接 开始")
        self.SetResult("OK")

        ###################################
        main_window = auto.WindowControl(ClassName=R'OMRON CX-Programmer', searchDepth=1)
        plc_tree_item = main_window.TreeItemControl(searchDepth=8, foundIndex=2)
        if plc_tree_item.Exists():
            plc_tree_item.Click()
            logger.info("点击plc图标 - 完成")
        else:
            logger.info("点击plc图标 - 失败")
        time.sleep(1)
        ##################################
        # 发送 Ctrl+W 快捷键
        main_window.SendKeys('{Ctrl}w', waitTime=0.1)
        logger.info("连接PLC,  快捷键{Ctrl+W} - 完成")
        time.sleep(1)

        ##################################
        # 使用“Y”确认（点击“是”）
        logger.info("即将连接到PLC，点击确认按钮 - 开始处理")
        connect_to_plc_yes_btn = main_window.ButtonControl(Name='是(Y)', foundIndex=1)
        if connect_to_plc_yes_btn.Exists():
            connect_to_plc_yes_btn.Click()
            logger.info("点击【即将连接到PLC，点击确认按钮】按钮 - 完成")
        else:
            logger.info("点击【即将连接到PLC，点击确认按钮】按钮 - 失败")

        # 获取成功连接的状态msctls_statusbar32
        statusBarControl = main_window.StatusBarControl(ClassName="msctls_statusbar32", foundIndex=2)
        connect_status = False
        if statusBarControl.Exists():
            for i in range(30):
                logger.info("确认连接成功状态第几次： " + str(i))
                statusBarControl_Children = statusBarControl.GetChildren()
                logger.info(statusBarControl_Children.__len__())
                # newCP2E(网络:0,节点:0) - 运行模式
                # newCP2E(网络:0,节点:0) - 离线
                for Child in statusBarControl_Children:
                    child_name = Child.Name
                    logger.info(child_name)
                    if child_name.startswith("newCP2E") \
                            and not child_name.endswith("离线"):
                        logger.info("连接成功")
                        connect_status = True
                        break
                if connect_status:
                    break
                time.sleep(1)
        else:
            logger.info("未捕获到状态栏： 获取连接成功状态失败")

        if not connect_status:
            raise ConnectError("确认连接到下位机状态失败！")

        logger.info("建立连接 完成")
        #  连接完成之后,初始化为[编程模式] "0402FFFF"
        finsBase = FinsBase(self.sysConfigModel.Ip_Computer.strip(), self.sysConfigModel.Ip_Plc.strip(),
                            int(self.sysConfigModel.Port))
        res = finsBase.ExecuteFinsAndGetResult("0402FFFF")
        logger.info("初始化为【编程模式】: " + "无响应" if res == "" else "初始化为[编程模式] Ok : " + res)
        time.sleep(2)

    def SetResult(self, test_result):
        # 写入测量结果
        for Command in self.processAndResult.Commands:
            if Command.Command_Name == self.Name:
                Command.Test_Result = test_result
                break


if __name__ == '__main__':
    logger.info("测试Fins")
    finsBase = FinsBase("192.168.250.5", "192.168.250.1", 9600)
    res = finsBase.ExecuteFinsAndGetResult("0402FFFF")
    logger.info(res)
    logger.info('Finised')




















