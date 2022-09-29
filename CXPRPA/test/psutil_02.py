import os

import psutil
from psutil import *
from datetime import *
import signal

#
# print(psutil.cpu_count())  # 8 获取 CPU 的逻辑数量
# print(psutil.cpu_count(logical=False))  # 4 获取 CPU 的物理核心数量
# print(psutil.cpu_times())  # 统计 CPU 的用户／系统／空闲时间
# print(psutil.cpu_times_percent() ) # 功能与之类似, 只不过返回的比例
#
# # 查看 CPU 的使用率
# for x in range(3):
#     # interval：表示每隔0.5s刷新一次
#     # percpu：表示查看所有的cpu使用率
#     print(psutil.cpu_percent(interval=0.5, percpu=True))
# """
# [6.1, 6.2, 9.4, 3.1, 0.0, 0.0, 0.0, 6.2, 3.1, 3.1, 3.1, 0.0]
# [0.0, 0.0, 6.1, 0.0, 6.1, 3.0, 0.0, 3.0, 3.0, 3.0, 0.0, 9.1]
# [0.0, 0.0, 6.2, 3.1, 3.1, 0.0, 3.1, 3.1, 3.1, 3.1, 0.0, 0.0]
# """
# # 我这里cpu的逻辑数量是12, 所以每个列表里面有12个元素
#
# # 查看 CPU 的统计信息，包括上下文切换、中断、软中断，以及系统调用次数等等
# print(psutil.cpu_stats())
#
#
# # 查看内存使用情况
# print(psutil.virtual_memory())
#
# print(psutil.swap_memory())
#
# # 查看磁盘分区、磁盘使用率和磁盘 IO 信息
# print(psutil.disk_partitions())
# print(psutil.disk_usage("C:\\"))
# print(psutil.disk_io_counters())
# print(psutil.disk_io_counters(perdisk=True))

# pids = psutil.pids()
# for pid in pids:
#     p = psutil.Process(pid)
#     # get process name according to pid
#     process_name = p.name()
#
#     print("Process name is: %s, pid is: %s" % (process_name, pid))
#
# print(psutil.net_io_counters())
# print(psutil.net_io_counters(pernic=True))
# print(psutil.net_if_addrs())
# print(psutil.net_if_stats())
# print(psutil.net_connections())
# print("=============================")
# print(psutil.users())
# print("=============================")
# print(psutil.boot_time())  # 1585282271.0
# print(datetime.fromtimestamp(psutil.boot_time()))  # 2020-03-27 12:11:11
# print("=============================")
# print(psutil.pids())
# print(psutil.pid_exists(22333))  # False
# print(psutil.pid_exists(0))  # True
# print(psutil.process_iter())
# print(psutil.Process(pid=0))
#
# for pid in psutil.pids():
#     p = psutil.Process(pid=pid)
#     print(str(pid) + " :  " + p.name())
#
# p = psutil.Process(pid=12896)
#
# # 进程名称
# print(p.name()) # WeChat.exe
#
# # 进程的exe路径
# print(p.exe()) # D:\WeChat\WeChat.exe
#
# # 进程的工作目录
# print(p.cwd()) # D:\WeChat
#
# # 进程启动的命令行
# print(p.cmdline()) # ['D:\\WeChat\\WeChat.exe']
#
# # 当前进程id
# print(p.pid) # 16948
#
# # 父进程id
# print(p.ppid()) # 11700
#
# # 父进程
# print(p.parent()) # psutil.Process(pid=11700, name='explorer.exe', started='09:19:06')
#
# # 子进程列表
# print(p.children())
# """
# [psutil.Process(pid=17452, name='WeChatWeb.exe', started='09:21:02'),
#  psutil.Process(pid=16216, name='WeChatApp.exe', started='09:21:40'),
#  psutil.Process(pid=13452, name='SogouCloud.exe', started='09:22:14')]
# """
#
# # 进程状态
# print(p.status()) # running
#
# # 进程用户名
# print(p.username()) # LAPTOP-264ORES3\satori
#
# # 进程创建时间,返回时间戳
# print(p.create_time()) # 1561775539.0
#
# # 进程终端
# # 在windows上无法使用
# try:
#     print(p.terminal())
# except Exception as e:
#     print(e) # 'Process' object has no attribute 'terminal'
#
# # 进程使用的cpu时间
# print(p.cpu_times())  # pcputimes(user=133.3125, system=188.203125, children_user=0.0, children_system=0.0)
#
# # 进程所使用的的内存
# print(p.memory_info())
# """
# pmem(rss=128634880, vms=117067776, num_page_faults=12193918,
#      peak_wset=263921664, wset=128634880, peak_paged_pool=1398584,
#      paged_pool=1329936, peak_nonpaged_pool=313896, nonpaged_pool=152192,
#      pagefile=117067776, peak_pagefile=201670656, private=117067776)
# """
#
# # 进程打开的文件
# print(p.open_files())
# """
# [popenfile(path='C:\\Users\\satori\\Documents\\WeChat Files\\wxid_3ksrps1o47mf22\\Msg\\Media.db-wal', fd=-1),
#  popenfile(path='C:\\Users\\satori\\AppData\\Roaming\\Tencent\\WeChat\\All Users\\CefResources\\2581\\qb_200_percent.pak', fd=-1),
#  popenfile(path='C:\\Users\\satori\\Documents\\WeChat Files\\wxid_3ksrps1o47mf22\\Msg\\Multi\\MSG0.db-shm', fd=-1),
#  popenfile(path='C:\\Program Files\\WindowsApps\\Microsoft.LanguageExperiencePackzh-CN_18362.28.87.0_neutral__8wekyb3d8bbwe\\Windows\\System32\\zh-CN\\dui70.dll.mui', fd=-1),
#  popenfile(path='C:\\Users\\satori\\Documents\\WeChat Files\\wxid_3ksrps1o47mf22\\Msg\\Multi\\MediaMSG2.db-shm', fd=-1),
#  popenfile(path='C:\\Users\\satori\\Documents\\WeChat Files\\wxid_3ksrps1o47mf22\\Msg\\Emotion.db-wal', fd=-1),
#  popenfile(path='C:\\Windows\\Fonts\\msyh.ttc', fd=-1),
#  ......
#  ......
#  ......
#  ]
# """
#
# # 进程相关的网络连接
# print(p.connections())
# """
# [pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='192.168.8.115', port=5162), raddr=addr(ip='183.3.234.107', port=443), status='ESTABLISHED'),
#  pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='192.168.8.115', port=13856), raddr=addr(ip='61.151.168.204', port=80), status='CLOSE_WAIT'),
#  pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='0.0.0.0', port=8680), raddr=(), status='LISTEN')]
# """
#
# # 进程内的线程数量，这个进程开启了多少个线程
# print(p.num_threads())  # 66
#
# # 这个进程内的所有线程信息
# print(p.threads())
# """
# [pthread(id=13340, user_time=113.328125, system_time=179.015625),
#  pthread(id=17120, user_time=0.0, system_time=0.0625),
#  pthread(id=7216, user_time=0.15625, system_time=0.515625),
#  pthread(id=13360, user_time=0.703125, system_time=0.21875),
#  pthread(id=10684, user_time=0.015625, system_time=0.078125),
#  pthread(id=13552, user_time=2.9375, system_time=0.171875),
#  pthread(id=12620, user_time=0.265625, system_time=0.296875),
#  pthread(id=14492, user_time=0.015625, system_time=0.03125),
#  pthread(id=14568, user_time=0.0, system_time=0.046875),
#  pthread(id=17112, user_time=0.015625, system_time=0.0625),
#  pthread(id=9344, user_time=0.0, system_time=0.015625),
#  pthread(id=13544, user_time=0.0, system_time=0.0),
#  pthread(id=10028, user_time=0.078125, system_time=0.125),
#  pthread(id=4920, user_time=0.015625, system_time=0.0625),
#  pthread(id=5744, user_time=0.0, system_time=0.015625),
#  pthread(id=7044, user_time=0.0, system_time=0.0),
#  pthread(id=14064, user_time=0.0, system_time=0.0),
#  pthread(id=11916, user_time=0.0, system_time=0.0),
#  pthread(id=1316, user_time=0.0, system_time=0.0),
#  pthread(id=18100, user_time=0.0, system_time=0.0),
#  pthread(id=2992, user_time=0.0, system_time=0.0),
#  pthread(id=8956, user_time=0.0, system_time=0.0),
#  pthread(id=8588, user_time=0.03125, system_time=0.03125),
#  pthread(id=3944, user_time=0.0, system_time=0.03125),
#  pthread(id=15828, user_time=0.0, system_time=0.015625),
#  pthread(id=7348, user_time=0.0, system_time=0.03125),
#  pthread(id=3400, user_time=0.0, system_time=0.015625),
#  pthread(id=8628, user_time=0.0, system_time=0.0),
#  pthread(id=2400, user_time=0.0, system_time=0.0),
#  pthread(id=9432, user_time=1.28125, system_time=0.171875),
#  pthread(id=11544, user_time=0.0, system_time=0.015625),
#  pthread(id=12348, user_time=2.96875, system_time=3.78125),
#  pthread(id=3444, user_time=0.0, system_time=0.0),
#  pthread(id=17476, user_time=0.0, system_time=0.0),
#  pthread(id=15856, user_time=0.0, system_time=0.015625),
#  pthread(id=12248, user_time=0.0, system_time=0.0),
#  pthread(id=17280, user_time=0.0, system_time=0.0),
#  ......
#  ......
#  ......
#  ]
# """
#
# # 进程的环境变量
# print(p.environ())
# """
# {'ALLUSERSPROFILE': 'C:\\ProgramData',
#  'APPDATA': 'C:\\Users\\satori\\AppData\\Roaming',
#  'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files',
#  'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
#  'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files',
#  'COMPUTERNAME': 'LAPTOP-264ORES3',
#  'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe',
#  'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData',
#  'GOPATH': 'C:\\Users\\satori\\go',
#  'HOMEDRIVE': 'C:',
#  'HOMEPATH': '\\Users\\satori',
#  'LOCALAPPDATA': 'C:\\Users\\satori\\AppData\\Local',
#  'LOGONSERVER': '\\\\LAPTOP-264ORES3',
#  'NUMBER_OF_PROCESSORS': '12',
#  'ONEDRIVE': 'C:\\Users\\satori\\OneDrive',
#  'ONEDRIVECONSUMER': 'C:\\Users\\satori\\OneDrive',
#  'ONLINESERVICES': 'Online Services',
#  'OS': 'Windows_NT',
#  'PATH': 'C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine '
#          'Components\\iCLS\\;C:\\Program Files\\Intel\\Intel(R) Management '
#          'Engine '
#          'Components\\iCLS\\;C:\\windows\\system32;C:\\windows;C:\\windows\\System32\\Wbem;C:\\windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\windows\\System32\\OpenSSH\\;C:\\Program '
#          'Files (x86)\\Intel\\Intel(R) Management Engine '
#          'Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine '
#          'Components\\DAL;C:\\Program Files (x86)\\NVIDIA '
#          'Corporation\\PhysX\\Common;C:\\Program '
#          'Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common '
#          'Files\\Intel\\WirelessCommon\\;C:\\python37;c:\\python37\\Scripts;C:\\Program '
#          'Files\\Git\\cmd;E:\\instantclient_10_2;C:\\Program '
#          'Files\\Redis\\;D:\\ffmpeg\\bin;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Go\\bin;C:\\MingW\\bin;C:\\Users\\satori\\.cargo\\bin;C:\\python37\\Scripts\\;C:\\python37\\;C:\\python38\\Scripts\\;C:\\python38\\;C:\\Users\\satori\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\satori\\go\\bin',
#  'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC',
#  'PLATFORMCODE': 'AN',
#  'PROCESSOR_ARCHITECTURE': 'x86',
#  'PROCESSOR_ARCHITEW6432': 'AMD64',
#  'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 10, GenuineIntel',
#  'PROCESSOR_LEVEL': '6',
#  'PROCESSOR_REVISION': '9e0a',
#  'PROGRAMDATA': 'C:\\ProgramData',
#  'PROGRAMFILES': 'C:\\Program Files (x86)',
#  'PROGRAMFILES(X86)': 'C:\\Program Files (x86)',
#  'PROGRAMW6432': 'C:\\Program Files',
#  'PSMODULEPATH': 'C:\\Program '
#                  'Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules',
#  'PUBLIC': 'C:\\Users\\Public',
#  'REGIONCODE': 'APJ',
#  'SESSIONNAME': 'Console',
#  'SYSTEMDRIVE': 'C:',
#  'SYSTEMROOT': 'C:\\WINDOWS',
#  'TBS_CONTENT_MAIN_RUNNER_INITIALIZED': '1',
#  'TEMP': 'C:\\Users\\satori\\AppData\\Local\\Temp',
#  'TMP': 'C:\\Users\\satori\\AppData\\Local\\Temp',
#  'USERDOMAIN': 'LAPTOP-264ORES3',
#  'USERDOMAIN_ROAMINGPROFILE': 'LAPTOP-264ORES3',
#  'USERNAME': 'satori',
#  'USERPROFILE': 'C:\\Users\\satori',
#  'VS140COMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio '
#                    '14.0\\Common7\\Tools\\',
#  'WINDIR': 'C:\\WINDOWS',
#  'WXDRIVE_START_ARGS': '--wxdrive-setting=0 --disable-gpu '
#                        '--disable-software-rasterizer '
#                        '--enable-features=NetworkServiceInProcess'}
# """
#
# # 结束进程, 返回 None, 执行之后微信就会被强制关闭, 当然这里就不试了
# # print(p.terminal())  # None
#
# print("=======================")
# # psutil.test()
print("=======================")


for prcs in psutil.process_iter():
    print(str(prcs.pid) + "  :  " +prcs.name())
    # print(prcs.pid)
    # if prcs.name().lower() == "chrome.exe":
    #     print(prcs.pid)
    # if prcs.name().lower().__contains__("cxp"):
    #     print(prcs.pid)
    #     print(prcs.name())
    if prcs.name().lower() == "cx-p.exe":
        os.kill(prcs.pid, signal.SIGILL)
        print("发现进程{0}，杀死".format( prcs.name()))








"""
16948
"""

# 有了这个操作之后，我们便可以通过进程 id 找到对应的进程
# 然后修改里面的数据





