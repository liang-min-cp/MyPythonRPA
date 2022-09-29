import os
import sys
import time

sys.path.append("..")


def main(argv):
    # print(type(argv))
    # print(argv.__len__())
    # for arg in argv:
    #     print(arg)
    # times_executes = argv[0]
    argtimes = 5  # 默认5次
    if argv.__len__() > 0:
        argtimes_str = argv[0]
        if argtimes_str.isdigit():
            argtimes = int(argtimes_str)
            print("执行次数： " + str(argtimes))
        else:
            print("输入执行次数无效，将执行默认次数： " + str(argtimes))
    else:
        print("执行默认次数： " + str(argtimes))

    time.sleep(3)
    for i in range(argtimes):
        os.system(R"E:\liangmin_oms\CXPRPA\dist\TC16.exe")
        print("第  " + str(i + 1) + " 次任务  执行完毕")
        if i + 1 == argtimes:
            print("这是最后一次任务")
        else:
            print("即将执行第  " + str(i + 2) + " 次任务")
        time.sleep(3)


if __name__ == "__main__":
    main(sys.argv[1:])
