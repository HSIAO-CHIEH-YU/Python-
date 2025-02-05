#動物
class Animal:
    aLive=True

    def eat(self):
        print("這個動物正在吃東西")
    def sleep(self):
        print("這個動物正在睡覺")

#兔子
class Rabbit(Animal):
    def Jump(self):
        print("這隻兔子正在跳")
animal=Animal()
rabbit=Rabbit()
#animal.eat(),animal.sleep()
#rabbit.eat(),rabbit.sleep(),rabbit.Jump()#兔子繼承父類別(動物)

class Fish(Animal):
    def swim(self):
        print("魚正在游泳")
class Hawk(Animal):
    def fly(self):
        print("老鷹正在飛")
fish=Fish()
fish.swim()

hawk=Hawk()
hawk.fly()
