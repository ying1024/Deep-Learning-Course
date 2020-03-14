import numpy as np
x = np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y = np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
w = np.sum((x - np.sum(x)/len(x)) * (y-np.sum(y)/len(y)))/np.sum((x - np.sum(x)/len(x)) ** 2)
b = np.sum(y)/len(y) - w * (np.sum(x)/len(x))
print("w=%f,b=%f"%(w,b))