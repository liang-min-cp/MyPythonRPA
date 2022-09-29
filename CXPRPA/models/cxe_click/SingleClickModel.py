import datetime
import sys
import time

import pythoncom
import uiautomation as auto
from openpyxl.worksheet.worksheet import Worksheet

sys.path.append("..")
from excel_tools.ExcelCommon import SetBodyCellStyle
from models.cxe_click.CordinateCxeClick import CordinateCxeClick
from log.logger import logger


class SingleClickModel:

    def __init__(self, work_sheet: Worksheet, cordinate_cxe_click: CordinateCxeClick,
                 test_name: str, execute_cmd_seq: int, execute_circle_seq: int):
        self.WorkSheet = work_sheet  # Excel工作页
        self.TestName = test_name  # 点击的测试名称（Init/Pre-Op/Safe-Op/Op）
        self.Cordinate_Excel = cordinate_cxe_click  # Excel配置坐标
        self.ExecuteCmdSeq = execute_cmd_seq  # 执行的命令序号（表示执行的第几个命令）
        self.ExecuteCircleSeq = execute_circle_seq  # 表示该命令每次执行循环第几次，从1开始

        self.RealValuePointCol = (self.ExecuteCircleSeq * 2) - 2 + \
                                 self.Cordinate_Excel.Test_Process_Detail_Start_Col  # 实际值，单元格纵坐标
        self.TestResultPointCol = (self.ExecuteCircleSeq * 2) - 1 + \
                                  self.Cordinate_Excel.Test_Process_Detail_Start_Col  # 测试结果，单元格纵坐标
        self.CurrentRow = self.Cordinate_Excel.Test_Process_Header_Row + self.ExecuteCmdSeq  # 当前行左边
        self.RealValue = None
        self.TestResult = None

    # def __init__(self, test_name: str):
    #     self.TestName = test_name  # 点击的测试名称（Init/Pre-Op/Safe-Op/Op）
    #     self.RealValue = None
    #     self.TestResult = None

    def WriteCurrentTestResultToExcel(self):
        # 写入实际值
        real_value_cell = self.WorkSheet.cell(self.CurrentRow, self.RealValuePointCol)
        real_value_cell.value = self.RealValue
        SetBodyCellStyle(real_value_cell)

        # 写入测试结果
        test_result_cell = self.WorkSheet.cell(self.CurrentRow, self.TestResultPointCol)
        test_result_cell.value = self.TestResult
        SetBodyCellStyle(test_result_cell)

    def Run(self):
        try:
            logger.info("开始执行:{}".format(self.TestName))

            # main_window = auto.WindowControl(Name=R"CX-EtherCAT")
            main_window = auto.WindowControl(Name="CX-EtherCAT") # CXE安装程序窗口
            # main_window = auto.WindowControl(AutomationId='mainWindow') # VS运行EC-Engineer窗口
            if main_window.Exists():
                # main_window.SendKeys('{Ctrl}O', waitTime=0.1)
                logger.info("定位CX-EtherCAT，ClassName：{}".format(main_window.ClassName))
                time.sleep(0.5)
            else:
                raise Exception("Not Found CX-EtherCAT")

            if self.TestName.lower() == "init":
                logger.info("")
                btn_control_init = main_window.ButtonControl(Name="Init")
                if not btn_control_init.Exists():
                    raise Exception("btn_control_init not found")
                btn_control_init.Click()
                time.sleep(1)
                edit_control_current_state = main_window.EditControl(ClassName="XamTextEditor", SearchIndex=1)
                if not edit_control_current_state.Exists():
                    raise Exception("edit_control_current_state not found")
                logger.info("Process Id: {}".format(edit_control_current_state.ProcessId))
                current_state_value = edit_control_current_state.GetLegacyIAccessiblePattern().Value
                logger.info(current_state_value)
                self.RealValue = current_state_value
                if self.RealValue.lower() == "初始化" or self.RealValue.lower() == "init":
                    self.TestResult = "OK"
                else:
                    self.TestResult = "NG"
                logger.info(self.TestResult)
            elif self.TestName.lower() == "pre-op":
                logger.info("")
                btn_control_pre_op = main_window.ButtonControl(Name="Pre-Op")
                if not btn_control_pre_op.Exists():
                    raise Exception("btn_control_pre-op not found")
                btn_control_pre_op.Click()
                time.sleep(1)
                edit_control_current_state = main_window.EditControl(ClassName="XamTextEditor", SearchIndex=1)
                if not edit_control_current_state.Exists():
                    raise Exception("edit_control_current_state not found")
                logger.info("Process Id: {}".format(edit_control_current_state.ProcessId))
                current_state_value = edit_control_current_state.GetLegacyIAccessiblePattern().Value
                logger.info(current_state_value)
                self.RealValue = current_state_value
                if self.RealValue.lower() == "pre-op":
                    self.TestResult = "OK"
                else:
                    self.TestResult = "NG"
                logger.info(self.TestResult)
            elif self.TestName.lower() == "safe-op":
                logger.info("")
                btn_control_safe_op = main_window.ButtonControl(Name="Safe-Op")
                if not btn_control_safe_op.Exists():
                    raise Exception("btn_control_safe-op not found")
                btn_control_safe_op.Click()
                time.sleep(1)
                edit_control_current_state = main_window.EditControl(ClassName="XamTextEditor", SearchIndex=1)
                if not edit_control_current_state.Exists():
                    raise Exception("edit_control_current_state not found")
                logger.info("Process Id: {}".format(edit_control_current_state.ProcessId))
                current_state_value = edit_control_current_state.GetLegacyIAccessiblePattern().Value
                logger.info(current_state_value)
                self.RealValue = current_state_value
                if self.RealValue.lower() == "safe-op":
                    self.TestResult = "OK"
                else:
                    self.TestResult = "NG"
                logger.info(self.TestResult)
            elif self.TestName.lower() == "op":
                logger.info("")
                btn_control_op = main_window.ButtonControl(Name="OP") #CXE元素定位
                # btn_control_op = main_window.ButtonControl(Name="Op")  # EC-Engineer元素定位
                if not btn_control_op.Exists():
                    raise Exception("btn_control_op not found")
                btn_control_op.Click()
                time.sleep(1)
                edit_control_current_state = main_window.EditControl(ClassName="XamTextEditor", SearchIndex=1)
                if not edit_control_current_state.Exists():
                    raise Exception("edit_control_current_state not found")
                logger.info("Process Id: {}".format(edit_control_current_state.ProcessId))
                current_state_value = edit_control_current_state.GetLegacyIAccessiblePattern().Value
                logger.info(current_state_value)
                self.RealValue = current_state_value
                if self.RealValue.lower() == "op":
                    self.TestResult = "OK"
                else:
                    self.TestResult = "NG"
                logger.info(self.TestResult)
            else:
                raise Exception("异常命令：{}，请检查配置文件。".format(self.TestName))

        except LookupError as e:
            logger.exception(e)
            self.RealValue = "None"
            self.TestResult = "NG"
            pass

        time.sleep(0.5)


if __name__ == '__main__':
    logger.info("main")
    # pythoncom.CoInitialize()
    #
    # main_window = auto.WindowControl(Name="CX-EtherCAT")
    #
    # if not main_window.Exists():
    #     raise Exception("未找到：CX-EtherCAT")
    # btn_control_safe_op = main_window.ButtonControl(Name="Safe-Op")
    # if not btn_control_safe_op.Exists():
    #     raise Exception("btn_control_init not found")
    # btn_control_safe_op.Click()
    # edit_control_current_state = main_window.EditControl(ClassName="XamTextEditor", SearchIndex=1)
    # if not edit_control_current_state.Exists():
    #     raise Exception("edit_control_current_state not found")
    # logger.info(edit_control_current_state.ProcessId)
    # current_state_value = edit_control_current_state.GetLegacyIAccessiblePattern().Value
    # logger.info(current_state_value)
    # RealValue = current_state_value
    # if RealValue.lower() == "safe-op":
    #     TestResult = "OK"
    # else:
    #     TestResult = "NG"
    # logger.info(TestResult)
