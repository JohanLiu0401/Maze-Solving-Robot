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


"""
电机代码
"""

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


"""
前侧超声波模块代码
"""

FRONT_ECHO = 4  # 超声波接收脚位
FRONT_TRIG = 17  # 超声波发射脚位

"""
前侧超声波模块管脚类型设置
"""
GPIO.setup(FRONT_TRIG, GPIO.OUT, initial=GPIO.LOW)  # 超声波模块发射端管脚设置trig
GPIO.setup(FRONT_ECHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 超声波模块接收端管脚设置echo


def get_front_distance():
    time.sleep(0.05)
    GPIO.output(FRONT_TRIG, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(FRONT_TRIG, GPIO.LOW)
    while not GPIO.input(FRONT_ECHO):
        pass
    t1 = time.time()
    while GPIO.input(FRONT_ECHO):
        pass
    t2 = time.time()
    time.sleep(0.1)
    return (t2 - t1) * 340 / 2 * 100


def detect_front():
    dis_send = int(get_front_distance())
    # dis_send = str("%.2f"%dis_send)
    if dis_send < 10:
        print('Obstacle detected on the front: %d cm' % dis_send)
        return True
    else:
        print("Obstacle not detected on the front")
        return False


"""
左侧超声波模块代码
"""
LEFT_ECHO = 7  # 超声波接收脚位
LEFT_TRIG = 5  # 超声波发射脚位
#

##########超声波模块管脚类型设置#########
GPIO.setup(LEFT_TRIG, GPIO.OUT, initial=GPIO.LOW)  # 超声波模块发射端管脚设置trig
GPIO.setup(LEFT_ECHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 超声波模块接收端管脚设置echo


def get_left_distance():
    time.sleep(0.05)
    GPIO.output(LEFT_TRIG, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(LEFT_TRIG, GPIO.LOW)
    while not GPIO.input(LEFT_ECHO):
        pass
    t1 = time.time()
    while GPIO.input(LEFT_ECHO):
        pass
    t2 = time.time()
    time.sleep(0.1)
    return (t2 - t1) * 340 / 2 * 100


def detect_left():
    dis_send = int(get_left_distance())
    # dis_send = str("%.2f"%dis_send)
    if dis_send < 10:
        print('Distance: %d cm' % dis_send)
        return True
    else:
        print("未检测到障碍物")
        return False


"""
右侧超声波模块代码
"""

RIGHT_ECHO = 8  # 超声波接收脚位
RIGHT_TRIG = 11  # 超声波发射脚位
#

##########超声波模块管脚类型设置#########
GPIO.setup(RIGHT_TRIG, GPIO.OUT, initial=GPIO.LOW)  # 超声波模块发射端管脚设置trig
GPIO.setup(RIGHT_ECHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 超声波模块接收端管脚设置echo


def get_right_distance():
    time.sleep(0.05)
    GPIO.output(RIGHT_TRIG, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(RIGHT_TRIG, GPIO.LOW)
    while not GPIO.input(RIGHT_ECHO):
        pass
    t1 = time.time()
    while GPIO.input(RIGHT_ECHO):
        pass
    t2 = time.time()
    time.sleep(0.1)
    return (t2 - t1) * 340 / 2 * 100


def detect_right():
    dis_send = int(get_right_distance())
    # dis_send = str("%.2f"%dis_send)
    if dis_send < 10:
        print('Distance: %d cm' % dis_send)
        return True
    else:
        print("未检测到障碍物")
        return False



"""
红外线模块代码
"""
#######红外传感器接口定义#################
IR_R = 18  # 小车右侧巡线红外
IR_L = 27  # 小车左侧巡线红外


#########红外初始化为输入，并内部拉高#########
GPIO.setup(IR_R, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def detect_end():
    if (GPIO.input(IR_L) == True) & (GPIO.input(IR_R) == True):     # 两侧都检测到黑色区域
        return True
    else:
        return False





"""电子罗盘模块代码"""


# 判断小车方向
def judge_direction():
    direction = None
    return direction


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



