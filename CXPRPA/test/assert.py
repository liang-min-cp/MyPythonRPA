import traceback

a = 1
try:
    assert a < 0
except AssertionError as aeeor:  # 明确抛出此异常

    # 抛出 AssertionError 不含任何信息，所以无法通过 aeeor.__str__()获取异常描述

    print('AssertionError', aeeor, aeeor.__str__())

    # 通过 traceback 打印详细异常信息

    print('traceback 打印异常')

    traceback.print_exc()

except:  # 不会命中其他异常

    print('assert except')

try:

    raise AssertionError('测试 raise AssertionError')

except AssertionError as aeeor:

    print('raise AssertionError 异常', aeeor.__str__())

print("end")

print("===================================================================")


# 除法运算

def foo(value, divide):
    assert divide != 0

    return value / divide


print('4除以2 =', foo(4, 2))  # 执行成功

try:
    print('4除以0 =', foo(4, 0))  # 抛出异常
except AssertionError as e:
    print(e)
    # pass

print("End")

print("=======================================")







