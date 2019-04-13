# coding:utf-8
# Python中声明文件编码的注释，编码格式指定为utf-8
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

"""
右侧超声波模块脚位
"""

RIGHT_ECHO = 8  # 超声波接收脚位
RIGHT_TRIG = 11  # 超声波发射脚位


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


'''
循环检测
'''
while True:
    detect_right()










