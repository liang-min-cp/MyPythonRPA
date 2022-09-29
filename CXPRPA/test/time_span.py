seconds = 5555
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print("%02d:%02d:%02d" % (h, m, s))

seconds_all = 333.44
m, s = divmod(seconds_all, 60)
print(m)
print(s)
res = "%02d 分 %.2f 秒" % (m, s)
print(res)
print("=======================")
seconds_amount = 55
time_amount = "%.2f 秒" % seconds_amount
print(time_amount)

