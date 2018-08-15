# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 22:42:02 2018

@author: Administrator
"""

import numpy as np
import pandas as pd
from datetime import datetime
import math
import random
import time
address = 'C://Users//Administrator//Desktop//'
data = pd.read_csv('%s1.csv'%(address))

flag = 1
def makeArray(t,num):
    
    tt = np.array(list(t[t.columns[num]]))
    t19 = []
    for i in tt:
        t19.append(int(i))
    t19 = np.array(t19)
    return t19
maxN = 0
time2 = time.time()
maxl = []
zl = []
y2l = []
a = np.array(data['a'])
b = np.array(data['b'])
a[765] = 5
for num in range(1980000000000000000):
    #zo = bin(2**2)
    z = np.random.randint(5,size=784)
    z+=1
        #zo = bin(z-num -1)
        #print(zo)

    
    thre = np.corrcoef(a,b)
    y = a*z
    n =  np.corrcoef(y,b)
    if abs(n[0,1])>maxN:
        maxN = n[0,1]
        print(maxN)
        maxl.append(maxN)
        zl.append(z)
data['a'] = a
data['c'] = zl[len(z)-1]
data.to_csv('%snew815.csv'%address,encoding='gbk',index=False)
'''
   
    t19 = makeArray(t,19)
    t12 = makeArray(t,12)
    y1 = np.corrcoef(xn,t19)
    y2 = np.corrcoef(xn,t12)
    if abs(y1[0,1])-abs(y2[0,1])>maxN:
        maxN = abs(y1[0,1])-abs(y2[0,1])
        m1 = y1[0,1]
        m2 = y2[0,1]
        xA = xn
        print(maxN)
        maxl.append(maxN)
        y1l.append(m1)
        y2l.append(m2)
 '''


       