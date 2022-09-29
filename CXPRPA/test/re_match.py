import re

# text = 'pythontab'
# m = re.match(r"\w+", text)
# if m:
#     print(m.group(0))
# else:
#     print('not match')

# print("===========================")
# print(re.match('abc', 'abcd'))

# print(re.match('01010?0000', '01010000001'))
# print(re.search('01010?0000', '01010000001'))

# res = re.sub(r"01010?0000", "*", "01010000001111")
# print(res)

print(re.fullmatch("010100*000",  "0101000000"))
# print(re.search("010100?000",  "0101000001"))
# print("===========================================")
# res = re.sub("010100?000", "", "0101000001")
#
# print(res)

