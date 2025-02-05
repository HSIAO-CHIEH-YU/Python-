import time
my_time=int(input("請輸入秒數:"))
#正著數
#for x in range(my_time):
#    print(x+1)
#    time.sleep(1)
#print("時間到!!!")
#倒數
#for x in range(my_time,0,-1):
#    print(x)
    #time.sleep(1)
#print("時間到")
#鬧鐘
for x in range(my_time,0,-1):
    sec=x%60
    min=x//60
    print(f"{min:02}:{sec:02}")
    time.sleep(1)
print("時間到")