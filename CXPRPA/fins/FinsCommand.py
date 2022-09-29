import datetime
import string
import sys
import time
import re

sys.path.append("..")
import openpyxl

from excel_tools.ExcelCommon import GetExcelTemplateFullPath
from excel_tools.ExcelRead import ExcelRead

from log.logger import logger
from fins.PortEth import PortEth
from models import ProcessAndResult, ProcessCommand
from models.SysConfig import SysConfigModel


class FinsCommand:
    def __init__(self, sys_config_model: SysConfigModel, process_and_result: ProcessAndResult,
                 command_seq: int,
                 command_execute_seq: int):
        self.processAndResult = process_and_result
        self.sysConfigModel = sys_config_model
        self.PCport = PortEth(sys_config_model.Ip_Computer.strip(), sys_config_model.Ip_Plc.strip(),
                              int(sys_config_model.Port))
        self.CommandSeq = command_seq
        self.CommandExecuteSeq = command_execute_seq
        self.TestActualValue = None  # 实际值
        self.TestActualResult = None  # 测试结果
        self.Command: ProcessCommand = None

    # 获取fins头,发送头和接收头
    def GetFinsHeader(self):
        # c = '%02X' % int(a)
        ip_pc = self.sysConfigModel.Ip_Computer.strip()
        ip_plc = self.sysConfigModel.Ip_Plc.strip()
        ip_pc_host = ip_pc.split('.')[ip_pc.split('.').__len__() - 1]
        ip_plc_host = ip_plc.split('.')[ip_plc.split('.').__len__() - 1]
        # logger.info(ip_pc_host)
        # logger.info(ip_plc_host)
        # 发送: 80000200010000050055
        ICF = '80'
        RSV = '00'
        GCT = '02'
        DNA = '00'
        # DA1 = '01' # 下位机 PLC IP
        DA1 = '%02X' % int(ip_plc_host)
        DA2 = '00'
        SNA = '00'
        # SA1 = '05' # 上位机 主机 IP
        SA1 = '%02X' % int(ip_pc_host)
        SA2 = '00'
        SID = '55'
        fins_header_send = ICF + RSV + GCT + DNA + DA1 + DA2 + SNA + SA1 + SA2 + SID
        # logger.info("fins 发送头: " + fins_header_send)

        # 接收: c0000200 05 0000 01 0055
        fins_header_recv = 'c0000200' + SA1 + '0000' + DA1 + '0055'
        # logger.info("fins 接收头: " + fins_header_recv)
        return fins_header_send, fins_header_recv

    # 运行
    def Run(self):
        for command in self.processAndResult.Commands:
            if command.Command_Seq_Num == self.CommandSeq:
                self.Command = command
                b_res = False
                logger.info(self.Command.__dict__)
                cmd_request = command.Command_Name.strip()  # 操作命令/名称
                # 处理加Fins发送头
                fins_header_send, fins_header_recv = self.GetFinsHeader()

                cmd_response_expect = command.Expect_Value.strip()  # 期待值
                cmd_response_expect_list = cmd_response_expect.strip().split('/')  # 期待值列表
                # logger.info(cmd_response_expect_list)
                cmd_request_with_header_bytes = bytes.fromhex(fins_header_send + cmd_request)

                cmd_response = self.PCport.send_cmd_wait_rsp(cmd=cmd_request_with_header_bytes)
                if cmd_response.__len__() == 2 and bool(cmd_response[1].strip()):
                    cmd_response_with_header_bytes = cmd_response[1].strip()
                    cmd_response_with_header = cmd_response_with_header_bytes.hex()
                    if cmd_response_with_header.startswith(fins_header_recv):
                        cmd_response_without_header = cmd_response_with_header.split(fins_header_recv)[
                            cmd_response_with_header.split(fins_header_recv).__len__() - 1]
                        self.TestActualValue = cmd_response_without_header
                        #  验证测量结果, 判断是否全为16进制字符，是:则用=匹配，否：用正则匹配
                        for response_expect in cmd_response_expect_list:
                            is_all_hex_in_expect = all(c in string.hexdigits for c in response_expect)
                            if is_all_hex_in_expect:
                                # 完全匹配
                                if response_expect == cmd_response_without_header:
                                    b_res = True
                                    break
                            else:
                                # 正则匹配
                                response_expect = re.fullmatch(str(response_expect), cmd_response_without_header)
                                if response_expect:
                                    b_res = True
                                    break
                    else:
                        # 返回结果头异常
                        self.TestActualValue = cmd_response_with_header
                else:
                    self.TestActualValue = "Time out"
                self.TestActualResult = "OK" if b_res else "NG"
                logger.info("测试过程循环总次数:【" + str(self.processAndResult.Test_Circulate_Number) + "】,当前次数:【" + str(self.CommandExecuteSeq)+"】")
                logger.info("命令： " + command.Command_Name)
                logger.info("期待值： " + command.Expect_Value)
                logger.info("实际值： " + self.TestActualValue)
                logger.info("测量结果： " + self.TestActualResult)
                time.sleep(2)
                break
        #  更新测量结果
        for test_res in self.Command.Test_Results:
            if test_res.Command_Test_Serial_Num == self.CommandExecuteSeq:
                test_res.Test_Actual_Value = self.TestActualValue  # 实际值
                test_res.Test_Actual_Result = self.TestActualResult  # 测试结果
                break

        logger.info("Current FinsCommand Run Finished")

    def SetResult(self, test_result):
        # 写入测量结果
        logger.info("写入测量结果")

    def RunEx(self):
        logger.info("本机IP ： " + self.sysConfigModel.Ip_Computer)
        logger.info("PLC-IP ： " + self.sysConfigModel.Ip_Plc)
        logger.info("端口号 ： " + str(self.sysConfigModel.Port))
        cmdsetw200 = bytes.fromhex('80000200010000050055010231000200000101')
        rspsetw200 = bytes.fromhex('c000020005000001005501020000')
        # PCport = PortEth('192.168.250.5', '192.168.250.1', 9600)
        # PCport = PortEth(self.sysConfigModel.Ip_Computer.strip(),
        #                  self.sysConfigModel.Ip_Plc.strip(),
        #                  int(self.sysConfigModel.Port))
        result = self.PCport.send_cmd_wait_rsp(cmd=cmdsetw200, rsp=rspsetw200)
        logger.info(result)
        time.sleep(1)
        req = "0101300064000001"
        res = self.PCport.send_cmd_wait_rsp(cmd=bytes.fromhex(req))
        logger.info(res)

        # result = self.PCport.send_cmd_wait_rsp(cmd=cmdsetw200)
        # logger.info(result)
        # # 先判断结果是不是相等，如果不相等，再判断符不符合正则，
        # if bool(result[1].strip()):
        #     res_val = result[1].strip().hex()
        #     logger.info(res_val)


if __name__ == '__main__':
    # # （1） 打开excel
    time_begin = datetime.datetime.now()
    logger.info(time_begin)
    excel_template_file_name = "TCsetting_Template.xlsx"
    file_path = GetExcelTemplateFullPath(excel_template_file_name)
    logger.info(file_path)
    excel_workbook = openpyxl.load_workbook(file_path)  # 获取表格文件
    logger.info("打开excel 完成")

    # # （2） 读取excel信息
    excelRead = ExcelRead(excel_workbook)
    systemConfigInfo = excelRead.ReadSystemConfigInfo()  # 系统设置
    processAndResul = excelRead.ReadProcessAndResultInfo()  # 测试过程及结果
    logger.info("读取excel信息 完成")
    # 关闭excel
    excel_workbook.close()
    logger.info("======================================================================")
    finsCommand = FinsCommand(systemConfigInfo, processAndResul, 1, 1)
    finsCommand.RunEx()
