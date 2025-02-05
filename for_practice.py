#for x in range(1,11):#印出1~10
#    print(x)
#print("")

#for x in reversed(range(1,11)):#印出10~1
#    print(x)
#print("")

#credit_card="1234-5678-9012-3456"
#for x in credit_card:
#    if x=="9":
        #continue跳過9繼續 #break遇到9就停止迴圈
#    print(x)

my_dict={"a":1,"b":2,"c":3}
#for x in my_dict:
#    print(x)
for key,value in my_dict.items():
    print(f"key:{key}")
    print(f"value:{value}")