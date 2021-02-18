#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. 고객리스트


# In[12]:


import csv
import pandas as pd
df2 = pd.read_csv("C:/Users/Quintet/Desktop/data/df_의약품유통업체리스트.csv",sep=",",encoding= "euc-kr")
#df2 = pd.read_csv("C:/Users/Quintet/Desktop/bucket/df_331100_MultipleAccount.csv",sep=",",encoding= "euc-kr")
df2.head()


# In[13]:


#2. 의약품유통고객리스트
df2019 = pd.read_excel("C:/Users/Quintet/Desktop/data/df_의약품유통업체004.xls",sheet_name = "2019")
df01 = df2019[['행 레이블','매출액','영업이익','수익성']] #수익성=당기순이익/매출액*100
df01show = df2019.sort_values("수익성",ascending=False)
df01show.head()


# In[14]:


#pip install quadrant


# In[15]:


import quadrant
import matplotlib.pyplot as plt
import seaborn as sns


# In[18]:


plt.rc('font', family='Malgun Gothic')


# In[29]:


plt.figure(figsize=(5,5))
sns.scatterplot(data=df2019, x='매출액', y='당기순이익')
plt.title(f"수익율 : {abbr['매출액']} vs {abbr['당기순이익']}")
plt.xlabel(abbr['매출액'])
plt.ylabel(abbr['당기순이익'])
          
for i in range(df2019.shape[0]):
          plt.text(df2019.매출액[i], y=df2019.당기순이익[i], s=df2019.수익성[i], alpha=0.8)

plt.show()


# In[42]:


#Quadrant Marker          
plt.text(x=100, y=100, s="4",alpha=10,fontsize=10, color='b')
plt.text(x=100, y=100, s="Q3",alpha=10,fontsize=10, color='b')
plt.text(x=100, y=100, s="Q2", alpha=10,fontsize=10, color='b')
plt.text(x=100, y=100, s="Q1", alpha=10,fontsize=10, color='b')          

# Benchmark Mean values          
plt.axhline(y=df2019.당기순이익.mean(), color='k', linestyle='--', linewidth=1)           
plt.axvline(x=df2019.매출액.mean(), color='k',linestyle='--', linewidth=1) 
          
plt.show()


# In[52]:


# heatmap by pandas
#df2019.style.background_gradient(cmap='magma',low=1)
sns.heatmap( df2019.drop('수익성', axis=1).corr(), annot=True)


# In[ ]:


from pandas import Series,DataFrame


# In[2]:


raw_data_2019 = {
  'year':[2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019],
  'region':['강원','경기','경북','경상','광주','대구','대전','부산','서울',
'인천','전라','전북','제주','충청'],
'numofcomp':[2,35,1,3,6,8,3,9,76,6,2,1,2,2],
'sum_당기순이익':[3121780337,100855974256,1419727864,1693342181,6165075899,
16616386214,27450733744,20717128060,191560285288,7272066952,1960397586, 
416802080,8028811619,2315393020],
'sum_매출액':[132699067946,5373440102889,26383777461,461873669042,484341723089, 
1310103123849,286539820002,1758900471301,11609082844153,763895326147,251256031672, 
25033608291,55816007726,142158473521],
'sum_매출원가':[119795570723,4796318012093,22581378287,433444668480,453275315952, 
1222470140631,285488265121,1637227314482,10751845898597,712260531745,228820596090, 
22398805209,46586576237,133760491952],
'sum_법인세비용':[818684321,53153810422,353355860,571155154,1163246058,3637478334, 
3579247977,6568716738,56329678400,2071462439,554947895,116982500,1942394549,599638011],
'sum_영업외비용':[1157728499,65617783204,195791990,826469457,1823907155, 
4006258295,617428724,9627180831,66638334045,2773587433,1206549511,
158121240,930196045,674922381],
'sum_영업외수익':[217194551,23401341633,3459184,774847666,951783248, 
4583167905,1863788859,10600345677,57005968309,1824969649,1646211085, 
41608394,7192997854,766274836],
'sum_영업이익':[4880998606,195775273989,1965416530,2316119126,6738073142, 
14994815101,29783621586,22376195972,266072899743,10292147175,2075683907, 
650297426,3708404359,2823678576],
'sum_판관비':[8022498617,384254493489,1836982644,26112881436,26973484547, 
74286678502,13538331987,100331209945,634112341229,41342647227,20359751675, 
1984505656,5521027130,5574302993]
}
  
data_2019 = DataFrame(raw_data_2019)
print(data_2019)  


# In[3]:


raw_data_2018 = {
  'year':[2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018],
  'region':['강원','경기','경북','경상','광주','대구','대전','부산','서울',
'인천','전라','전북','제주','충청'],
'numofcomp':[2,35,1,3,6,8,3,9,76,6,2,1,2,2],
'sum_당기순이익':[2056388408,62813618456,369567591,2245541032,6977139639, 
12496974519,20701281659,11265636965,231773598655,8611910036,6591759736, 
548376748,3883204949,1987429403],
'sum_매출액':[119285305577,4944654093169,27376066730,425689545496,499719965634, 
1185960102855,262852814489,1425779582096,10508541624055,665867712801, 
230702440103,20595918415,58188621489,63774445191],
'sum_매출원가':[202205525290,4198709233890,10993178148,385414711979,
417182220529,664232441662,348913737574,741529268922,8771745870886,
1238492733471,508310004787,33961895843,46852231299,128222854256],
'sum_법인세비용':[537311147,19323447369,119747922,513649549,1701817018, 
3247519742,8962855315,3344150860,71126771192,2685667491,1860657376, 
170107047,665796292,621896424],
'sum_영업외비용':[2130864006,30484035748,298675853,814474742,1392897952, 
5047709945,2403140310,10747981263,54844347900,4057963571,2086377282, 
44955324,390901748,168669919],
'sum_영업외수익':[309746222,20672040181,265506622,1220305336,1848764683, 
2394254634,2112989401,2526252141,49531719202,2073872193,1525504665, 
47219733,2591096719,496227789],
'sum_영업이익':[2940157964,87001796679,319693987,2252638816,9185860051, 
15833743788,29085181274,19281573922,318821471722,16717940267,9013289729, 
825875060,2447336435,2693284624],
'sum_판관비':[13475697669,336348373632,4743244901,25860232273,29075842402, 
50559432200,12806599295,40799069826,546488275575,56380462516,25072258873, 
1883468160,6739362525,5822664284]}

data_2018 = DataFrame(raw_data_2018)
print(data_2018)  


# In[4]:


#import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']
import numpy as np
import pandas as pd
import matplotlib.font_manager as fm
font_name = fm.FontProperties(fname = 'C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family = font_name)
matplotlib.rcParams['axes.unicode_minus'] = False


# In[21]:


plt.plot(data_2019["region"],data_2019["numofcomp"],'o',color='red',alpha=.5)
plt.title('2019지역별기업분포수',fontsize=14)
plt.xlabel("region",fontsize=12)
plt.ylabel("number of company",fontsize=12)
plt.show()


# In[6]:


plt.figure(figsize=(7,5))
plt.scatter(data_2018["region"],data_2018["numofcomp"],c=data_2018["numofcomp"],cmap='coolwarm',alpha=.5)
plt.title('2018지역별기업분포수',fontsize=14)
plt.xlabel("region",fontsize=12)
plt.ylabel("number of company",fontsize=12)
plt.grid()
plt.colorbar()
plt.show()


# In[7]:


#pie차트
from matplotlib import font_manager,rc
from matplotlib import style
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')


# In[8]:


plt.pie(data_2018.sum_매출액, labels=data_2018.region,autopct='%1.1f%%',shadow=True, startangle=90)
plt.show()


# In[23]:


#macro
#table = pd.pivot_table(data=df2,index=['종업원수','2020년매출액'])
#table


# In[ ]:


#pip uninstall requests
#memsql.py


# In[ ]:


import memsql
import MySQLdb 
import sys
import os
import pymysql
import base64
import requests


# In[ ]:


#AWS RDS Info
host = 'app-sfa.cilpkhhykq9i.ap-northeast-2.rds.amazonaws.com'
port = '3306'
username = "sfaadmin"
database = "sfa"
password = "P@ssw0rd1!"

def connect_RDS(host,port,username,password,database):
    try:
        conn = pymysql.connect(host,port=port,user=ursername,passwd=password,db=database,use_unicode=True,
                              charset ='utf8')
        cursor = conn.cursor()
    except:
        logging.error("RDS에 연결되지 않았습니다")
        sys.exit(1)
    return conn,cursor

