import math
#次方
print(pow(5,2))#5的2次方
print(5**2)#也能這樣寫
#最大值Max,最小值Min
x=1
y=2
z=3
print (max(x,y,z))
print(min(x,y,z))
#4捨5入
a=3.14
b=3.5
print(round(a))
print(round(b))
#絕對值
c=-20
print(abs(c))
#無條件進位,#無條件捨去
d=9.5
print(math.ceil(d))#無條件進位
print(math.floor(d))#無條件捨去

print(math.pi)#圓周率

#圓周長
r=5
circle=2*math.pi*r
print(round(circle))
#園面積
circle=(r**2)*math.pi
print(round(circle))