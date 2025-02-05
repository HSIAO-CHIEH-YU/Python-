import os
str=r"C:\Users\user\Desktop\workSpace\test.txt" #加上r才能顯示出來 或是每一個\都要變\\
#print(str)
if os.path.exists(str):
    print("路徑存在")
    if os.path.isfile(str):
        print("路徑是檔案")
    elif os.path.isdir(str):
        print("路徑是目錄")
else:
    print("不存在")