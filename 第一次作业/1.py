import math
r = float(input("输入球形半径r："))
icon = 7.86 #铁的比重7.86
gold = 19.3	#金的比重19.3
print ()
print ("铁球：",4*math.pi*math.pow(r, 3)*icon/3)
print ("金球：",4*math.pi*math.pow(r, 3)*gold/3)