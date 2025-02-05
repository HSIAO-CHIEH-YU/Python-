row=int(input("請輸入行數:"))
cols=int(input("請輸入列數:"))
symbol=input("請輸入符號:")

for x in range(row):
    for y in range(cols):
        print(symbol,end=" ")
    print("")