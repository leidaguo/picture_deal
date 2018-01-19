# -*- coding:utf8 -*-

import os
import shutil
import numpy as np
import pandas as pd
path_img='C:/Users/49691/Desktop/数据集/test'
ls = os.listdir(path_img)
lenl=len(ls)
print(len(ls))


train_labels = pd.read_csv('C:/Users/49691/Desktop/数据集/b.csv')
train_labels.head()
labels = train_labels.invasive.values
name = train_labels.name.values
print(train_labels.shape,train_labels.shape[0],labels,name)

for i in range(lenl):
    #if i.find('testnan')!=-1:
    shutil.move(path_img+'/'+str(i) + ".jpg","C:/Users/49691/Desktop/数据集/test1/"+ str(name[i]) +".jpg")
    print(i,name[i])