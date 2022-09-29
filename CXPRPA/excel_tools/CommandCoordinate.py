import datetime
import sys

sys.path.append("..")
from log.logger import logger


class CommandCoordinate:

    # DetailTableHeadRowNum = 8  # Excel明细表头行号
    def __init__(self, command_seq_num: int, detail_table_head_row_num: int):
        self.CurrentRow = command_seq_num + detail_table_head_row_num  # 当前行号

        self.Command_Seq_Num_Location = (self.CurrentRow, 1)  # 序号
        self.Execution_Phase_Location = (self.CurrentRow, 2)  # 执行阶段
        self.Test_Method_Location = (self.CurrentRow, 3)  # 测试方式
        self.Command_Name_Location = (self.CurrentRow, 4)  # 操作命令/名称
        self.Expect_Value_Location = (self.CurrentRow, 6)  # 期待值
        self.Wait_Time_Location = (self.CurrentRow, 7)  # 超时等待时间
        self.Test_Result_Location = (self.CurrentRow, 8)  # 测试结果
        self.Sheet_Name = "测试过程及结果"


if __name__ == '__main__':
    processCommandCoordinate = CommandCoordinate(1, 2)
    logger.info(processCommandCoordinate.CurrentRow)
