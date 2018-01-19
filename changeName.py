# -*- coding:utf8 -*-

import os

class BatchRename():
    '''
    批量重命名文件夹中的图片文件

    '''
    def __init__(self):
        self.path = 'C:/Users/49691/Desktop/model/seborrheic'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        print(total_num)
        i = 0
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(i) + '.jpg')
                print(item,i)
                try:
                    os.rename(src, dst)
                    print ("converting %s to %s ..." % (src, dst))
                    i = i + 1
                except:
                    continue
        print ("total %d to rename & converted %d jpgs" % (total_num, i))

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()