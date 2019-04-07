#coding:utf-8
#Python中声明文件编码的注释，编码格式指定为utf-8
import time			#导入time库，可使用时间函数。
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)	##信号引脚模式定义，使用.BCM模式
LED0 = 10		##LED0的IO口定义
LED1 = 9		##LED1的IO口定义
LED2 = 25		##LED2的IO口定义
GPIO.setwarnings(False)
GPIO.setup(LED0,GPIO.OUT,initial=GPIO.HIGH)##led初始化为
GPIO.setup(LED1,GPIO.OUT,initial=GPIO.HIGH)##led初始化为
GPIO.setup(LED2,GPIO.OUT,initial=GPIO.HIGH)##led初始化为
def	init_light():	##使用def定义函数，可在其他地方调用此函数。未调用不执行。
	GPIO.output(LED0,False)
	GPIO.output(LED1,False)
	GPIO.output(LED2,False)###LED0,LED1,LED2 = 亮 亮 亮
	time.sleep(0.5)
	GPIO.output(LED0,True)
	GPIO.output(LED1,False)
	GPIO.output(LED2,False)###LED0,LED1,LED2 = 灭 亮 亮
	time.sleep(0.5)
	GPIO.output(LED0,False)
	GPIO.output(LED1,True)
	GPIO.output(LED2,False)###LED0,LED1,LED2 = 亮 灭 亮
	time.sleep(0.5)
	GPIO.output(LED0,False)
	GPIO.output(LED1,False)
	GPIO.output(LED2,True)###LED0,LED1,LED2 = 亮 亮 灭
	time.sleep(0.5)
	GPIO.output(LED0,False)
	GPIO.output(LED1,False)
	GPIO.output(LED2,False)###LED0,LED1,LED2 = 亮 亮 亮
	time.sleep(0.5)
	GPIO.output(LED0,True)
	GPIO.output(LED1,True)
	GPIO.output(LED2,True)###LED0,LED1,LED2 = 灭 灭 灭
	time.sleep(0.5)
for i in range(1,5):		#调用rang（）循环函数，功能类似 for（i =1;i<5;i++ ）执行4遍
	init_light()
'''
整个程序功能为：
	执行4遍流水灯状态
	程序结束
'''
