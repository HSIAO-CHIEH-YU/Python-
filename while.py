#name=input("請輸入使用者名稱:")
#if name=="":
#    print("你沒有輸入名字")
#else:
#    print(f"你好,{name}!")
##############################################
#name=""
#while name=="":
#    name=input("請輸入使用者名稱:")
#print(f"你好,{name}~~")
###############################################
#food=input("請輸入你喜歡吃的食物:")
#while food!="q":
#    print(f"你喜歡吃的食物是{food}")
#    food=input("請輸入你喜歡吃的食物:")
#print("再見!")
###############################################
number=int(input("請輸入一到十的數字:"))
while not 1<=number<11:
    print("輸入無效")
    number=int(input("請輸入一到十的數字:"))
print(f"你輸入的數字是{number}")
