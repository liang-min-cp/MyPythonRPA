import datetime
import os
import sys
import time

sys.path.append("..")
from models.RegisterExecutions import RegisterExecutions

from cxp.CxpClose import CxpClose
from cxp.CxpStart import CxpStart

from excel_tools.ExcelWrite import ExcelWrite
from excel_tools.ExcelRead import ExcelRead
import openpyxl
from excel_tools.ExcelCommon import GetExcelTemplateFullPath, GetExcelResultFullPath
from log.logger import logger

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

    # # （3） 注册测试命令
    logger.info("注册测试命令")
    registerExecutions = RegisterExecutions(processAndResul, systemConfigInfo)
    registerExecutions.RegisterCommands()
    listCmd = registerExecutions.listCmd
    logger.info("注册命令执行总次数： " + str(listCmd.__len__()))

    # （4） 进行测试
    logger.info("测试- 开始")
    for cmd in listCmd:
        cmd.Run()
    logger.info("测试- 完成")

    excel_workbook.close()
    # # （5） 汇总测试结果
    logger.info("汇总测试结果 - 开始")
    # （5.1） 汇总测试命令结果
    for command in processAndResul.Commands:
        test_res = "OK"
        for res in command.Test_Results:
            if res.Test_Actual_Result == "NG":
                test_res = res.Test_Actual_Result
                break
        command.Test_Result = test_res

    # （5.1） 汇总测试命令条数，总条数，成功条数，失败条数
    nums_total = processAndResul.Commands.__len__()
    nums_OK = 0
    nums_NG = 0
    for command in processAndResul.Commands:
        if command.Test_Result == "OK":
            nums_OK += 1
        elif command.Test_Result == "NG":
            nums_NG += 1
        else:
            logger.info("有异常结果")
            logger.info(command.__dict__)
    processAndResul.TestCommandAllNum = nums_total
    processAndResul.TestCommandSuccessNum = nums_OK
    processAndResul.TestCommandFailedNum = nums_NG
    # 汇总本次测量总结果
    processAndResul.TestResultSummary = "OK" if nums_NG == 0 else "NG"

    # （5.2） 汇总测试时间，总耗时，命令平均耗时
    time_finished = datetime.datetime.now()
    logger.info(time_finished)
    processAndResul.ProgramStartTime = time_begin
    processAndResul.ProgramFinishedTime = time_finished
    time_span = time_finished - time_begin
    total_seconds = time_span.total_seconds()
    minute_amount, seconds_amount = divmod(total_seconds, 60)
    time_amount = "%.2f 秒" % total_seconds
    if total_seconds > 60:
        time_amount = "%02d 分 %.2f 秒" % (minute_amount, seconds_amount)
    processAndResul.TestTimeALl = time_amount
    # processAndResul.TestTimeALl = str(total_seconds.__format__(".2f")) + " 秒"  # 测试命令总耗时

    single_seconds_all = total_seconds / nums_total
    minute_single, seconds_single = divmod(single_seconds_all, 60)
    time_single = "%.2f 秒" % single_seconds_all
    if single_seconds_all > 60:
        time_single = "%02d 分 %.2f 秒" % (minute_single, seconds_single)
    processAndResul.TestTimeAverage = time_single
    # processAndResul.TestTimeAverage = str((total_seconds / nums_total).__format__(".2f")) + " 秒"  # 测试命令平均耗时
    logger.info("汇总测试结果 - 完成")

    # # （6） 测试结果写入excel
    excelWrite = ExcelWrite(excel_workbook, processAndResul)
    excelWrite.WriteProcessAndResultInfoToExcel()
    logger.info("测试结果写入excel Finished")

    # # （7） 测试完毕，保存excel
    file_path_output = GetExcelResultFullPath()
    if os.path.isfile(file_path_output):
        os.remove(file_path_output)
    logger.info(file_path_output)
    excel_workbook.save(file_path_output)
    excel_workbook.close()
    logger.info("测试完毕，保存excel  Finished")
    # os.system("pause")
    #################################################################
    # logger.info("Begin Start CXP")
    # cxpStart = CxpStart(R"E:\liangmin_oms\TC16\Input Process Data Invalid Error.cxp")
    # cxpClose = CxpClose()
    # listExecutionCommands = [cxpStart, cxpClose]
    # for listExecutionCommand in listExecutionCommands:
    #     if type(listExecutionCommand) is CxpClose:
    #         listExecutionCommand.PopenObj = listExecutionCommands[0].PopenObj
    #         logger.info("CxpClose PopenObj is Ready")
    #     listExecutionCommand.Run()
    #     time.sleep(5)
    #     logger.info("Finished: " + str(listExecutionCommand.__class__))
    #
    # logger.info('Finised All')
