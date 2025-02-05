#*args任意數量參數 ->元組
#**kwargs -> 字典

#def add(a,b):
#    return a+b
#print(add(2,3)

#def add(*args):
#    total=0
#    for arg in args:
#        print(f"args:{arg}")
#        total+=arg
#    return total
#print(add(1,2,3))

def printInfo(**kwargs):
    for key,value in kwargs.items():
        print(f"key:{key}value:{value}")
printInfo(name="蕭頡榆",age="22",work="工程師")

