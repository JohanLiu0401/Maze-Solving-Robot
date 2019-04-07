# coding:utf-8
# Python中声明文件编码的注释，编码格式指定为utf-8
from socket import *
from time import ctime
import binascii
import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

########电机驱动接口定义#################
ENA = 13  # //L298使能A
ENB = 20  # //L298使能B
IN1 = 19  # //电机接口1
IN2 = 16  # //电机接口2
IN3 = 21  # //电机接口3
IN4 = 26  # //电机接口4

#########电机初始化为LOW##########
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)


########超声波接口定义#################
# 前侧超声波模块脚位
ECHO = 4  # 超声波接收脚位
TRIG = 17  # 超声波发射脚位
#

##########超声波模块管脚类型设置#########
GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)  # 超声波模块发射端管脚设置trig
GPIO.setup(ECHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 超声波模块接收端管脚设置echo



#########定义电机函数##########
def motor_forward():
    print 'motor forward'
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)


def motor_backward():
    print 'motor_backward'
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)


def motor_turnLeft():
    print 'motor_turnleft'
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)


def motor_turnRight():
    print 'motor_turnright'
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)


def motor_stop():
    print 'motor_stop'
    GPIO.output(ENA, False)
    GPIO.output(ENB, False)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)


def get_front_distance():
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


def detect_left():
    dis_send = int(get_front_distance())
    # dis_send = str("%.2f"%dis_send)
    if dis_send < 300:
        print('Distance: %d cm' % dis_send)
        return True
    else:
        print("左边未检测到障碍物")
        return False


def detect_front():
    dis_send = int(get_front_distance())
    # dis_send = str("%.2f"%dis_send)
    if dis_send < 300:
        print('Distance: %d cm' % dis_send)
        return True
    else:
        print("前方未检测到障碍物")
        return False


def detect_right():
    dis_send = int(get_front_distance())
    # dis_send = str("%.2f"%dis_send)
    if dis_send < 300:
        print('Distance: %d cm' % dis_send)
        return True
    else:
        print("右侧未检测到障碍物")
        return False


####################################################
##函数名称 Send_Distance()
##函数功能 ：超声波距离PC端显示
##入口参数 ：无
##出口参数 ：无
####################################################
# def detect_obstacle():
#     dis_send = int(get_front_distance())
#     # dis_send = str("%.2f"%dis_send)
#     if dis_send < 300:
#         print('Distance: %d cm' % dis_send)
#         return True
#     else:
#         print("未检测到障碍物")
#         return False
#

# '''
# 循环检测
# '''
# while True:
#     Send_Distance()

# Motor_Forward()
# time.sleep(0.5)
# Motor_Backward()
# time.sleep(0.5)
# Motor_TurnLeft()
# time.sleep(0.5)
# Motor_TurnRight()
# timeout.sleep(0.5)

# print("calculate distance")
# dis = int(Get_Distence())
# print ("distance", dis)

