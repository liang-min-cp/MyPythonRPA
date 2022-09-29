import re


# 功能：检查字符串str是否符合正则表达式re_exp
# re_exp:正则表达式
# str:待检查的字符串
def check_string(re_exp, str):
    res = re.search(re_exp, str)
    if res:
        return True
    else:
        return False


def check_string_full(re_exp, str):
    res = re.fullmatch(re_exp, str)
    if res:
        return True
    else:
        return False


def check_string_match(re_exp, str):
    res = re.fullmatch(re_exp, str)
    if res:
        return True
    else:
        return False


# 检查格式是否满 YYYY-MM-DD的日期格式
# print(check_string('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', "2012-03-04"))  # True
# print(check_string('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', "1232012-03-04"))  # False
# print(check_string('0101000000', "0101000000"))  #
# print(check_string('01020000', "c000020005000001005501020000"))
print(check_string('010100?000', "0101000000000222333"))
print(check_string_full('01010?0000', "0101000000"))
print(check_string_match('01010?0000', "0101000000"))
# 010100?000
# 0101000001