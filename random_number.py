import random
#print(random.randint(1,10))取隨機1~10

#option=["剪刀","石頭","布"]
#rand_option=random.choice(option)
#print(rand_option)

#cards=["2","3","4","5","6","7",'8',"9",'10',"J","Q","K",'A']
#random.shuffle(cards)打亂列表
#print(cards)

#猜數字遊戲
x=random.randint(1,100)
print(x)
guess=0
while True:
    y=int(input("請輸入你要猜的數字(1~100):"))
    guess+=1
    if y==x:
        print("恭喜答對")
        print(f"你總共猜了{guess}次")
        break
    elif y>x:
        print("太大了")
    elif y<x:
        print("太小了")
