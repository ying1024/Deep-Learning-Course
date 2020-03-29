import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

handnum = tf.keras.datasets.mnist

#加载数据集
(train_x,train_y),(test_x,test_y) = handnum.load_data()

#随机取出16个下标组成一个1*16的新数组
a = np.random.choice(len(test_x),size=16)
#创建画布
plt.figure()
#设置字体
plt.rcParams["font.sans-serif"] = "SimHei"
#设置全局标题
plt.suptitle("MNIST测试集样本",fontsize=20,color="r")

#计数、子图编号
t = 1
#遍历随机取出的数据
for i in a:
    plt.subplot(4,4,(t))
    t = t+1
    plt.axis("off")
    text = "标签值:"+str(test_y[i])
    plt.title(text,fontsize=14)
    plt.imshow(test_x[i])
plt.tight_layout(rect=[0,0,1,0.9])
plt.show()