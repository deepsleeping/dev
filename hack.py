import time
a=input("ip를 우회하여  공격을 시작하시겠습니까?  Y/N")
while True:
	if(a=='Y'):
		for i in range(1,101):
			time.sleep(0.25)
			print("loading file {} %".format(i))
		print("loding terminate")
		time.sleep(5)
		print("cmd 자동 로그인")
		time.sleep(3) 
		print("cmd자동 로그인 성공")
		time.sleep(3)
		print("**AOL Pest [Dos attack]play**")
		time.sleep(10)
		break