import time
for grow in range(1,50):
	print("이 컴퓨터를 해킹 하지못하게 방벽을 관리자 권한으로 실행중{}".format(grow))
a=input("ip를 우회하여  공격을 시작하시겠습니까?  Y/N : ")
while True:
	if(a=='Y'):
		for i in range(1,101):
			time.sleep(0.25)
			print("loading file {} %".format(i))
		print("loading terminate")
		time.sleep(5)
		print("cmd 자동 로그인")
		time.sleep(3) 
		print("cmd자동 로그인 성공")
		time.sleep(3)
		print("**AOL Pest [AOS attacking]play**")
		time.sleep(10)
		print("=-=-=-==-=-==-=-=system attacking=-=-=-=-=-=-=-=-=-==")
		email=input("공격할 대상의 이메일 주소를 적어주세요 : ")
		for w in range(1,100):
			time.sleep(0.1)
			print("도메인 좀비 {}마리 전송 ".format(w))
		time.sleep(10)
		print("kimrungtext04@gmail.com해킹 성공 ")
		time.sleep(1)
		print("kimrungtext04@gmail.com의 사용자의 이름은(는) 김륭 ")
		print("이메일 제작 시간은(는) 17/2/13/PM7:30")
		print("계정이 만들어진 곳은 대한민굿 서울특별시 서대문구 북가좌동 거북골로")
		print("이메일 제작 기기(은)는 Samsung Galaxy S III")
		time.sleep(5)
		bug=input("Dos를 날렸으므로 이계정 사용자가 신고할수있기에  <AOS attacking>을 삭제함과 동시에 상대의 email과 기록을 삭제하여 재부팅 하겠습니다.")
		a=1
	else:
		break
