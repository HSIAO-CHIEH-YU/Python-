cart=[]
menu={"披薩":"300",
    "爆米花":"200",
    "薯條":"90",
    "洋芋片":"60",
    "麵包條":"120",
    "蘇打水":"60",
    "檸檬水":"90"
      }
total=0
print("菜單")
print("------------")
for item,price in menu.items():
    print(f"{item}:{price}")
while True:
    food=input("請輸入想吃什麼(輸入q結束):")
    if food.lower()=="q":
        break
    elif menu.get(food) is None:
        print("沒有這個商品")
    else:
        cart.append(food)
        total+=int(menu.get(food))
        #print(food,end="")
print(f"總共{total}元")