import os
import sys
import time
import socket

import openpyxl
from ping3 import ping

sys.path.append("..")

from models.plc_reset.PlcConfigModel import PlcConfigInfo

from excel_tools.ExcelCommon import GetExcelConfigFullPath
from fins.FinsBase import FinsBase
from models.SysConfig import SysConfigModel
from log.logger import logger
from models import ProcessAndResult
import uiautomation as auto
from exceptions.ConnectError import ConnectError


if __name__ == "__main__":
    try:
        config_excel_path = GetExcelConfigFullPath("excel_config", "Config.xlsx")
        logger.info(config_excel_path)
        excel_workbook = openpyxl.load_workbook(config_excel_path)  # 获取表格文件
        plcConfigInfo = PlcConfigInfo(
            ip_pc_rx65="",
            ip_pc_am3352="",
            ip_plc_rx65="",
            port_plc_rx65=0,
            ip_plc_am3352="192.168.250.100",
            ip_plc_am3352_check_mode="192.168.250.200",
            port_plc_am3352_check_mode=4096
        )
        plcConfigInfo.GetConfigFromExcel(excel_workbook, "系统设置")
        logger.info(plcConfigInfo.__dict__)
        excel_workbook.close()
        logger.info("读取配置信息 - 完成")

        rx65_ip_is_ok = plcConfigInfo.CheckIP_rx65()
        if not rx65_ip_is_ok:
            logger.info(rx65_ip_is_ok)
            logger.info("IP异常，（1）请检查IP设置及网线连接，（2）重新上电主站，（3）重新执行该软件")
            raise Exception("IP异常，（1）请检查IP设置及网线连接，（2）重新上电主站，（3）重新执行该软件")

        finsBase = FinsBase(plcConfigInfo.Ip_pc_rx65,
                            plcConfigInfo.Ip_plc_rx65,
                            int(plcConfigInfo.Port_plc_rx65))
        res = finsBase.ExecuteFinsAndGetResult("0402FFFF")
        if res != "":
            # logger.info("RX65设置为编程模式, {} - 完成".format(res))
            logger.info("RX65设置为编程模式 - 完成")
        else:
            logger.info("设置为编程模式异常:（1）重新上电主站，（2）重新执行该软件")
            raise Exception("设置为编程模式异常:（1）重新上电主站，（2）重新执行该软件")
        time.sleep(2)
        res_diagnosis = finsBase.ExecuteFinsAndGetResult("2124000000000000")
        logger.info(res_diagnosis)
        logger.info("RX65进入检查机模式 - 完成")
        time.sleep(2)

        am3352_check_mode_ip_is_ok = plcConfigInfo.CheckIP_am3352_check_mode()
        if not am3352_check_mode_ip_is_ok:
            logger.info(am3352_check_mode_ip_is_ok)
            logger.info("IP异常，（1）请检查IP设置及网线连接，（2）重新上电主站，（3）重新执行该软件")
            raise Exception("IP异常，（1）请检查IP设置及网线连接，（2）重新上电主站，（3）重新执行该软件")

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(300)
        client.connect((plcConfigInfo.Ip_plc_am3352_check_mode, plcConfigInfo.Port_plc_am3352_check_mode))
        send_msg = "TT/00"  # 返回： b'OK/00\r'
        client.send(send_msg.encode("utf-8") + bytes.fromhex("0D"))
        msg = client.recv(1024)
        logger.info(msg)
        mes_decode = msg.decode("utf-8")
        logger.info(mes_decode)
        if mes_decode.startswith("OK"):
            logger.info("检检查机模式OK")
        else:
            logger.info("检检查机模式异常：（1）重新上电主站，（2）重新执行该软件")
            client.close()
            raise Exception("检检查机模式异常：（1）重新上电主站，（2）重新执行该软件")

        client.send("TT/24_41".encode("utf-8") + bytes.fromhex("0D")) # 返回 OK/24_41
        logger.info("等待返回中，请勿断开连接, 请耐心等待（3分钟左右）...")
        msg01 = client.recv(1024)
        client.settimeout(300)
        logger.info("接收：" + msg01.decode("utf-8"))
        if msg01.decode("utf-8").startswith("OK/24_41"):
            logger.info("检检查机写入OK")
        else:
            logger.info("检检查机写入异常：（1）重新上电主站，（2）重新执行该软件")
            client.close()
            raise Exception("检检查机写入异常：（1）重新上电主站，（2）重新执行该软件")

        # 确认状态
        send_msg_check = "TT/92_01_00000000" # 返回 OK/92_00_FFFFFFFF
        client.send(send_msg_check.encode("utf-8") + bytes.fromhex("0D"))
        msg_check = client.recv(1024)
        logger.info(msg_check.decode("utf-8"))
        if msg_check.decode("utf-8").startswith("OK/92_00_FFFFFFFF"):
            logger.info("确认写入OK")
        else:
            logger.info("确认写入异常：（1）重新上电主站，（2）重新执行该软件")
            client.close()
            raise Exception("确认写入异常：（1）重新上电主站，（2）重新执行该软件")

        client.close()
        logger.info("程序执行完毕，请断电重启主站。")
        os.system("pause")
    except Exception as e:
        logger.info(e.__str__())
        os.system("pause")


















