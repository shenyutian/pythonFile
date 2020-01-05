import matplotlib.pyplot as pb
import matplotlib

k = 3  # 一共三个族群
x = [
    [2, 4, 7, 8, 10, 11, 14, 16, 19, 22, 26, 28, 30, 31, 34, 35, 36, 45, 46, 47, 48, 49, 50, 52, 57, 58, 63, 64, 70, 71,
     73, 74, 75, 83, 84, 85, 87, 88, 89],
    [1, 3, 5, 6, 9, 12, 13, 15, 17, 18, 20, 21, 23, 24, 25, 27, 29, 32, 33, 37, 38, 39, 40, 42, 43, 51, 66, 67, 68, 69,
     76, 81, 82, 86],
    [41, 44, 53, 54, 55, 56, 59, 60, 61, 62, 65, 72, 77, 78, 79, 80, 90]
]
y = [
    [78.75, 82.5, 78.75, 78.25, 87.75, 81.75, 85.25, 83.75, 87.25, 87.75, 81.25, 89, 85.25, 80.25, 85.25, 89, 79.25,
     83.75, 78.25, 79.25, 79.25, 80.25, 84.25, 88.75, 79.25, 77.25, 92.5, 79.25, 81.25, 85.75, 92.5, 94.5, 84.75, 81.75,
     84.25, 81.75, 82.75, 82.25, 87.75],
    [69, 67.5, 75.25, 70.25, 68.25, 65.75, 72.75, 67.25, 69.25, 74.75, 67.25, 71.25, 76.25, 72.25, 71.25, 72.75, 76.25,
     63.75, 73.25, 66.75, 72.25, 76.25, 71.75, 62.5, 73.75, 73.75, 65.75, 68.25, 68.75, 75.75, 62.75, 64, 72.75, 70.25],
    [54, 59.5, 51, 54, 52.25, 52.25, 51.25, 52.25, 50, 50, 58.75, 45, 52.25, 53.75, 43, 45, 53.25]
]
# 把三个族群分别用不同颜色的圆点表示出来
for i in range(k):
    if i == 0:
        pb.plot(x[i], y[i], 'or')
    elif i == 1:
        pb.plot(x[i], y[i], 'ob')
    elif i == 2:
        pb.plot(x[i], y[i], 'og')

# (xa,ya),(xb,yb),(xc,yc)分别表示三个族群的中心点，下面这段代码计算出中心点
nsum = 0
for i in range(len(x[0])):
    nsum += x[0][i]
xa = nsum / len(x[0])

nsum = 0
for i in range(len(x[1])):
    nsum += x[1][i]
xb = nsum / len(x[1])

nsum = 0
for i in range(len(x[2])):
    nsum += x[2][i]
xc = nsum / len(x[2])

nsum = 0
for i in range(len(y[0])):
    nsum += y[0][i]
ya = nsum / len(y[0])

nsum = 0
for i in range(len(y[1])):
    nsum += y[1][i]
yb = nsum / len(y[1])

nsum = 0
for i in range(len(y[2])):
    nsum += y[2][i]
yc = nsum / len(y[2])

xd = []
for x in range(90):
    xd.append(x)
yd = []
for x in range(90):
    yd.append(77)

xe = []
for x in range(90):
    xe.append(x)
ye = []
for x in range(90):
    ye.append(61)
# 用正方形把(xa,ya),(xb,yb),(xc,yc)画出来
pb.plot(xa, ya, 'or', marker="s", markersize=10)
pb.plot(xb, yb, 'ob', marker="s", markersize=10)
pb.plot(xc, yc, 'og', marker="s", markersize=10)
# 应小余同学的要求，给族群画上一条虚线
pb.plot(xd, yd, 'ok', marker='s', markersize=1)
pb.plot(xe, ye, 'ok', marker='s', markersize=1)
# 添加一个图例说明
myfont = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\STXIHEI.TTF")
pb.legend((u'基础级', u'提高级', u'发展级'), loc='best', prop=myfont)
# 在控制台显示图像
pb.show()