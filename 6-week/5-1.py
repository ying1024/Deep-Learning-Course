import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# logdir = "G:/course/dasanxia/sj/log"
# summary_writer = tf.summary.create_file_writer(logdir)

x_data = np.linspace(0,100,500)

y_data = 3.1234 * x_data + 2.98
y_rdata = 3.1234 * x_data + 2.98 + np.random.randn(*y_data.shape) * 20
# print(y_rdata)
plt.figure()
def model(x,w,b):
    return tf.multiply(x,w) + b
w = tf.Variable(10.0,tf.float32)
b = tf.Variable(0.0,tf.float32)

def loss(x,y,w,b):
    err = model(x,w,b) - y
    squared_err = tf.square(err)
    return tf.reduce_mean(squared_err)

training_epochs =  10
learning_rate = 0.0000001

def grad(x,y,w,b):
    with tf.GradientTape() as tape:
        loss_ = loss(x,y,w,b)
    return tape.gradient(loss_,[w,b])
step = 0
loss_list = []
display_step = 20

for epoch in range(training_epochs):
    for xs,ys in zip(x_data,y_rdata):
        loss_ = loss(xs,ys,w,b)
        loss_list.append(loss_)

        delta_w,delta_b = grad(xs,ys,w,b)
        change_w = delta_w * learning_rate
        change_b = delta_b * learning_rate
        w.assign_sub(change_w)
        b.assign_sub(change_b)
        step = step + 1
        # with summary_writer.as_default():
        #     tf.summary.scalar("loss epoch: "+str(epoch), loss_.numpy(), step = step)
        # if step % display_step == 0:
        #     print("step:%3d" %(step),"loss:%f"%(loss_list[step-1]))
    # print(w,b)
    plt.plot(x_data,w.numpy() * x_data + b.numpy())

plt.plot(x_data,y_data,'#000')
print(5.79 * w.numpy() + b.numpy())
# plt.scatter(x_data,y_rdata)
plt.show()


# writer.close()