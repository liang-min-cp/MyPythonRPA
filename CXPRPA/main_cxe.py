import datetime
import os
import sys
import openpyxl

sys.path.append("../..")
sys.path.append("..")
from models.cxe_click.CxeClickModel import CxeClickModel
from models.cxe_click.CordinateCxeClick import CordinateCxeClick
from excel_tools.ExcelCommon import GetExcelTemplateFullPath, GetExcelResultFullPath
from log.logger import logger

if __name__ == '__main__':
    # # （1） 打开excel并读取配置参数
    time_begin = datetime.datetime.now()
    logger.info(time_begin)
    excel_template_file_name = "Template_click.xlsx"
    file_path = GetExcelTemplateFullPath(excel_template_file_name)
    logger.info(file_path)
    excel_workbook = openpyxl.load_workbook(file_path)  # 获取表格文件
    logger.info("打开excel 完成")

    # # （2） 读取excel信息
    sheet_name = "测试过程及结果"
    excel_sheet = None
    if excel_workbook.__contains__(sheet_name):
        excel_sheet = excel_workbook[sheet_name]
    else:
        raise Exception("未找到sheet：{}，请检查配置文件。".format(sheet_name))
    logger.info("读取excel信息 完成")

    # # （3） 初始化测试模型
    cordinateCxeClick = CordinateCxeClick()
    cxeClickModel = CxeClickModel(excel_sheet, cordinateCxeClick)
    cxeClickModel.InitModels()
    logger.info("初始化测试模型 完成")

    try:
        # # （4） 注册测试命令
        list_click_cmds = []
        for i in range(cxeClickModel.TestCircleTime):
            for clickCmds in cxeClickModel.ClickCmds:
                list_click_cmds.append(clickCmds.ClickModels[i])
        logger.info("注册测试命令 完成, 命令数目: {}".format(list_click_cmds.__len__()))

        commands_sum = list_click_cmds.__len__()
        # # （5） 执行命令
        iCount = 0
        for click_cmd in list_click_cmds:
            logger.info("当前执行序号：{}， 总数：{}".format(iCount+1, commands_sum))
            click_cmd.Run()
            iCount = iCount + 1

        # # （6） 测试结果写入excel
        cxeClickModel.InitTableHeader()
        cxeClickModel.WriteCmdTestResultToExcel()
        logger.info("结果写入Excel 完成")

        # # （7） 测试完毕，保存excel
        file_path_output = GetExcelResultFullPath()
        if os.path.isfile(file_path_output):
            os.remove(file_path_output)
        logger.info(file_path_output)
        excel_workbook.save(file_path_output)
        excel_workbook.close()
        logger.info("测试完毕，保存excel")
    except Exception as e:
        logger.info(e.__str__())
        excel_workbook.close()

    os.system("pause")
