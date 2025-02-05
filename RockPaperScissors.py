import random
running=True
while running:
    a = ["剪刀", "石頭", "布"]
    aigamer = random.choice(a)
    print(aigamer)
    gamer=input("請輸入剪刀石頭布:")
    if gamer==aigamer:
        print("平手")
    elif ((gamer=="剪刀" and aigamer=="石頭") or
         (gamer=="石頭" and aigamer=="布")or
         (gamer=="布" and aigamer=="剪刀")):
        print("你輸了,電腦勝利")
    else:
        print("你贏了")
    playAgain=input("是否再玩一局?(y,n)").lower()
    if not playAgain=="y":
        running=False
    else:
        print("謝謝遊玩")