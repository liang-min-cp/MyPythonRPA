import sys

sys.path.append("..")
sys.path.append("../..")
import pyautogui as gui
import subprocess
import pyperclip
import xlrd
from xlutils.copy import copy
import os
from fins.PortEth import *
import datetime

'''
def openCxpFile():
    os.startfile(r'状态转换自动测试Ladder.cxp')
    print("打开cxp文件")

def onlinework():
    gui.hotkey('ctrl','w')

def pressY():
    gui.press('Y')

def transfertoPLCNoSetting():
    gui.hotkey('ctrl','t')

def pressEnter():
    gui.press('enter')
'''

PCport = PortEth('192.168.250.101', '192.168.250.1', 9600)
cmd = bytes.fromhex('8000020001000065005520010000030053260002')
rsp0101equal1 = bytes.fromhex('c0000200650000010055200100000003')

# 读取excel数据
readbook = xlrd.open_workbook(r'testcase.xlsx')
sheet_name = 'testsheet'
sheet = readbook.sheet_by_name(sheet_name)
# 状态个数
state_num = sheet.cell(1, 0).value
# 循环次数
cycleNum = sheet.cell(1, 1).value

# 创建状态列表
state = []

# 将excel中的状态赋值给state列表
for i in range(int(state_num)):
    state.append(sheet.cell(i + 4, 3).value)

# mouseposition
# 将excel中的鼠标位置进行赋值
sheet_name1 = 'testsheet'
sheet1 = readbook.sheet_by_name(sheet_name1)
# position2_B_x = sheet1.cell(2, 2).value
# position2_B_y = sheet1.cell(2, 3).value

current_x = sheet1.cell(1, 4).value
current_y = sheet1.cell(1, 5).value

window_x = sheet1.cell(2, 4).value
window_y = sheet1.cell(2, 5).value

positionx = []
positiony = []

for i in range(int(state_num)):
    positionx.append(sheet1.cell(i + 4, 4).value)
    positiony.append(sheet1.cell(i + 4, 5).value)

# 鼠标位置确认测试
# for i in range(int(state_num)):
#
#     print(state[i])
#     print(positionx[i],positiony[i])

op_delay = 0.5
sleep(1)

currentstate = 'normal'

'''
#打开CXP文件，路径固定
openCxpFile()
print("等待10s，打开cxp文件")
time.sleep(10)

#直接在线
#使用Ctrl+W 点击直接在线
onlinework()
print("等待10s，在线操作")
time.sleep(10)

#使用“Y”确认（点击“是”）
pressY()
print("等待10s，点击’是‘")
time.sleep(10)

#传送数据（不包含设置）
#使用ctrl+T传送到PLC（不含设置）
transfertoPLCNoSetting()
print("等待5s，传送到plc界面显示")
time.sleep(5)

#点击enter，进行传输
pressEnter()
print("等待5s，传送到plc界面显示")
time.sleep(5)

#使用“Y”确认（点击“是”）
#命令将影响plc状态，要继续吗？
pressY()
print("等待10s，点击’是‘")
time.sleep(10)

#使用“Y”确认（点击“是”）
#下载完成后点击确认
pressY()
print("等待5s，点击’是‘")
time.sleep(5)

#点击enter（点击“是”）
#切换到编程模式
pressEnter()
print("等待5s，点击’是‘")
time.sleep(5)

#使用“Y”确认（点击“是”）
#切换到运行模式
pressY()
print("等待5s，点击’是‘")
time.sleep(5)
'''

# 鼠标点击EC-Engineer 将窗口置顶
gui.moveTo(window_x, window_y, duration=op_delay)
gui.click(window_x, window_y)
sleep(op_delay)
# log = open("a.txt", mode="a", encoding="utf-8")
sheet1_copy = copy(readbook)
write_sheet1 = sheet1_copy.get_sheet(0)

now_time = datetime.datetime.now()

for i in range(int(cycleNum)):
    write_sheet1.write(3, i + 6, '结果' + str(i + 1))
    sheet1_copy.save(r'testresult.xls')
    k = 0
    # ----------EC-E init1状态切换------------------
    # tic = time.time()
    for j in range(int(state_num)):

        # if j == 3:
        #     tic = time.time()
        #
        # if j == 7:
        #     toc = time.time()
        #     shijian = toc - tic
        #     print(shijian)

        # 状态选择
        gui.moveTo(positionx[j], positiony[j], duration=op_delay)
        gui.click(positionx[j], positiony[j])
        sleep(4)

        result = PCport.send_cmd_wait_rsp(cmd=cmd, rsp=rsp0101equal1)
        if result[0] == True:
            k += 1
            if k == 2:
                op_time = datetime.datetime.now()
                minus_time = str(op_time - now_time)
                if int(minus_time[5:7]) > 60:
                    print('第' + str(i + 1) + '次检测超时')
                now_time = op_time

        # current状态选择
        gui.moveTo(current_x, current_y, duration=op_delay)
        gui.click(current_x, current_y)
        sleep(op_delay)

        # 全选目标数据
        gui.hotkey('ctrl', 'a')
        sleep(op_delay)
        # 复制目标数据
        gui.hotkey('ctrl', 'c')
        sleep(op_delay)

        write_sheet1.write(j + 4, i + 6, state[j])
        sheet1_copy.save(r'testresult.xls')

        '''
        x = pyperclip.paste()
        if x != state[j]:
            currentstate = 'abnormal'
            #print('switch num',j+1,x,'NG',file = log)
            #write_sheet1.write(j+4,i+6,'NG')
            #sheet1_copy.save(r'testresult.xls')
        else:
            write_sheet1.write(j + 4, i + 6, 'OK')
            sheet1_copy.save(r'testresult.xls')
            continue
        '''

    # ----------EC-E init1状态切换------------------

    # print(shijian)
    # toc = time.time()
    # shijian = toc - tic
    # print(shijian)

    # 将结果输出为txt文件
    # print('current round:',i,file = log)
    # print('state switch:',currentstate,file = log)

    '''
    if currentstate == 'abnormal':
        break
    else:
        continue
    '''
# log.close()
gui.moveTo(861, 273, duration=op_delay)
gui.click(861, 273)
sleep(1)
gui.alert('程序执行完毕，请查看运行结果后关闭此窗口')

