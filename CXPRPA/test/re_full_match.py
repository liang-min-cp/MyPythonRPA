# python 3.6
# 蔡军生
# http://blog.csdn.net/caimouse/article/details/51749579
#
import re

text = 'This is some text -- with punctuation.'
pattern = 'is'

print('Text    :', text)
print('Pattern  :', pattern)

m = re.search(pattern, text)
print('Search   :', m)
s = re.fullmatch(pattern, text)
print('Full match :', s)

text = 'is'
print('Text    :', text)
s = re.fullmatch(pattern, text)
print('Full match :', s)

text = 'iss'
print('Text    :', text)
s = re.fullmatch(pattern, text)
print('Full match :', s)

