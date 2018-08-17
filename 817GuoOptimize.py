# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:57:50 2018

@author: chenc
"""

import numpy as np
import pandas as pd
from datetime import datetime
import math
import random
import time
address = 'C://Users//chenc//Downloads//'
data = pd.read_csv('%snew815.csv'%address)

a = np.array(data['a'])
b = np.array(data['b'])
c = np.array(data['c'])
flag = np.zeros((len(c)))
#标记flag，1为+，-1为-
count = 10
while(count>5):
    count = 0
    for i in range(len(c)):
        flag = 0
        while(flag == 0):
            basic = np.corrcoef(a*c,b)[0,1]
            c[i]+=1
            up = np.corrcoef(a*c,b)[0,1]
            c[i]-=2
            down = np.corrcoef(a*c,b)[0,1]
            c[i]+=1
            
            if up>basic:
                if up>down:
                    c[i]+=1
                    count+=1
            if down>basic:
                if down>up:
                    c[i]-=1
                    count+=1
            if basic>down:
                if basic>up:
                    flag = 1
    
            
            if c[i]>5:
                c[i] = 5
                break
            if c[i]<1:
                c[i] = 1
                break
    print(np.corrcoef(a*c,b)[0,1])
'''
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