import datetime
import sys

sys.path.append("..")
from excel_tools import ResultCoordinate

from log.logger import logger


class ProcessResult:

    def __init__(self, command_test_serial_num, coordinate: ResultCoordinate):
        self.Command_Test_Serial_Num = command_test_serial_num  # 命令测试序号，表示该命令进入第几次循环测量
        self.Test_Actual_Value = None  # 实际值
        self.Test_Actual_Result = None  # 测试结果
        self.Coordinate = coordinate  # 该次测量结果在Excel中的填写坐标


if __name__ == '__main__':
    processSingleResult = ProcessResult("1")
    logger.info(processSingleResult.Command_Test_Serial_Num)
    logger.info(processSingleResult.Test_Actual_Value)
    logger.info(processSingleResult.Test_Actual_Result)
