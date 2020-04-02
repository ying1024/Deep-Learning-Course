import matplotlib.pyplot as plt
import tensorflow as tf

boston_housing = tf.keras.datasets.boston_housing
(x,y),(test_x,test_y) = boston_housing.load_data(test_split=0)
print("1--CRIM\n2--ZN\n3--INDUS\n4--CHAS\n5--NOX\n6--RM\n7--AGE\n8--DIS\n9--RAD\n10-TAX\n11-PTRATIO\n12-B\n13-LSTAT")
t = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT"]
i = int(input("请输入属性："))
plt.figure()
plt.scatter(x[:,i-1],y)
plt.suptitle(str(i)+"-"+t[i-1])
plt.xlabel(t[i-1])
plt.ylabel("price($1000)")
plt.show()