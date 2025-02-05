happy=True
print(happy:=False)

foods=[]
#while True:
#    food=input("請輸入喜歡的食物:")
#    if food=="q":
#        break
#    foods.append(food)
#print(foods)

#改寫成下面
while (food:=input("請輸入喜歡的食物:"))!="q":
    foods.append(food)
print(foods)

