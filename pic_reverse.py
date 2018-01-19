import PIL.Image as img
import os
path_old = "C:/Users/49691/Desktop/数据集/数据集备份/基底细胞癌1/"
path_new = "C:/Users/49691/Desktop/数据集/数据集备份/基底细胞癌4_ud/"
filelist = os.listdir(path_old)
total_num = len(filelist)
print(total_num)
for i in range(total_num):
    im = img.open(path_old + str(i) + ".jpg")
    #ng = im.transpose(img.ROTATE_180) #旋转 180 度角。
    #ng = im.transpose(img.FLIP_LEFT_RIGHT) #左右对换。
    ng = im.transpose(img.FLIP_TOP_BOTTOM)  # 上下对换。
    ng.save(path_new + str(i) +'.jpg')
    if i%20 == 0:
        print(i)
print(i)

#ng = im.rotate(180) #逆时针旋转 45 度角。
#im.transpose(img.FLIP_LEFT_RIGHT) #左右对换。
#im.transpose(img.FLIP_TOP_BOTTOM) #上下对换。
#im.transpose(Image.ROTATE_90) #旋转 90 度角。

#im.transpose(Image.ROTATE_270) #旋转 270 度角。
#im.show()
#ng.show()
