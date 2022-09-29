import time
import sys
from socket import *
from time import *
sys.path.append("..")
from log.logger import logger

class PortEth:
    """
    ethernet driver，当前主要使用UDP发送Fins命令
    """

    def __init__(self, src_ip: str, dst_ip: str, port: int):
        """
        ethernet初始化，设置本机IP，远端IP及端口号
        :param src_ip: 本机IP地址
        :param dst_ip: 远端IP地址
        :param port: 端口号
        """
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.port = port
        self.s = None

    def _open_udp(self):
        """打开端口
        """

        try:
            if self.s:
                self.close()
            self.s = socket(AF_INET, SOCK_DGRAM)
        except Exception as e:
            print(e)

    def close(self):
        """
        关闭端口
        :return:
        :return:
        """

        if self.s:
            try:
                self.s.close()
            except Exception as e:
                print(e)
            self.s = None
            print("套接字已关闭")

    def _udp_send(self, data: bytes):
        """
        :param data: 要传输的数据
        :return:
        """
        try:
            self.s.sendto(data, (self.dst_ip, self.port))
        except Exception as e:
            print(e)

    def _udp_rcv(self, nbytes: int = 1024, timeout: float = 0.5):
        try:
            self.s.settimeout(timeout)
            response = self.s.recv(nbytes)
        except Exception as e:
            print(e)
            response = bytes()

        return response

    def send_cmd_wait_rsp(self, cmd: bytes, rsp: bytes = bytes(), rsp_len: int = 1024, timeout: float = 0.5):
        """
        发送命令，并在指定的时间内等待响应
        :param cmd: 要发送的数据
        :param rsp: 期待接收到的数据
        :param rsp_len: 如果rsp为空，则由此处指定等待的字节数
        :param timeout: 超时时间，单位秒
        :return: （成功/失败， 接收的数据）
        """
        result = (False, bytes())
        if not self.s:
            self._open_udp()

        self._udp_send(cmd)
        if rsp:
            rcv = self._udp_rcv(len(rsp))
            result = rcv == rsp, rcv
        else:
            rcv = self._udp_rcv(rsp_len, timeout)
            result = len(rcv) == rsp_len, rcv

        return result


if __name__ == '__main__':
    # 0402FFFF 进入program模式
    PCport = PortEth('192.168.250.222', '192.168.250.1', 9600)
    cmd = bytes.fromhex('800002000100000500550402FFFF')

    rsp = bytes.fromhex('c000020005000001005504020000')
    result = PCport.send_cmd_wait_rsp(cmd=cmd, rsp=rsp)
    logger.info(result)
    logger.info(result[1].hex())

    sleep(1000)

    '''
    读取cio100.00,判断response是否为0
    '''
    cmd = bytes.fromhex('800002000100000500550101300064000001')
    rsp = bytes.fromhex('c00002000500000100550101000000')
    rsp0201equal1 = bytes.fromhex('c00002000500000100550101000001')

    cmdtoPrgMode = bytes.fromhex('800002000100000500550402FFFF')
    rsptoPrgMode = bytes.fromhex('c000020005000001005504020000')

    cmdtoRunMode = bytes.fromhex('800002000100000500550401FFFF04')
    rsptoRunMode = bytes.fromhex('c000020005000001005504010000')

    '''
    cmdclear0442 = bytes.fromhex('8000020001000005005521010442')
    rspclear0442 = bytes.fromhex('c000020005000001005521010000')
    '''

    cmdclearall = bytes.fromhex('800002000100000500552101FFFF')
    rspclearall = bytes.fromhex('c000020005000001005521010000')

    '''
    循环发送0201，检查是否为0：
        1.如果此时为0，则等待1s后继续发送
        2.如果此时为1，则发送
    '''
    cmdsetw200 = bytes.fromhex('80000200010000050055010231000200000101')
    rspsetw200 = bytes.fromhex('c000020005000001005501020000')
    cmdreadw200 = bytes.fromhex('800002000100000500550101310002000001')
    rspreadw200 = bytes.fromhex('c00002000500000100550101000001')

    result = PCport.send_cmd_wait_rsp(cmd=cmdsetw200, rsp=rspsetw200)
    '''CIO100.00 为0'''
    if (result[0] == True):
        print('set w200 check {0}'.format(result))

    result = PCport.send_cmd_wait_rsp(cmd=cmdreadw200, rsp=rspreadw200)
    '''CIO100.00 为0'''
    if (result[0] == True):
        print('read w200 check {0}'.format(result))

    while True:
        result = PCport.send_cmd_wait_rsp(cmd=cmd, rsp=rsp)
        '''CIO100.00 为0'''
        if (result[0] == True):
            print('CIO100.00 ==0 check {0}'.format(result))

        else:
            if result[1] == rsp0201equal1:
                print('CIO100.00 ==1 check {0}'.format(result))
                """
                进入升级模式
                """
                resulttoPrg = PCport.send_cmd_wait_rsp(cmd=cmdtoPrgMode, rsp=rsptoPrgMode)
                if resulttoPrg[0] == True:
                    print('in program mode:')
                    """
                    清除所有错误
                    """
                    resultclearall = PCport.send_cmd_wait_rsp(cmd=cmdclearall, rsp=rspclearall)
                    if (resultclearall[0] == True):
                        print('cleared all error')
                        """
                        进入run模式
                        """
                        resulttoRun = PCport.send_cmd_wait_rsp(cmd=cmdtoRunMode, rsp=rsptoRunMode)
                        if (resulttoRun[0] == True):
                            print('in run mode:\n')

                """
                进入升级模式并清除错误，等待15s
                """
                sleep(15)

        sleep(1)
