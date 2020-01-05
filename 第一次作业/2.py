import math
for num in range(0, 19):
	radian = num * 5 # 0 - 90 每隔5
	k = math.radians(radian);
	print ("sin(", radian, "):",'%.2f' % math.sin(k))
	print ("cos(", radian, "):",'%.2f' % math.cos(k))