import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

bsdh = tf.keras.datasets.boston_housing

(train_x,train_y),(test_x,test_y) = bsdh.load_data()

# print(train_x[:,-1])
# print(train_y)

x = train_x[:,-1].astype(np.float32)
y = train_y.astype(np.float32)


training_epochs = 50
learnint_rate = 0.001

w = tf.Variable(1.0)
b = tf.Variable(1.0)

plt.figure()
loss_list = []
for i in range(training_epochs):
    loss = tf.reduce_mean(tf.square(x*w+b-y))
    loss_list.append(loss)
    dw = tf.reduce_mean(x*(x*w+b-y))
    db = tf.reduce_mean(x*w+b-y)
    w.assign(dw*learnint_rate)
    b.assign(db*learnint_rate)
    plt.plot(x,x*w+b)
# plt.plot(loss_list)
print(loss_list)
print("-"*10)
print(w,b)
plt.show()