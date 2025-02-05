#Python異常處理
try:
    x=int(input("請輸入一個整數:"))
    y=int(input("請輸入另一個整數:"))
    print(x/y)
#except ZeroDivisionError:
#    print("除數不能為0")
#except ValueError:
#    print("請輸入整數")
except (ZeroDivisionError,ValueError):
    print("出現錯誤,請重新輸入")
#finally:
#    print("無論正確還是錯誤都會執行")
else:
    print("else")