import sys
import time

sys.path.append("..")
from log.logger import logger
from fins.PortEth import PortEth
from models import ProcessAndResult, ProcessCommand
from models.SysConfig import SysConfigModel


class FinsBase:
    def __init__(self, ip_sender: str, ip_recv: str, port: int):
        self.PortEth = PortEth(ip_sender, ip_recv, port)
        self.Ip_Sender = ip_sender.strip()
        self.Ip_Recv = ip_recv.strip()
        self.Port = port
        self.Host_Sender = self.Ip_Sender.split('.')[self.Ip_Sender.split('.').__len__() - 1]
        self.Host_Recv = self.Ip_Recv.split('.')[self.Ip_Recv.split('.').__len__() - 1]
        self.Fins_Header_Sender = "80000200" + '%02X' % int(self.Host_Recv) + "0000" + '%02X' % int(self.Host_Sender) + "0055"
        self.Fins_Header_Recv = 'c0000200' + '%02X' % int(self.Host_Sender) + '0000' + '%02X' % int(self.Host_Recv) + '0055'

    # Fins无响应,则返回空,Fins返回值头与系统预设值不一致,返回带有Fins头的结果
    def ExecuteFinsAndGetResult(self, cmd: str):
        # logger.info("Fins 发送头: " + self.Fins_Header_Sender)
        # logger.info("Fins 接收头: " + self.Fins_Header_Recv)
        # logger.info("Fins命令: " + cmd.strip())
        cmd_request_with_header = self.Fins_Header_Sender + cmd.strip()
        # logger.info("Fins命令(加发送头): " + cmd_request_with_header.strip())
        cmd_request_with_header_bytes = bytes.fromhex(cmd_request_with_header)
        cmd_response = self.PortEth.send_cmd_wait_rsp(cmd=cmd_request_with_header_bytes)
        if cmd_response.__len__() == 2 and bool(cmd_response[1].strip()):
            cmd_response_with_header_bytes = cmd_response[1].strip()
            cmd_response_with_header = cmd_response_with_header_bytes.hex()
            if cmd_response_with_header.startswith(self.Fins_Header_Recv):
                cmd_response_without_header = cmd_response_with_header.split(self.Fins_Header_Recv)[
                    cmd_response_with_header.split(self.Fins_Header_Recv).__len__() - 1]
                return cmd_response_without_header
            else:
                logger.info("接收到的返回值, Fins头与系统预设值不一致")
                logger.info(cmd_response_with_header)
                return cmd_response_with_header
        else:
            return ""


if __name__ == '__main__':
    logger.info("main")
