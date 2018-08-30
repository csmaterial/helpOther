# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 12:27:41 2018

@author: chenc
"""

import pandas as pd
from scipy.cluster import hierarchy  #用于进行层次聚类，话层次聚类图的工具包 
import matplotlib.pyplot as plt
import math
import numpy as np
from pylab import * 
import openpyxl
import warnings
warnings.filterwarnings("ignore")

if __name__=="__main__":
    
    mpl.rcParams['font.sans-serif'] = ['SimHei']  
    #此处为文件名称,文件地址间隔符号为‘/’
    filename = "C:/Users/chenc/Desktop/1.xlsx"
    #此处为文件的sheet名称

 
    wb = openpyxl.load_workbook(filename)
     
    #获取workbook中所有的表格
    sheets = wb.get_sheet_names()
    print(sheets)

    #sheets = ['批发零售贸易业']
    for sheetname in sheets:
        df = pd.read_excel(filename,sheetname = sheetname)
    
        df = df.drop(df.columns[0],axis = 1)
        
        city = df.iloc[0]
        human = df.iloc[1]
    
        human.index= range(len(human))
        city.index= range(len(city))
        
        
        colindex = df.columns[0]
        
        df = df.drop(0,axis = 0)
        df = df.drop(1,axis = 0)
        
        df.index = range(len(df))
        
        c1 = df[colindex]
        for j in range(len(c1)):
            if math.isnan(c1[j]):
                c1[j] = 0
                
        mean = df[colindex]      
        num = 1
        j = 0
        for j in range(df.shape[1]-num):
            try:
                temp = float(human[j+num])
                te = temp*mean
                df[df.columns[j+num]] = te
            except:
                1
            
        df.columns = city
        #获取当前地址
        for i in range(len(filename)):
            j = len(filename) - i-1
            if filename[j] == '/':
                temp = (filename[0:j])
                break    
        df.to_csv('%s/output%s.csv'%(temp,sheetname),encoding = 'gbk',index = False)    
    
        
        
    
    
    
    