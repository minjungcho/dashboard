
import streamlit as st
import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
import requests

base_url = 'http://dh.aks.ac.kr/Encyves/wiki/index.php/조선_세종'
con = requests.get(base_url)
soup = BeautifulSoup(con.content, 'lxml')

infoTable = soup.find("table",{"class":"wikitable sortable"})  #테이블 태그중 클래스가 wikitable sortable인 것만 찾기
infoPrint =[]
for a in infoTable.find_all("tr"):    #wikitable sortable이라는 이름의 테이블에서 모든 tr태그(행)를 반복해서 불러오기
    infolist = []
    for b in a.find_all("td"):        #모든 tr태그(행)마다 모든 td태그(열)을 반복해서 불러오기
        info = b.get_text()           #td 값의 텍스트 추출
        infolist.append(info)         #추출한 텍스트를 리스트에 저장
    infoPrint.append(infolist)
print(infoPrint)


#import streamlit as st
#import numpy as np
#import pandas as pd

#pip install memsql --error
#import memsql
#import MySQLdb 
#import sys
#import os
#import pymysql
#import base64
#import requests

########## dont remove remark ##
##AWS RDS Info
##host = 'app-sfa.cilpkhhykq9i.ap-northeast-2.rds.amazonaws.com'
##port = '3306'
##username = "sfaadmin"
##database = "sfa"
##password = "P@ssw0rd1!"

########## dont remove remark ##
##def connect_RDS(host,port,username,password,database):
##    try:
##        conn = pymysql.connect(host,port=port,user=ursername,passwd=password,db=database,use_unicode=True,
##                              charset ='utf8')
##        cursor = conn.cursor()
##   except:
##        logging.error("RDS에 연결되지 않았습니다")
##       sys.exit(1)
##  return conn,cursor

#singlestore sfa db
#connection = pymysql.connect(host='13.124.198.70', user='dbadmin', password='quintet', port = 3306, db = 'sfa')
#cursor = connection.cursor()
#try:
#    with connection.cursor() as cursor:  
#        sql = "select * from T_OPTY"
#        cursor.execute("set names utf8")
#        cursor.execute(sql)
#        result = cursor.fetchall()
        
#        for i in result:
#            print(i)
#finally:
#    connection.close()

#dict형식의 cursor
#cursor = connection.cursor(pymysql.cursors.DictCursor)

#sql작성
#mysql = "select * from T_SERIES"
#mysql = "select * from t_reference"

#sql실행
#cursor.execute(query=mysql)


#결과가져오기
#result = cursor.fetchall() #또는 result = cursor.fetchone()
#df_T_SERIES = pd.DataFrame(result)
#df_T_SERIES['ATTRIBUTE_11']=df_T_SERIES.replace('ATTRIBUTE_11','END_DT' - 'START_DT')

#st.title('의약품유통업체리스트')

#df = pd.DataFrame({
#  'first column': [1, 2, 3, 4],
#  'second column': [10, 20, 30, 40]
#})


# Line Chart
#chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

#st.line_chart(chart_data)

# Plot a map
#map_data = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#    columns=['lat', 'lon'])

#st.map(map_data)


#if st.checkbox('Show dataframe'):
#    chart_data = pd.DataFrame(
#       np.random.randn(20, 3),
#       columns=['a', 'b', 'c'])

#    st.line_chart(chart_data)

#  Selectbox
# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])
#
# 'You selected: ', option


#  Widget
#option = st.sidebar.selectbox(
#    'Which number do you like best?',
#     df['first column'])

#'You selected:', option

