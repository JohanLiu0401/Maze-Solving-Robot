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

#######红外传感器接口定义#################
IR_M = 22  # 小车中间避障红外

#########电机初始化为LOW##########
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

#########红外初始化为输入，并内部拉高#########
GPIO.setup(IR_M, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#########定义电机函数##########
def Motor_Forward():
    print 'motor forward'
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)


def Motor_Backward():
    print 'motor_backward'
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)


def Motor_TurnLeft():
    print 'motor_turnleft'
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)


def Motor_TurnRight():
    print 'motor_turnright'
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)


def Motor_Stop():
    print 'motor_stop'
    GPIO.output(ENA, False)
    GPIO.output(ENB, False)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)


def Avoiding():  # 红外避障函数
    if GPIO.input(IR_M) == False:  # 检测到障碍物低电平停止
        Motor_Stop()
        return
    else:
        Motor_Forward()  # 如果没有检测到前进
        return


'''
循环检测
'''
while True:
    Avoiding()
