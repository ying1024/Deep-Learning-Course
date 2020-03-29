import numpy as np
np.random.seed(612)
a = np.random.rand(1000)
x = int(input("请输入一个1-100的整数："))
t = 1
print("序号","索引值","随机数")
for i in range(len(a)):
    if (i % x) == 0:
        print(t,i,a[i])
        t=t+1
