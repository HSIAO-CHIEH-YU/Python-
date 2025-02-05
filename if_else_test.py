#Python計算機程式
x=float(input("請輸入第一個數字:"))
y=float(input("請輸入第二個數字:"))
z=input("請輸入 加(+),減(-),乘(*),除(/):")
if z=="+":
   result=x+y
elif z=="-":
    result=x-y
elif z=="*":
    result=x*y
elif z=="/":
    result=x/y
else:
    print("輸入格式錯誤")
print(f"運算結果是{result}")