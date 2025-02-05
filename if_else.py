for_sale=True
if for_sale:
    print("此項目正在出售")
else:
    print("此項目未出售")

age=int(input("請輸入年齡:"))
if age>=100:
    print("年齡太大無法註冊")
elif age>=18:
        print("你可以註冊")
elif age<0:
    print("你還沒出生!")
else:
    print("你必須年滿18歲才能註冊")