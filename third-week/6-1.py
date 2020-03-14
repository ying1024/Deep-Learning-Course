import matplotlib.pyplot as pl

pl.rcParams["font.family"] = "SimHei"#设置中文字体

fig = pl.figure()#绘制画布
x = [137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21]
y = [145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30]
pl.scatter(x,y,color='r')#绘制散点图
pl.suptitle("商品房销售记录",fontsize=16,color='b')#设置全局标题
pl.xlabel("面积(平方米)",fontsize=14)#设置x轴标签
pl.ylabel("价格(万元)",fontsize=14)#设置y轴标签

pl.show()