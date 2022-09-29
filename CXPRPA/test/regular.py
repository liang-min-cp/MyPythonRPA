import re
result=re.search(r'wuyanzu','cn.wuyanzu') # search 会在里面寻找，并返回
a=result.group()
print(a)
result=re.match(r'wuyanzu','wuyanzu.cn') # match 如果开始没有则没有
b=result.group()
print(b)
result=re.match(r'.','M') # match '.'匹配任意字符
c=result.group()
print(c)
result=re.match(r't.o','too') # match '.'匹配任意字符
d=result.group()
print(d)
result=re.match(r'[x]','xs') # match '[]'匹配[]中列举的字符
e=result.group()
print(e)
result=re.match(r'\d','92bkbijk') # match '\d'匹配数字 即0-9
f=result.group()
print(f)
result=re.match(r'\D','M6151nmbhj') # match '\D'匹配非数字
g=result.group()
print(g)
result=re.match(r'\s',' M') # match '\s'匹配空白，即空格，tab键
h=result.group()
print(h)
result=re.match(r'\S','11 M') # match '\S'匹配非空白
i=result.group()
print(i)
result=re.match(r'\w','xM') # match '\w'匹配单词字符，即a-z，A-Z，0-9，_
j=result.group()
print(j)
result=re.match(r'\W',' M') # match '\W'匹配非单词字符
k=result.group()
print(k)
result=re.match(r'[A-Z][a-z]*','M') # match '*'匹配前一个字符出现0次或者无限次，即可有可无\d*等价于\d{0，}
l=result.group()
print(l)
result=re.match(r'[A-Z][a-z]*','MnnM') # match '*'匹配前一个字符出现0次或者无限次，即可有可无\d*等价于\d{0，}
m=result.group()
print(m)
result=re.match(r'[A-Z]+[a-z]','MnnM') # match '+'匹配前一个字符出现1次或者无限次，即至少有1次\d+等价于\d{1，}
m1=result.group()
print(m1)
result=re.match(r'[0-9]?[1-9]','33') # match '？'匹配前一个字符出现1次或者0次，即要么有1次，要么没有\d？等价于\d{0,1}
n=result.group()
print(n)
result=re.match(r'[0-9]?[^1-9]','00') # match '^'匹配[^]外的任何符号
o=result.group()
print(o)
result=re.match(r'[1-9]?[0-9]','09') # match '？'匹配前一个字符出现1次或者0次，即要么有1次，要么没有\d？等价于\d{0,1}
p=result.group()
print(p)
result=re.match(r'[a-zA-Z0-9_]{8,20}','12345sdwdfac') # match '{m,n}'匹配前一个字符出现m到n次
q=result.group()
print(q)
result=re.match(r'[a-zA-Z0-9_]{6}','12345sdwdfac') # match '{m}'匹配前一个字符出现m次
r=result.group()
print(r)
result=re.match(r'[\w]{4,20}@163.com','272263915@163.com') # match '{m,n}'匹配前一个字符出现m到n次
s=result.group()
print(s)
result=re.findall(r'\d+','python=9999,c=8888,c++=12345') # findall 匹配数字
t=result
print(t)
result=re.sub(r'\d+','998','c=8888') # sub  替换数字
u=result
print(u)
result=re.split(r'\:','info:xiaoming')   # split 分割  linux上是':|'作为分割符
v=result
print(v)
xxx=re.match('^4.*[369]$','46516516')
sss=xxx.group()
print(sss)
www=re.match('\.\*','.*').group()
print(www)
mylist=['apple','banana','pen','orange']
for i in mylist:
    match_obj=re.match('apple|pen',i)
    if match_obj:
        print(match_obj.group())
    else:
        print('没有')

mail=['aaa@163.com','bbb@126.com','ccc@qq.com']
for i in mail:
    match_obj=re.match('\w{3,20}@(163|126)\.com$',i)
    if match_obj:
        print(match_obj.group())
        print(match_obj.group(1))

    else:
        print('没有')

tel=re.match('(0[1-9][0-9]{1,2})-?(\d{6,8})','010-123456').group()
print(tel)
