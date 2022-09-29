import sys

sys.path.append("..")
from excel_tools import SystemConfigCoordinate
from log.logger import logger


class SysConfigModel:

    def __init__(self, fins_trans_way, ip_computer, ip_plc, port, coordinate: SystemConfigCoordinate):
        self.Fins_Trans_Way = fins_trans_way  # fins的传输方式:0-以太网,1-串口,2-USB
        self.Ip_Computer = ip_computer  # 电脑的IP地址
        self.Ip_Plc = ip_plc  # PLC的IP地址
        self.Port = port  # 端口号
        self.Coordinate: SystemConfigCoordinate = coordinate


if __name__ == '__main__':
    sysconfig = SysConfigModel("0-以太网", "192.168.250.5", "192.168.250.1", "5")
    logger.info(sysconfig.Fins_Trans_Way)
    logger.info(sysconfig.Ip_Computer)
    logger.info(sysconfig.Ip_Plc)
    logger.info(sysconfig.Port)
