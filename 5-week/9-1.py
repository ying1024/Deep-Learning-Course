import tensorflow as tf
#初始数据
x1 = [137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21]
x2 = [3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2]
y = [145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30]
ones = tf.ones(16)
#数据处理
X = tf.stack((ones,x1,x2),axis = 1)
Y = tf.reshape(y,(-1,1))
#计算
xt = tf.transpose(X)
w = tf.linalg.inv(xt @ X) @ xt @ Y

w = tf.reshape(w,(-1,))
#交互
print("房价估计")
m = float(input("请输入20-500之间的房屋面积："))
while(1):
    if m >= 20 and m <= 500:
        print("已输入面积：%f"%(m))
        break
    else:
        m = float(input("输入数据有误！请重新输入："))
num = int(input("请输入1-10的房间数："))
while(1):
    if num >= 1 and num <= 10:
        print("已输入房间数：%d"%(num))
        break
    else:
        num = int(input("输入数据有误！请重新输入："))
res = w[1] * m + w[2] * num + w[0]
print("此房估价为：%f"%(res))
