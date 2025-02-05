try:
    str=r"C:\Users\user\Desktop\workSpace\test.txt"
    with open(str) as file:
        print(file.read())
except FileNotFoundError:
    print("檔案不存在")