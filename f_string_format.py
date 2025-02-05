price1=3.321
price2=-77
price3=15.11

#小數點的精確度
print(f"價格1為{price1:.2f}\n"#取小數點後兩位
      f"價格2為{price2:.2f}\n"
      f"價格3為{price3:.2f}")
print("")
#在數字錢加上+ -符號
print(f"價格1為{price1:+.2f}\n"#取小數點後兩位並且加上+-符號
      f"價格2為{price2:+.2f}\n"
      f"價格3為{price3:+.2f}")
print("")
#對齊 < > ^
print(f"價格1為{price1:<10.2f}\n"#對齊左邊
      f"價格2為{price2:>10.2f}\n"#對齊右邊
      f"價格3為{price3:^10.2f}")#至中對齊
print("")
#混合符號
print(f"價格1為{price1:>+.2f}\n"#取小數點後兩位
      f"價格2為{price2:>+.2f}\n"
      f"價格3為{price3:>+.2f}")