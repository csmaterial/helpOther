# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 22:07:11 2018

@author: Administrator
"""

import pandas as pd

address = 'C://Users//Administrator//Desktop//'
temp = pd.read_csv('%snewdata20180727.csv'%address,encoding='gbk') 
temp1 = pd.read_csv('%sall.csv'%address,encoding='gbk') 
temp1 = temp1.drop(820)
temp1 = temp1.drop(0)
temp1 = temp1.drop(821)
temp2 = temp1
temp2.index = range(len(temp2))

col1 = temp.columns
col2 = temp2.columns

tl = [1,2,4,8,9,10,25,26,28,32,39,45,54,56,57,62,68,69,70,76]
ttl = []
for i in tl:
    ttl.append(col2[i])
t = temp2[ttl]

tcc = list(t.columns)
tc = list(col1)
for i in tc:
    if i not in tcc:
        print(i)
print('----')
for i in tcc:
    if i not in tc:
        print(i)
        
t.to_csv('%snew7_28.csv'%address,encoding='gbk',index=False)
def deleteNan(num,temp2,col2):
        
    temp2.index = range(len(temp2))
    count=0
    for i in range(len(temp2)):
        try:
            int(temp2[col2[num]][i])
        except:
            temp2= temp2.drop(i)
            count+=1
            #print(count)
    return temp2
'''
for j in range(4):
    num = j+5
    print(col2[num])
    temp2 = deleteNan(num,temp2,col2)
'''


