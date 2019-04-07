def Wava_Avoiddance():
	dis=int(Get_Distence())
	time.sleep(0.05)
	if dis > 25:
		Motor_Forward()
	else :
		Motor_Backward
		time.sleep(0.3)
		Motor_Stop()
		XRservo.XiaoRGEEK_SetServo(0x07,10)	##设置7舵机角度10°
		time.sleep(1)
		distance_L=int(Get_Distence())
		time.sleep(1)
		XRservo.XiaoRGEEK_SetServo(0x07,65)	##设置7舵机角度65°,根据实际情况测，此时角度位置是正中
		time.sleep(1)
		distance_M=int(Get_Distence())
		time.sleep(1)
		XRservo.XiaoRGEEK_SetServo(0x07,130)	##设置7舵机角度130
		time.sleep(1)
		distance_R=int(Get_Distence())
		time.sleep(1)
		if (distance_L<distance_R) & (distance_M<distance_R):
			Motor_TurnLeft()  #根据实际情况测，如果反了可以交换左右方向
			time.sleep(0.3)
			Motor_Stop()
		elif (distance_L<distance_M) & (distance_R<distance_M):
			Motor_Forward()
		elif (distance_M<distance_L) & (distance_R<distance_L):
			Motor_TurnRight()  #根据实际情况测，如果反了可以交换左右方向
			time.sleep(0.3)
			Motor_Stop()
		XRservo.XiaoRGEEK_SetServo(0x07,65)	##设置1舵机角度90°，舵机回中
		time.sleep(1)
