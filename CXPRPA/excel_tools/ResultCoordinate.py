import sys

sys.path.append("..")
from log.logger import logger


class ResultCoordinate:

    # 当前行号， 执行序号 ， Excel中明细输入开始的列号,默认第9列
    def __init__(self, current_row: int, execute_serial_number: int, start_col_num: int):
        self.Current_Row = current_row
        self.Execute_Serial_Number = execute_serial_number
        self.Start_Col_Num = start_col_num  # 实际值1，起始列数
        self.Test_Actual_Value_Location = (current_row, self.Start_Col_Num + 2 * execute_serial_number - 2)  # 实际值 坐标
        self.Test_Actual_Result_Location = (current_row, self.Start_Col_Num + 2 * execute_serial_number - 1)  # 测试结果 坐标

        self.Sheet_Name = "测试过程及结果"


if __name__ == '__main__':
    excelSingleTestCoordinate = ResultCoordinate(9, 3)
    logger.info(excelSingleTestCoordinate.Test_Actual_Value_Location)
    logger.info(excelSingleTestCoordinate.Test_Actual_Result_Location)
