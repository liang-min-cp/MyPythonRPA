import datetime
import sys

sys.path.append("..")
from log.logger import logger


class SummaryCoordinate:

    def __init__(self):
        self.Test_Circulate_Number_Location = (2, 2)  # 测试循环次数, 坐标
        self.CX_Programmer_Version_Location = (3, 2)  # CX-Programmer版本号
        self.RX65_Version_Location = (4, 2)  # RX65固件版本号
        self.AM3352_Version_Location = (5, 2)  # AM3352固件版本号
        self.Cxp_File_Path_Location = (2, 4)  # CXP工程路径, 坐标

        self.TestCommandAllNum_Location = (3, 4)  # 测试命令总条数, 坐标
        self.TestCommandSuccessNum_Location = (4, 4)  # 测试命令成功条数, 坐标
        self.TestCommandFailedNum_Location = (5, 4)  # 测试命令失败条数, 坐标
        self.TestTimeALl_Location = (2, 6)  # 测试命令总耗时, 坐标
        self.TestTimeAverage_Location = (3, 6)  # 测试命令平均耗时, 坐标
        self.TestResultSummary_Location = (4, 6)  # 测试结果(本case总结果)

        self.Detail_Table_Head_Row_Num = 8  # 当前表格中明细表头所在行数
        self.Start_Col_Num = 9  # 测量结果，例如：实际值1，起始列数
        self.Sheet_Name = "测试过程及结果"


if __name__ == '__main__':
    summaryCoordinate = SummaryCoordinate()
    logger.info(summaryCoordinate.Test_Circulate_Number_Location)
    logger.info(summaryCoordinate.__dict__)
