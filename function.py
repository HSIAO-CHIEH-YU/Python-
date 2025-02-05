#def say_hello():
#    print("Hello, World!")
#say_hello()  # 呼叫函式，會輸出 "Hello, World!"

#def greeting(name):
#    print(f"你好{name}")
#greeting("魚魚")

#def add(x,y):
#    return x+y
#result=add(3,4)
#print(result )

def creat_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last

print(creat_name("john","wick"))