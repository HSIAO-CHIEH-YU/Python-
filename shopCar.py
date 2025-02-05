goods=[]
prices=[]

while True:
    good=input("請輸入想要購買的物品:")
    if good.lower()=="q":
        break
    price=float(input(f"請輸入{good}的價格:"))
    goods.append(good)
    prices.append(price)
print(f"商品列表:{goods}")
print(f"價格列表:{prices}")
for index,good in enumerate(goods):
    print(f"第{index+1}個物品{good}的售價為{prices[index]}")
total=sum(prices)
print(f"總價格為{total}元")