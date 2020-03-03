a = float(input("请输入a的值"))
b = float(input("请输入b的值"))
c = float(input("请输入c的值"))
t = b ** 2 - 4*a*c
if t < 0:
    print("此方程无解")
else:
    x1 = (-b + t ** 0.5)/2/a
    x2 = (-b - t ** 0.5)/2/a
    print("次方程的解为：x1 = %0.2f，x2 = %0.2f"%(x1,x2))