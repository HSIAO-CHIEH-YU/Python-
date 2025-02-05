name="我是魚魚 英文名叫fish"
length=len(name)#全長有幾個字
print(length)
space=name.find(" ")#找第一個空格
print(f"我的第一個空格在第{space}個字元")
phone=input("請輸入電話號碼:")
dash_count=phone.count("-")
print(f"有{dash_count}個-")