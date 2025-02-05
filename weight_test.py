#體重轉換器
weight=float(input("請輸入體重:"))
x=input("請輸入單位(kg公斤 or lb磅):").upper()
if x=="KG":
    result=weight*2.20
    new_unit="磅"
elif x=="LB":
    result=weight/2.20
    new_unit="公斤"
else:
    print("單位或格式錯誤")
    exit()

print(f"你的體重是{round(result)}{new_unit}")#round 4捨5入