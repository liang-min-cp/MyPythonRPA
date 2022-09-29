import datetime
import sys

sys.path.append("..")
from excel_tools import CommandCoordinate

from log.logger import logger

from models.ProcessResult import ProcessResult


class ProcessCommand:

    def __init__(self, command_seq_num, execution_phase, test_method, command_name, expect_value, wait_time, execute_times,
                 coordinate: CommandCoordinate):
        self.Command_Seq_Num = command_seq_num  # 序号
        self.Execution_Phase = execution_phase  # 执行阶段
        self.Test_Method = test_method  # 测试方式
        self.Command_Name = command_name  # 操作命令/名称
        self.Expect_Value = expect_value  # 期待值
        self.Wait_Time = wait_time  # 超时等待时间
        self.Test_Result = None  # 测试结果

        self.Execute_Times = execute_times  # 当前命令执行次数
        self.Coordinate: CommandCoordinate = coordinate  # 本条数据Excel坐标信息

        self.Test_Results: list[ProcessResult] = []  # 该命令循环测量结果集合


if __name__ == '__main__':
    testProcessSingleCommand = ProcessCommand("1", R"准备", "cxp", "0-启动CXP", "OK", "10")
    logger.info(testProcessSingleCommand.Command_Seq_Num)
    logger.info(testProcessSingleCommand.Execution_Phase)
    logger.info(testProcessSingleCommand.Test_Method)
    logger.info(testProcessSingleCommand.Command_Name)
    logger.info(testProcessSingleCommand.Test_Results)
