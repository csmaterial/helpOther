# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 22:07:11 2018

@author: Administrator
"""

import pandas as pd
import math
address = 'C://Users//Administrator//Desktop//'
temp = pd.read_csv('%snewdata20180727.csv'%address,encoding='gbk') 
temp1 = pd.read_csv('%sall.csv'%address,encoding='gbk') 
sort = pd.read_csv('%s20180728sort.csv'%address,encoding='gbk') 

temp1 = temp1.drop(820)
temp1 = temp1.drop(0)
temp1 = temp1.drop(821)
temp2 = temp1
temp2.index = range(len(temp2))

col1 = temp.columns
col2 = temp2.columns

tl = []
s = sort.columns
for i in s[0:46]:
    if i not in col2:
        print(i)
    else:
        tl.append(i)
'''
tl = [0,1,2,4,7,8,9,10,25,26,28,32,39,45,54,56,57,62,68,69,70,76]
ttl = []
for i in tl:
    ttl.append(col2[i])
'''
t = temp2[tl]
#t = temp2

tcc = list(t.columns)
tc = list(col1)
for i in tc:
    if i not in tcc:
        print(i)
print('----')
for i in tcc:
    if i not in tc:
        print(i)
        
#t.to_csv('%snew7_28.csv'%address,encoding='gbk',index=False)
def deleteNan(num,temp2,col2):
        
    temp2.index = range(len(temp2))
    count=0
    for i in range(len(temp2)):
        try:
            float(temp2[col2[num]][i][0])
        except:
            temp2= temp2.drop(i)
            count+=1
    print(count)
    return temp2

def countNan(num,temp2,col2):
        
    temp2.index = range(len(temp2))
    count=0
    for i in range(len(temp2)):
        try:
            float(temp2[col2[num]][i][0])
        except:
            #temp2= temp2.drop(i)
            count+=1
    print(count)
    return temp2
def fillNan(num,temp2,col2):
    temp2.index = range(len(temp2))
    sumN = 0
    count=0
    for i in range(len(temp2)):
        try:
            #float(temp2[col2[num]][i])
            if math.isnan(float(temp2[col2[num]][i])):
                #print('warning!')
                #print(i)
                #print(num)
                #print(temp2[col2[num]][i])
                1
                #break
            else:
                sumN+=float(temp2[col2[num]][i])
                count+=1
            
            #print(sumN)
        except:
            #print(temp2[col2[num]][i])
            1
    
    tmean = int(sumN/count)      
    print(tmean)
    for i in range(len(temp2)):
        try:
            float(temp2[col2[num]][i])
        except:
            temp2[col2[num]][i]  = tmean
            #print(temp2[col2[num]][i])
    return temp2
print('----')

delL = []
startC=0
for j in range(len(t.columns)-startC):
    num = j+startC
    
    
    #
    if j not in [1,2,5,6,8,9,41]:
        print(t.columns[num])
        #t = countNan(num,t,t.columns)
        t = deleteNan(num,t,t.columns)
        delL.append(j)
    if len(t)<785:
        break
delL+=[5,6,41]
for num in range(44):
    num+=1
    if num not in delL:
        t = fillNan(num,t,t.columns)
        print(num)
        print('-----')

t.to_csv('%snew7_29.csv'%address,encoding='gbk',index=False)
'''
for j in range(4):
    num = j+5
    print(col2[num])
    temp2 = deleteNan(num,temp2,col2)
'''


