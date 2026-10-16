
import time
import random
#aa = [1,2,3]
#random.shuffle(aa)
#print(aa)

print("공지: 이 게임은 도박 중독 위험이 있습니다. 모든 책임은 사용자에게 달려있습니다.")
money=1000
xp=0
level=1
while True:
    print("돈:", money)
    print("xp:",xp)
    if xp>level*10-1:
        level=level+1
        xp=xp-level*10
        print("level up!")
    print("level:", level)
    #aaa=input("a=러시안 룰렛 져도 안죽는 카드 사기 enter")
    if money>0:
        option=input("game choose 1= luckyslot(jackpot) 2=승마 3=러시안 룰렛(전 재산 걸고)")
        if option=='1':
            #랜덤룰렛
            print("Luckyslot에서는 똑같은 숫자 3개 (AAA)가 나오면 333원, 777이 나오면 7777원,\n 두개 나오면 122원을 갖습니다. 만약 실패 하면 60원을 잃습니다.")
            d=True
            while d:

                numberlist=[1,2,3,4,5,6,7,8,9]
                onenumber=random.choice(numberlist)
                twonumber=random.choice(numberlist)
                threenumber=random.choice(numberlist)
                print(onenumber, "", end="")
                time.sleep(0.3)
                print(twonumber, "", end="")
                time.sleep(0.3)
                print(threenumber, "", end="")
                time.sleep(0.3)
                if onenumber==7 and twonumber==7 and threenumber==7:
                    print("+7777원 JACKPOT")
                    money=money+7777
                    xp=xp+50
                elif onenumber==twonumber and twonumber==threenumber:
                    print("+333원 TRIPLE!")
                    money=money+333
                    xp=xp+10
                elif onenumber==twonumber or twonumber==threenumber or threenumber==onenumber:
                    print("+122원 DOUBLE")
                    money=money+122
                    xp=xp+1
                else:
                    print("-60원")

                    money=money-60
                print("돈:",money)
                v=input("끝=1 계속=Enter")
                if v=='1' or money<1:
                    d=False
                else:
                    continue
        if option=='2':
            #승마

            horselist=[]
            horsenamelist = ["가위", '민우', '강철연어', '오래오래살아라', '당근', '컴퓨터','건빵 좋아하는 말','용준']
            while len(horselist) != 5:
                name = random.choice(horsenamelist)
                if name not in horselist:
                    horselist.append(name)
                    
            print("경주마 목록:", horselist)
            horse=int(input("1-5번말 중에서 1마리를 고르세요. 번호만 쓰시오."))
            

            
            time.sleep(3)
            print(random.choice(horselist),"가 이기고 있습니다.")
            time.sleep(3)
            print(random.choice(horselist),"가 이기고 있습니다!")
            time.sleep(3)
            winhorse=random.choice(horselist)
            print(winhorse,"(이)가 이겼습니다!!!!!!!")
            if winhorse==horselist[horse - 1]:
                print("당신이 고른 말이 이겼습니다!")
                print("+300원!")
                money=money+300
                xp=xp+3
            else:
                print("졌습니다. -100원")
                money=money-10033
            
        if option == "3":
        
            numberlist=[1,2,3,4,5,6]
            answer=input("전재산을건 이 게임을 진짜 시작하시겠습니까?후회하실수 있습니다.그리고 상금은 1500원 입니다.(네,아니요)")
            if answer=="아니요":
                print("잘 선택 하셨습니다.")
                print("그럼 나가!!!!!!!!")
        
            if answer=="네":
                print("후회를 하지 않으시길 바랍니다...")
                print("이게임엔 6명의 사람이 있습니다.탈락되는 순간 그사람의 재산은 한순간에 사라지죠.")
                print("자그럼 시작하겠습니다...")
                
                answer = int(input("당신의 자리 번호를 입력: (1에서부터6까지)"))

                tangnumber=random.choice(numberlist)

                p = ['나 죽는거 아니지...?', '돈을 벌수 있겠군 ㅎㅎㅎ',"아악아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ"]

                while True:
                    print("총이 준비됐다", end='')
                    time.sleep(0.1)
                    print(".", end='')
                    time.sleep(0.1)
                    print(".", end='')
                    time.sleep(0.1)
                    print(".")

                    print("2")
                    break



                if answer==tangnumber:
                    print("당신은 죽었습니다.")
                    time.sleep(1)
                    money=0
                    break
                else:
                    print("+1500원")
                    money=money+1500
        else:
            print('잘못됀 입력입니다') 
                
                
                
    print("당신의 돈이 바닥났습니다.")

                

