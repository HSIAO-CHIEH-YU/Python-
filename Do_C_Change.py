#Python溫度轉換
x=float(input("請輸入溫度:"))
y=input("請輸入單位(攝氏C,華式F):").upper()
if y=="C":
    result=x*1.8+32
    new_unit="F"
    print(f"溫度為{round(result,2)}{new_unit}")#4捨5入到小數點後兩位
elif y=="F":
    result=(x-32)*0.5556
    new_unit="C"
    print(f"溫度為{round(result,2)}{new_unit}")#4捨5入到小數點後兩位
else:
    print("單位輸入錯誤")