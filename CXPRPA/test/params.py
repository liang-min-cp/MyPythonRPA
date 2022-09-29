import sys

sys.path.append("..")


# from log.logger import logger


# 若不定参位于位置参数之后则传入的参数会按顺序先传入位置参数再将剩下的所有传入不定参，不会抛出仅接受关键字参数的异常。
def test(a, *params_a):
    print(a)
    print(*params_a)
    print(params_a)
    for each in params_a:
        print(each)
    return params_a


a = test(1, 2, 3, 4, 5, 6)
print(type(a))
print("========================================")


# 若使用的不定参为* * params的形式则仅接受关键字传参，以位置参数的形式传入则会抛出异常（毕竟收集到的参数是存放在字典中，一定要有k才能有v），
# 且传入的关键字参数不可重复（即不可自身重复，也不可与已有的形参名重复） 重复则抛出异常。
def test(a, **params_a):
    print(a)
    print(*params_a)
    print(params_a)
    for each in params_a:
        print(each)
    return params_a


a = test(1, aa=2, b=3, c=4, d=5, e=6)
print(type(a))

print("========================================")


# 若不定参位于非不定参的前面，则后面的参数一定要使用关键字参数才可正常调用，否则将抛出却是仅关键字参数的异常。
# 仅有* params的形式才可以将形参放置到不定参后面，* * params后若有形参则无法通过语法检测。
def test(*params_a, a):
    print(a)
    print(*params_a)
    print(params_a)
    for each in params_a:
        print(each)
    return params_a


a = test(1, 2, 3, 4, 5, 6, a=9)
print(type(a))
