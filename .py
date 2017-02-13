import enchant
import sys,os,time,random

checker = enchant.Dict("en_US")
#참 거짓을 반환하는 checker.
#if(checker.check("hello")) 하면 참.
#checker.check("asdasd") 하면 거짓.

used_data = [] #이미사용된 단어 저장
time.sleep(1)
a_point=3
b_point=3

print("Loading dictionary ...")
print("""


    =-=-=-=-=-=-=-=-=-=-=-=-=( INFO )-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Developer : IT_GAME
    Power By  : Python 3
    Blog      : https://medium.com/@jinkwon711
    Since     : 2017 02 07
    Version   : 1.0.0 Alpha
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")
a_word = ""
b_word = ""
player_a_turn = False;
while True:
    a_word = input("시작할 영단어를 입력해주세요 : ")
    if(checker.check(a_word)):
        used_data.append(a_word)
        break

while True:
    if player_a_turn:
        while a_point>0:
            a_word = input("A's Turn -- '{}' 로 시작하는 영단어를 입력해!: ".format(b_word[-1]))
            if(b_word[-1]==a_word[0]):
                if(checker.check(a_word)):
                    if(a_word not in used_data):
                        used_data.append(a_word)
                        player_a_turn =False
                        break
                    else:
                        print("{}(은)는 이미 사용했자나!!".format(a_word))
                else:
                    print("이단어가 영어로 보이냐....?")
            else:
                print("{}단어로 끝나지 않았어! 다시써!".format(b_word[-1]))
    else:
        while True:
            b_word = input("B's Turn -- {}로 시작하는 영단어를 입력해주렴: ".format(a_word[-1]))
            if(a_word[-1]==b_word[0]):
                if(checker.check(b_word)):
                    if(b_word not in used_data):
                        used_data.append(b_word)
                        player_a_turn =True
                        break
                    else:
                        print("{}(은)는 이미 사용했단다!".format(b_word))
                else:
                    print("아쉽지만 이단어는 영어가 아니구나....?")
            else:
                print("{}단어로 끝나지 않았어 괜찮아 다시생각해봐^^ ".format(a_word[-1]))