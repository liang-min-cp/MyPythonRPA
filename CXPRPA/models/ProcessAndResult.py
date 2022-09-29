import datetime
import sys

sys.path.append("..")
from models import ProcessCommand
from excel_tools import SummaryCoordinate
from log.logger import logger


class ProcessAndResult:

    def __init__(self, test_circulate_number, cxp_file_path, coordinate: SummaryCoordinate):
        self.Test_Circulate_Number = test_circulate_number  # 测试循环次数
        self.CX_Programmer_Version = None  # CX-Programmer版本号
        self.RX65_Version = None  # RX65固件版本号
        self.AM3352_Version = None  # AM3352固件版本号
        self.Cxp_File_Path = cxp_file_path  # CXP工程路径

        self.TestCommandAllNum = None  # 测试命令总条数
        self.TestCommandSuccessNum = None  # 测试命令成功条数
        self.TestCommandFailedNum = None  # 测试命令失败条数
        self.TestTimeALl = None  # 测试命令总耗时
        self.TestTimeAverage = None  # 测试命令平均耗时
        self.TestResultSummary = None # 测试结果(本case总结果)

        self.ProgramStartTime = datetime.timezone  # 程序开始执行时间
        self.ProgramFinishedTime = datetime.timezone  # 程序结束时间
        self.CommandStartTime = datetime.timezone  # 命令开始测试时间
        self.CommandFinishedTime = datetime.timezone  # 命令结束测试时间

        self.Coordinate = coordinate  # 坐标信息

        self.Commands: list[ProcessCommand] = []  # 所有测试命令集合信息


if __name__ == '__main__':
    processAndResult = ProcessAndResult("4", R"E:\liangmin_oms\TC16\Input Process Data Invalid Error.cxp", 8)
    logger.info(processAndResult.Test_Circulate_Number)
    logger.info(processAndResult.Cxp_File_Path)
    logger.info(processAndResult.CommandStartTime)
    logger.info(processAndResult.TestCommandAllNum)
