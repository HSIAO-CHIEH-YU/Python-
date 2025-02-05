name=input("請輸入使用者名稱:")
#print("使用者名稱不能超過12個字元")
#print("使用者名稱不能包含空格")
#print("使用者名稱不能包含數字")
nameLen=len(name)
if nameLen>12:
    print("使用者名稱不能超過12個字元")
elif " " in name:
    print("使用者名稱不能包含空格")
elif not name.isalpha():
    print("使用者名稱不能包含數字")
else:
    print(f"歡迎{name}")