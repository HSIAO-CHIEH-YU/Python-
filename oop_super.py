class Rectengle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        print("矩形初始化已執行")
class Square(Rectengle):
    def __init__(self,legth,width):
        super().__init__(legth,width)#用super來簡化避免重
#複寫一樣的東西
        print("正方形初始化已執行")

square=Square(500,1000)

class Cube(Rectengle):#長*寬*高
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height
        print(f"立方體的長寬高是{length},{width},{height}")

cube=Cube(100,200,300)