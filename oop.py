class Car:
    def __init__(self,make,modle,year,color):
        self.make=make
        self.modle=modle
        self.year=year
        self.color=color

    def drive(self):
        print(self.modle+"正在行駛")
    def stop(self):
        print(self.modle+"已停止")


car1=Car("BMW","430i",2025,"black")
print(car1.make,car1.modle,car1.year,car1.color)

car1.drive()
car1.stop()