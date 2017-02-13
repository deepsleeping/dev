A = "사랑해"
while True:
	B=input("{}에 단어를 입력해주세요 : ".format(A))
	if(A[-1]==B[0]):
		print("통과!\n")
		A=B
	else:
		print("떙\n")
		break
