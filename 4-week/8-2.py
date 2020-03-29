import tensorflow as tf

x = [64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
y = [62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]

tfx = tf.constant(x)
tfy = tf.constant(y)

w = (len(tfx) * tf.reduce_sum(tfx * tfy) - tf.reduce_sum(tfx) * tf.reduce_sum(tfy))/(len(tfx) * tf.reduce_sum(tfx ** 2)-(tf.reduce_sum(tfx) ** 2))

b = (tf.reduce_sum(tfy) - w * tf.reduce_sum(tfx))/len(tfx)

print(w)
print(b)
