#def hello(greeting,title,firstName,lastName):
#    print(f"{greeting}, {title}, {firstName}, {lastName}")

#hello("你好","Mr","Apple","蕭")
#hello(greeting="你好",title="Mr",firstName="Apple",lastName="許")

def getPhone(countryCode,areaCode,first,last):
    return f"{countryCode}-{areaCode}-{first}-{last}"

phone=getPhone(countryCode="886",areaCode="09",first="1580",last="6306")
print(phone)