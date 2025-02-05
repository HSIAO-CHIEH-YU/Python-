x=float(input("請輸入溫度:"))
if x>0 and x<30:
    print("溫度適宜")
else:
    print("溫度不適宜")

if x<0 or x>=30:
    print("溫度不適宜")
else:
    print("溫度適宜")