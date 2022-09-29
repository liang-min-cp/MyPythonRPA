'''
Template_click.xlsx坐标
'''
import sys

sys.path.append("..")
from log.logger import logger


class CordinateCxeClick:
    def __init__(self):
        self.Sheet_Name = "测试过程及结果"
        self.Test_Cycle_Time_Location = (2, 2)  # 测试循环次数 坐标
        self.Test_Cmd_Summary_Location = (2, 4)  # 测试项目总数目 坐标
        self.Test_Cmd_Success_Location = (3, 4)  # 测试项目成功数目 坐标
        self.Test_Cmd_Failed_Location = (4, 4)  # 测试项目失败数目 坐标
        self.Test_Result_Location = (5, 4)  # 测试结果 坐标
        self.Test_Process_Header_Row = 8  # 测试过程表头行号
        self.Test_Process_Result_Col = 4  # 测试过程的结果所在列
        self.Test_Process_Detail_Start_Col = 5  # 测试过程的结果,明细，起始列
        self.Test_Cmd_Col = 2  # 测测试项目所在列


if __name__ == '__main__':
    logger.info("main")
