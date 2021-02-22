pip install WordCloud
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create some sample text
text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()


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

