import sys

sys.path.append("..")
from log.logger import logger


class SystemConfigCoordinate:

    def __init__(self):
        self.SheetName = R"系统设置"
        self.Fins_Trans_Way_Location = (2, 3)  # fins的传输方式,坐标
        self.Ip_Computer_Location = (4, 3)  # 电脑的IP地址,坐标
        self.Ip_Plc_Location = (5, 3)   # PLC的IP地址,坐标
        self.Port_Location = (7, 3)   # 端口号,坐标

        self.Sheet_Name = "系统设置"


if __name__ == '__main__':
    excelSystemConfigCoordinate = SystemConfigCoordinate()
    logger.info(excelSystemConfigCoordinate.SheetName)
    logger.info(excelSystemConfigCoordinate.Fins_Trans_Way_Location)
    logger.info(excelSystemConfigCoordinate.Ip_Computer_Location)
    logger.info(excelSystemConfigCoordinate.Ip_Plc_Location)
    logger.info(excelSystemConfigCoordinate.Port_Location)
