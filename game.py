import random
print("반가워")
point = 10
rand=random.randrange(1,11)
tong=[]
while(point>0):
	i=input("1부터10까지중 원하는 숫자를 골라서 적어")
	if(rand>int(i)):
		point = point -1
		tong.append(i)
		print("그 숫자보단 커")
	elif(rand<int(i)):
		point  = point -1
		tong.append(i)
		print("그 숫자보단 작아")

	else:
		print("축하해")
		print("네 점수는 {}점 이야".format(point))
		for a in tong:
			print("네가 고른 틀린 숫자들은{}".format(a))
		break