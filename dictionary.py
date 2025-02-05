capital={"US":"DC",
         "JP":"Tokyo",
         "France":"Paris",
         "Russia":"Moscow"}

print(capital.get("JP"))
capital.update({"Germany":"BerLin"})#新增
print(capital)
capital.pop("Germany")#刪除
print(capital)
print(capital.values())#獲得所有的值
print(capital.items())#獲得我有的鍵值對