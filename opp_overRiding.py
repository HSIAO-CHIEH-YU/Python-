class Animal:
    def eat(self):
        print("動物正在吃東西")
#class Rabbit(Animal):
#    def eat(self):
#        print("兔子正在吃紅蘿蔔")

#animal=Animal()
#animal.eat()
#rabbit=Rabbit()
#rabbit.eat()

#-------------------------------------------
#哺乳類
class Mammal(Animal):
    def hi(self):
        print("我是哺乳類")
    pass
#貓
class Cat(Mammal):
    def eat(self):
        print("小貓正在吃魚")
#狗
class Dog(Mammal):
    def eat(self):
        print("小狗正在啃骨頭")

cat=Cat()
cat.eat()
dog=Dog()
dog.eat()
m=Mammal()
m.eat()
