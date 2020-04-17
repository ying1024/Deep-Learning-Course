import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

bsdh = tf.keras.datasets.boston_housing
#加载数据
(train_x,train_y),(test_x,test_y) = bsdh.load_data()

#训练集数据处理
ones = np.ones((len(train_x),1),dtype=np.float32)
x = (train_x-test_x.min(axis=0))/(train_x.max(axis=0)-train_x.min(axis=0))
x = tf.cast(tf.concat([ones,x],axis=1),dtype=tf.float32)
y = tf.constant(train_y.reshape(-1,1),dtype=tf.float32)

#测试集数据处理
tx = (test_x-test_x.min(axis=0))/(test_x.max(axis=0)-test_x.min(axis=0))
ones2 = np.ones((len(test_x),1),dtype=np.float32)
tx = tf.cast(tf.concat([ones2,tx],axis=1),dtype=tf.float32)
ty = tf.constant(test_y.reshape(-1,1),dtype=tf.float32)

# 定义变量
w = tf.Variable(np.random.randn(len(x[0]),1),dtype=tf.float32)

# 设置参数
training = 2500
learning = 0.01
loss_list = []
loss_list2 = []

#训练
for i in range(training):
    with tf.GradientTape() as tape:
        pred_train = tf.matmul(x,w)
        loss = tf.reduce_mean(tf.square(pred_train-y))

    pred_test = tf.matmul(tx,w)
    loss2 = tf.reduce_mean(tf.square(pred_test-ty))
    loss_list.append(loss)
    loss_list2.append(loss2)
    dw = tape.gradient(loss,w)
    w.assign_sub(learning*dw)
    #print("step:%d,loss:%f" %(i+1,loss))

#画图
plt.figure(figsize=(10,8))

plt.subplot(311)
plt.title("loss")
plt.plot(loss_list,'b',label="train")
plt.plot(loss_list2,'r',label="test")
plt.legend()

plt.subplot(312)
plt.title("pred_train right")
plt.plot(pred_train,'b',label="pred")
plt.plot(y,'r',label="right")
plt.legend()

plt.subplot(313)
plt.title("pred_test right")
plt.plot(pred_test,'b',label="pred")
plt.plot(ty,'r',label="right")
plt.legend()

plt.tight_layout()
plt.show()