import sys

sys.path.append("..")
from fins.FinsCommand import FinsCommand
from models.SysConfig import SysConfigModel

from cxp.CxpClose import CxpClose
from cxp.CxpConnectPlc import CxpConnectPlc
from cxp.CxpDeliverDown import CxpDeliverDown

from cxp.CxpStart import CxpStart

from models import ProcessAndResult
from log.logger import logger


class RegisterExecutions:
    def __init__(self, process_and_result: ProcessAndResult, sys_config_model: SysConfigModel):
        self.processAndResult = process_and_result
        self.sysConfigModel = sys_config_model
        self.listCmd = []
        self.CxpStartObj = CxpStart(process_and_result)
        self.CxpConnectPlcObj = CxpConnectPlc(sys_config_model, process_and_result)
        self.CxpDeliverDownObj = CxpDeliverDown(process_and_result)
        self.CxpCloseObj = CxpClose(self.CxpStartObj, process_and_result)
        self.Cxp = {
            "启动CXP": self.CxpStartObj,
            "建立连接": self.CxpConnectPlcObj,
            "传输程序与设置": self.CxpDeliverDownObj,
            "关闭CXP程序": self.CxpCloseObj,
        }

    def RegisterCommands(self):
        # (1) 注册准备阶段
        for CommandReady in self.processAndResult.Commands:
            if CommandReady.Execution_Phase == "准备":
                logger.info("开始注册：" + CommandReady.Command_Name)
                if CommandReady.Command_Name in self.Cxp.keys():
                    self.listCmd.append(self.Cxp[CommandReady.Command_Name])
                    logger.info("注册成功：" + CommandReady.Command_Name)
                else:
                    logger.info("注册失败：" + CommandReady.Command_Name)

        # （2）注册测试阶段
        test_Circulate_Number = self.processAndResult.Test_Circulate_Number  # 测试循环次数
        logger.info("测试循环总次数: " + str(test_Circulate_Number))
        for i in range(test_Circulate_Number):
            for CommandExecution in self.processAndResult.Commands:
                if CommandExecution.Execution_Phase == "测试":
                    logger.info("开始注册：" + CommandExecution.Command_Name)
                    finsCommand = FinsCommand(self.sysConfigModel,
                                              self.processAndResult,
                                              CommandExecution.Command_Seq_Num,
                                              i + 1)
                    self.listCmd.append(finsCommand)

        # （3）注册结束阶段
        for CommandEnd in self.processAndResult.Commands:
            if CommandEnd.Execution_Phase == "结束":
                logger.info("开始注册：" + CommandEnd.Command_Name)
                if CommandEnd.Command_Name in self.Cxp.keys():
                    self.listCmd.append(self.Cxp[CommandEnd.Command_Name])
                    logger.info("注册成功：" + CommandEnd.Command_Name)
                else:
                    logger.info("注册失败：" + CommandEnd.Command_Name)
