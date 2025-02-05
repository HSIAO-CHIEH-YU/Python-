#複利計算機
#公式:總金額=本金*(1+(利率/100))**年限
money=0
rate=0
year=0

money=int(input("請輸入本金:"))
while money<=0:
    print("本金不能小於等於0")
    money = int(input("請輸入本金:"))


rate=int(input("請輸入利率:"))
while rate<=0:
    print("利率不能小於等於0")
    rate = int(input("請輸入利率:"))


year=int(input("請輸入年限:"))
while year<=0:
    print("年限不能小於等於0")
    year = int(input("請輸入年限:"))

print("")
print(f"本金為:{money}")
print(f"利率為:{rate}")
print(f"年限為:{year}")

#公式:總金額=本金*(1+(利率/100))**年限
total=money*(1+(rate/100))**year
print(f"總金額為:{total}")