# coding:utf-8
# Python中声明文件编码的注释，编码格式指定为utf-8
from socket import *
from time import ctime
import binascii
import RPi.GPIO as GPIO
import time
import threading

#######################################
#############信号引脚定义##############
#######################################
GPIO.setmode(GPIO.BCM)
#######################################
#########管脚类型设置及初始化##########
#######################################
GPIO.setwarnings(False)

########超声波接口定义#################
ECHO = 4  # 超声波接收脚位
TRIG = 17  # 超声波发射脚位

##########超声波模块管脚类型设置#########
GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)  # 超声波模块发射端管脚设置trig
GPIO.setup(ECHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 超声波模块接收端管脚设置echo


####################################################
##函数名称 ：Get_Distence()
##函数功能 超声波测距，返回距离（单位是米）
##入口参数 ：无
##出口参数 ：无
####################################################
def Get_Distence():
    time.sleep(0.05)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TRIG, GPIO.LOW)
    while not GPIO.input(ECHO):
        pass
    t1 = time.time()
    while GPIO.input(ECHO):
        pass
    t2 = time.time()
    time.sleep(0.1)
    return (t2 - t1) * 340 / 2 * 100


####################################################
##函数名称 Send_Distance()
##函数功能 ：超声波距离PC端显示
##入口参数 ：无
##出口参数 ：无
####################################################
def Send_Distance():
    dis_send = int(Get_Distence())
    # dis_send = str("%.2f"%dis_send)
    if dis_send < 255:
        print 'Distance: %d cm' % dis_send


'''
循环检测
'''
while True:
    Send_Distance()


