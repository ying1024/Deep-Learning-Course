import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


bsdh = tf.keras.datasets.boston_housing

(x,y),(test_x,test_y) = bsdh.load_data()

x = x.astype(np.float32)
y = y.astype(np.float32)

for i in range(13):
    x[:,i] = (x[:,i]-np.min(x[:,i]))/(np.max(x[:,i])-np.min(x[:,i]))

def model(x,w,b):
    return tf.matmul(x,w) + b

w = tf.Variable(tf.random.normal([13,1],mean=0,stddev=1.0,dtype=tf.float32))
b = tf.Variable(tf.zeros(1),dtype=tf.float32)

training_epochs = 50 #迭代次数
learning_rate = 0.001 #学习率
batch_size = 10 #批量训练一次的样本数

def loss(x,y,w,b):
    err = model(x,w,b) - y
    squared_err = tf.square(err)
    return tf.reduce_mean(squared_err)

def grad(x,y,w,b):
    with tf.GradientTape() as tape:
        loss_ = loss(x,y,w,b)
    return tape.gradient(loss_,[w,b])

optimizer = tf.keras.optimizers.SGD(learning_rate)

loss_list = []
total_step = int(len(y)/batch_size)

x1 = x.astype(np.float32)
print(tf.matmul(x1,w))

for epoch in range(training_epochs):
    for step in range(total_step):
        xs = x[step*batch_size:(step+1)*batch_size,:]
        ys = y[step*batch_size:(step+1)*batch_size]

        grads = grad(xs,ys,w,b)
        optimizer.apply_gradients(zip(grads,[w,b]))
    loss_train = loss(x,y,w,b).numpy()
    loss_list.append(loss_train)
    print("epoch={:3d},train_loss={:.4f}".format(epoch+1,loss_train))
print("w:",w)
print("b:",b)

plt.figure()
plt.rcParams["font.sans-serif"]="SimHei"
plt.plot(loss_list,label="loss")
plt.legend()
plt.suptitle("迭代次数:"+str(training_epochs)+" 学习率:"+str(learning_rate))
plt.show()
