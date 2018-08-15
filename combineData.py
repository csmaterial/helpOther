# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 08:36:16 2018

@author: chenc
"""
import numpy as np
import pandas as pd
from datetime import datetime
import math

import warnings
warnings.filterwarnings("ignore")

#取出日期区间内的数据
def getIndex(datatemp,startyear,startmonth,endyear,endmonth):
        
    colname = '日期_Date'
    startIn = 0
    endIn = 0
    flag = 0
    for i in range(len(datatemp)):
        if flag ==0:
            if startyear+'-' +startmonth==datatemp[colname][i][0:7]:
                flag = 1
                startIn = i
        if flag == 1:
            if endyear+'-' +endmonth==datatemp[colname][i][0:7]:
                endIn = i
    te = datatemp.loc[startIn:endIn]
    return te

def getDataL(startyear,startmonth,address,filenum):

    endmonth = int(startmonth) + 0
    if(endmonth)>12:
        endmonth -= 12
        endyear = str(int(startyear)+1)
    else:
        endyear = startyear
    if endmonth<10:
        endmonth = '0' + str(endmonth)
    else:
        endmonth = str(endmonth)
    #print(endmonth)
    #print(endyear)
    
    dataL = []
    
    #第一个文件，1.csv，无需合并
    
    num = 1
    data = pd.read_csv('%s%s.csv'%(address,num),encoding='gbk')
    #去掉有不少于thresh个Nan的列
    data = data.dropna(axis=1,thresh=len(data)/2)
    
    col = data.columns

    m = data.groupby(col[0])    
    
    for i in m:
        temp = i
        datatemp = temp[1]
        datatemp.index = range(len(datatemp))
        
        #判断该区间内是否为ST
        if datatemp.iloc[0][col[1]] == 'Norm':
            targetData = (getIndex(datatemp,startyear,startmonth,endyear,endmonth))
            try:
                if targetData.iloc[len(targetData)-1][col[1]] == 'Norm':
                    targetData = targetData.dropna(axis=1,thresh=len(targetData)/2)
                    dataL.append(targetData)
                    
                #targetData = targetData.dropna(axis=1,thresh=len(data)/2)
        #
        #
            except:
                1
    #print(len(dataL))
    #第2-35个文件，合并及读取
    for num in range(filenum):
        
        num +=1
        data = pd.read_csv('%s%s.csv'%(address,num),encoding='gbk')
        if dataL[len(dataL)-1][col[0]].iloc[0] == data[col[0]][0]:
            data = dataL[len(dataL)-1].append(data)
        
        #去掉有不少于thresh个Nan的列
        data = data.dropna(axis=1,thresh=len(data)/2)

    
        m = data.groupby(col[0])    
        
        for i in m:
            temp = i
            datatemp = temp[1]
            datatemp.index = range(len(datatemp))
            
            #判断该区间内是否为ST
            if datatemp.iloc[0][col[1]] == 'Norm':
                targetData = (getIndex(datatemp,startyear,startmonth,endyear,endmonth))
                try:
                    if targetData.iloc[len(targetData)-1][col[1]] == 'Norm':
                        targetData = targetData.dropna(axis=1,thresh=len(targetData)/2)
                        dataL.append(targetData)
                        
                    #targetData = targetData.dropna(axis=1,thresh=len(targetData)/2)
                except:
                    1
        #print(len(dataL))
    return dataL

def getRightList(dataL):
        
    #删去行列数没有达到均值的一半的样本
    dataR = []
    row = 0
    col = 0
    for i in dataL:
        row += i.shape[0]
        col += i.shape[1]
    row = int(row/len(dataL))
    col = int(col/len(dataL))
    
    for i in dataL:
        if i.shape[0] >= row/2:
            if i.shape[1] > col/2:                  
                dataR.append(i)
    list1 = list(dataR[0].columns)                  
    return (dataR,list1)
#填充DataFrame所有startnum以后的列的Nan
def fillDF(te,startnum):
    
    col = te.columns
    for num in range(len(col)-startnum):
        num+=startnum
        temp = te[col[num]]
        before = temp.iloc[0]
        
        if math.isnan(before):
            return 0
        else:
            for i in range(len(temp)-1):
                i+=1
                
                if math.isnan(temp.iloc[i]):
                    temp.iloc[i] = before
                else:
                    before = temp.iloc[i]
        
    return te
def fillSome(l2,data):
    
    for num in range(len(l2)):
        temp = data[l2[num]]
        before = temp.iloc[0]
        for i in range(len(temp)-1):
            i+=1
            
            if math.isnan(temp.iloc[i]):
                temp.iloc[i] = before
            else:
                before = temp.iloc[i]
    return data
#填充DataFrame所有startnum以后的列的倒数rownum行的Nan
def fillDFrow(te,startnum,rownum):
    
    col = te.columns
    for num in range(len(col)-startnum):
        num+=startnum
        temp = te[col[num]]
        before = temp.iloc[0]
        
        if math.isnan(before):
            return 0
        else:
            for i in range(rownum):
                i = len(temp)-rownum+i
                
                if math.isnan(temp.iloc[i]):
                    temp.iloc[i] = before
                else:
                    before = temp.iloc[i]
        
    return te

def fillColAll(dataR,list1):
    
    dataT = []
    for inum in range(len(dataR)):
        
        i = dataR[inum]
        i = i[list1]
        i1 = fillDF(i,3)
        dataT.append(i1)
        #print(inum)
    return dataT
#第code行的倒数X日内的幅度变化
def X_day(i1,code,X):

    day20 = i1[code].iloc[len(i1)-1]
    day10 = i1[code].iloc[len(i1)-1-X]
    per = (day20-day10)/day10
    return per
def fillColRow(dataR,list1):
                
    dataT = []
    for inum in range(len(dataR)):
        
        i = dataR[inum]
        try:
            i = i[list1]
            flag = 1
        except:
            flag = 0
            #l2列的填充满
        if flag == 1:
            
            l2 = ['收盘价_Clpr',  '日振幅(%)_Dampltd','流通股日换手率(%)_DTrdTurnR']
            i = fillSome(l2,i)
            i1 = fillDFrow(i,3,3)
            try:
                i1['月均振幅'] = i1['日振幅(%)_Dampltd'].mean()
                flag = 1
            except:
                flag = 0
                    
            if flag ==1:
                
                i1['月均换手率'] = i1['流通股日换手率(%)_DTrdTurnR'].mean()
        
                code = '流通股日换手率(%)_DTrdTurnR'
                i1['5日换手率'] = X_day(i1,code,5)
                i1['10日换手率'] = X_day(i1,code,10)
                i1['本月换手率'] = X_day(i1,code,len(i1)-1)
                code = '收盘价_Clpr'
                i1['5日涨幅'] = X_day(i1,code,5)
                i1['10日涨幅'] = X_day(i1,code,10)
                i1['本月涨幅'] = X_day(i1,code,len(i1)-1)
                
                
                dataT.append(i1)
    return dataT

def getData(dataT,rownum,list1):
    flag = 1
    l = []
    for i in dataT:
        if type(i) !=type(0):
            if flag == 1:
                temp = i[list1].iloc[0:0]
                flag =0
            else:
                code = i['股票代码_Stkcd'].iloc[0]
                if code not in l:
                    l.append(code)
                    temp = temp.append(i.iloc[rownum:rownum+1])
    return temp

def getlastData(dataT,list1):
    flag = 1
    l = []
    for i in dataT:
        if type(i) !=type(0):
            if flag == 1:
                temp = i[list1].iloc[0:0]
                flag =0
            else:
                rownum = len(i)-1
                code = i['股票代码_Stkcd'].iloc[0]
                if code not in l:
                    l.append(code)
                    temp = temp.append(i.iloc[rownum:rownum+1])
    return temp
def combine(startyear,startmonth,address):
    dataL = getDataL(startyear,startmonth,address)
    (dataR,list1) = getRightList(dataL)
    dataT = fillColAll(dataR,list1)
    #
    #list1.remove(list1[len(list1)-2])
    #rowl = [0,10,11]
    rowl = [0]
    for rownum in rowl:
        temp = getData(dataT,rownum,list1)
        temp.to_csv('%s%s-%sday%s.csv'%(address,startyear,startmonth,rownum),index = False)

    temp = getlastData(dataT,list1)
    temp.to_csv('%s%s-%sdayLast.csv'%(address,startyear,startmonth),index = False)
    return temp

def getEnd(startmonth,startyear,month):
        
    endmonth = int(startmonth) + month
    if(endmonth)>12:
        endmonth -= 12
        endyear = str(int(startyear)+1)
    else:
        endyear = startyear
    if endmonth<10:
        endmonth = '0' + str(endmonth)
    else:
        endmonth = str(endmonth)
    return (endmonth,endyear)

if __name__=="__main__":
    startyear = '2015'
    startmonth = '12' 
    #dataL = getDataL(startyear,startmonth)
    
    address = 'D://quant//JS_Fund//16-18//'
    tempList = ['股票代码_Stkcd','总股数_Fullshr','收盘价_Clpr',  '日振幅(%)_Dampltd','流通股日换手率(%)_DTrdTurnR','市盈率_PE', '市净率_PB', '市现率_PCF',
       '市销率_PS', '每股收益(摊薄)(元/股)_EPS', '净资产收益率(摊薄)_ROE',
       '每股公积金(元/股)_AccumFundPS', '每股营业利润(元/股)_OpPrfPS', '每股净资产(元/股)_NAPS',
       '每股营业收入_IncomePS', '每股经营活动现金流量净额(元/股)_NCFfropePS']
    l1 = ['月均振幅','月均换手率','5日换手率','10日换手率','本月换手率','5日涨幅','10日涨幅','本月涨幅']
    filenum = 32
    for i in range(1):
        (startmonth,startyear) = getEnd(startmonth,startyear,1)
        print('month is %s-%s'%(startmonth,startyear))
        #temp = combine(startyear,startmonth,address)
        dataL = getDataL(startyear,startmonth,address,filenum)
        dataL[0][tempList]
        (dataR,list1) = getRightList(dataL)
        dataT = fillColRow(dataR,tempList)
        
        #dataT = fillColAll(dataR,list1)
        #
        #list1.remove(list1[len(list1)-2])
        
        new = tempList+l1
        #rowl = [0,10,11]
        rowl = [0]
        for rownum in rowl:
            temp = getData(dataT,rownum,new)
            #temp.to_csv('%s%s-%sday%s.csv'%(address,startyear,startmonth,rownum),index = False)
        '''
        temp1 = getlastData(dataT,new)
        temp1.to_csv('%s%s-%sdayLast.csv'%(address,startyear,startmonth),index = False)
        '''

