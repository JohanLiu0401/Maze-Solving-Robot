#coding:utf-8
#Python中声明文件编码的注释，编码格式指定为utf-8
import time #导入time库，可使用时间函数
import binascii
import RPi.GPIO as GPIO
from smbus2 import SMBus             #这里导入的包改过
XRservo = SMBus(1)
GPIO.setmode(GPIO.BCM)	##信号引脚模式定义，使用.BCM模式
GPIO.setwarnings(False)
'''
XRservo中，有3个标准函数可直接使用
1、设置舵机角度
	XRservo.XiaoRGEEK_SetServo(0x01,angle)
	注释：此函数为设置1号舵机角度为angle
2、舵机角度记忆，存储当前所有舵机角度值。
	XRservo.XiaoRGEEK_SaveServo()
3、恢复所有舵机至已存储的角度
	XRservo.XiaoRGEEK_ReSetServo()
'''
time.sleep(2)
XRservo.XiaoRGEEK_SetServo(0x01,90)	##设置1舵机角度90°
print('ser1= 90° ')
time.sleep(0.5)
XRservo.XiaoRGEEK_SetServo(0x01,30)	##设置1舵机角度30°
print('ser1= 30°并存储 ')
time.sleep(0.1)
XRservo.XiaoRGEEK_SaveServo()	##存储当前角度（30°）
time.sleep(0.5)
XRservo.XiaoRGEEK_SetServo(0x01,90)	##设置1舵机角度90°
print('ser1= 90° ')
time.sleep(0.5)
XRservo.XiaoRGEEK_SetServo(0x01,150)##设置1舵机角度150°
print('ser1= 90° ')
time.sleep(1.5)
XRservo.XiaoRGEEK_ReSetServo()	##恢复舵机存储的角度（30°）
print('ser1= 90° ')
'''
整个程序功能为：
	舵机转动到90°
	舵机转动到30°，并存储，
	依次隔0.5s，转动到90°及150°
	隔1.5s后，恢复存储的角度30°
	程序结束
'''
