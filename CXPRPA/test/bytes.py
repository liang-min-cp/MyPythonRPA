import datetime
import string
import sys
import time

sys.path.append("..")
from log.logger import logger

if __name__ == '__main__':
    # cmdsetw200 = bytes.fromhex('80000200010000050055010231000200000101')
    # logger.info(cmdsetw200)
    # a = bytes.fromhex('6162636465')
    # b = a.hex()
    # logger.info(a)
    # logger.info(b)
    # logger.info(hex(255))
    # ret = cmdsetw200.hex()
    # logger.info(ret)

    # a = bytes.fromhex('0101000088')
    # b = a.hex()
    # logger.info(a)
    # logger.info(b)
    # logger.info("   aas   assa  as    ")
    # logger.info("   aas   assa  as    ".strip())
    # str = "111222ffff"
    #
    # a = bytes.fromhex(str)
    # logger.info(a)
    #
    # s = 'af'
    # res = all(c in string.hexdigits for c in s)
    # logger.info(res)

    # a = "255"
    # b = hex(int(a))
    # logger.info(b)
    # c = '%02X' % b
    # logger.info(c)

    def print_bytes_hex(data):
        lin = ['%02X' % i for i in data]
        print(" ".join(lin))


    # ipa1 = '192.168.250.1'
    # b= ipa1.split('.')[ipa1.split('.').__len__()-1]
    # logger.info(b)
    # res = '800002000100000500550101300064000001'
    # header = '80000200010000050055'
    # a = res.split(header)[res.split(header).__len__() - 1]
    # logger.info(a)

    # 测试字节列表，这也是网络传输收到的原始类型
    # arr = [0x4B, 0x43, 0x09, 0xA1, 0x01, 0x02, 0xAB, 0x4A, 0x43]
    # print_bytes_hex(arr)
    # a = "255"
    # b = hex(int(a))
    # c = '%02X' % int(a)
    # logger.info(c)

    msg = "TT/00"
    a1 = msg.encode("utf-8")
    logger.info(a1.__len__())
    b1 = bytes.fromhex("0D")
    a1 = a1 + b1
    logger.info(a1)
