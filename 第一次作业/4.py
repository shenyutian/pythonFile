strs = input("输入一个大写字母:")
num = ord(strs)
n = num - 65
k = 2*(num - 65) + 1
for i in range(65, num+1):
	m = i - n
	for j in range(0, k):
		# 大于 等于 A  显示
		if(m >= 65):
			print (chr(m), end='')
		else:
			print(' ',end='')
		# 判断到达中间值  前加  后减
		if(j+66 > num):
			m = m-1
		else:
			m = m+1
		#换行用的
		if( j == k-1 ):
			print()