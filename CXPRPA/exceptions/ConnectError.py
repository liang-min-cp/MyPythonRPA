class ConnectError(Exception):
    '''当输出有误时，抛出此异常'''

    # 自定义异常类型的初始化
    def __init__(self, value):
        self.value = value

    # 返回异常类对象的说明信息
    def __str__(self):
        return "ConnectError:{}".format(repr(self.value))


if __name__ == "__main__":
    try:
        raise ConnectError("确认连接到下位机状态失败！")
        # raise ConnectError(1)  # 抛出 MyInputError 这个异常

    except ConnectError as err:
        print('error: {}'.format(err))
        print(err)

