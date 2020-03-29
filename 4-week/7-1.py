import matplotlib.pyplot as plt
from PIL import Image
plt.figure()
plt.rcParams["font.sans-serif"] = "SimHei" #设置字体
plt.suptitle("图像基本操作",fontsize=20,color='b')#全局标题
img = Image.open("lena.tiff")
r,g,b = img.split()

plt.subplot(2,2,1)
plt.title("R-缩放",fontsize=14)
plt.xticks([])
plt.yticks([])
plt.imshow(r.resize((50,50)))

plt.subplot(2,2,2)
tg = g.transpose(Image.FLIP_LEFT_RIGHT)
tg = tg.transpose(Image.ROTATE_270)
plt.title("G-镜像+旋转",fontsize=14)
plt.imshow(tg)

plt.subplot(2,2,3)
cb = b.crop((0,0,150,150))
plt.xticks([])
plt.yticks([])
plt.title("B-裁剪",fontsize=14)
plt.imshow(cb)

plt.subplot(2,2,4)
plt.xticks([])
plt.yticks([])
rgbimg = Image.merge("RGB",[r,g,b])
plt.title(rgbimg.mode,fontsize=14)
plt.imshow(rgbimg)
plt.tight_layout()
rgbimg.save("test.png")
plt.show()