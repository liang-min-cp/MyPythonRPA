import datetime
import sys

from openpyxl.worksheet.worksheet import Worksheet
sys.path.append("..")
sys.path.append("../..")
from excel_tools.ExcelCommon import SetBodyCellStyle


from models.cxe_click import SingleClickModel, CordinateCxeClick

from models import ProcessCommand
from excel_tools import SummaryCoordinate
from log.logger import logger


class ClickCommandModel:

    def __init__(self, work_sheet: Worksheet, cordinate_cxe_click: CordinateCxeClick,
                 test_name: str, execute_cmd_seq: int):
        self.WorkSheet = work_sheet  # Excel工作页
        self.TestName = test_name  # 点击的测试名称（Init/Pre-Op/Safe-Op/Op）
        self.Cordinate_Excel = cordinate_cxe_click  # Excel配置坐标
        self.ExecuteCmdSeq = execute_cmd_seq  # 执行的命令序号（表示执行的第几个命令,从1开始）

        self.CurrentRow = self.Cordinate_Excel.Test_Process_Header_Row + self.ExecuteCmdSeq  # 当前行左边
        self.CurrentCmdTestResultCol = self.Cordinate_Excel.Test_Process_Result_Col  # 该命令，测试结果，所在列号
        self.ClickModels: list[SingleClickModel] = []  # 当前点击命令，所有循环次数集合
        self.CmdTestResult = None

    # 改行测试结果命令，写入excel
    def WriteCmdTestResultToExcel(self):
        result = "OK"
        for each_test in self.ClickModels:
            if each_test.TestResult == "NG":
                result = "NG"
                break
        # 写入测试结果
        self.CmdTestResult = result
        cmd_test_result_cell = self.WorkSheet.cell(self.CurrentRow, self.CurrentCmdTestResultCol)
        cmd_test_result_cell.value = result
        SetBodyCellStyle(cmd_test_result_cell)


if __name__ == '__main__':
    logger.info("main")

















