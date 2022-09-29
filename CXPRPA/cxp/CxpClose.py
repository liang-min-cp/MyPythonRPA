import sys

sys.path.append("..")
from log.logger import logger
from cxp.CxpStart import CxpStart
from models import ProcessAndResult


class CxpClose:
    def __init__(self, cxp_start: CxpStart, process_and_result: ProcessAndResult):
        logger.info('CxpClose __init__')
        self.processAndResult = process_and_result
        self.Cxp_Start_Obj = cxp_start
        self.Name = "关闭CXP程序"

    def Run(self):
        #  关闭Cxp软件
        # try:
        #     if self.PopenObj is not None:
        #         logger.info("PopenObj closed")
        #         self.PopenObj.kill()
        #     else:
        #         logger.info("PopenObj closed failed: PopenObj is null ")
        # except Exception as e:
        #     logger.exception(e)
        #     pass
        self.Cxp_Start_Obj.Kill()
        self.SetResult("OK")
        logger.info("CxpClose Run Finished")

    def SetResult(self, test_result):
        # 写入测量结果
        for Command in self.processAndResult.Commands:
            if Command.Command_Name == self.Name:
                Command.Test_Result = test_result
                break


if __name__ == '__main__':
    # logger.info("Begin Start CXP")
    # cxpStart = CxpStart(R"E:\liangmin_oms\TC16\Input Process Data Invalid Error.cxp")
    # cxpClose = CxpClose(cxpStart)
    # listExecutionCommands = [cxpStart, cxpClose]
    # for listExecutionCommand in listExecutionCommands:
    #     # if type(listExecutionCommand) is CxpClose:
    #     #     listExecutionCommand.PopenObj = listExecutionCommands[0].PopenObj
    #     #     logger.info("CxpClose PopenObj is Ready")
    #     listExecutionCommand.Run()
    #     time.sleep(5)
    #     logger.info("Finished: " + str(listExecutionCommand.__class__))

    logger.info('Finised All')
