
import streamlit as st
import numpy as np
import pandas as pd

import memsql
import MySQLdb 
import sys
import os
import pymysql
import base64
import requests

#AWS RDS Info
#host = 'app-sfa.cilpkhhykq9i.ap-northeast-2.rds.amazonaws.com'
#port = '3306'
#username = "sfaadmin"
#database = "sfa"
#password = "P@ssw0rd1!"

#def connect_RDS(host,port,username,password,database):
#    try:
#        conn = pymysql.connect(host,port=port,user=ursername,passwd=password,db=database,use_unicode=True,
#                              charset ='utf8')
#        cursor = conn.cursor()
#    except:
#        logging.error("RDS에 연결되지 않았습니다")
#        sys.exit(1)
#    return conn,cursor

#singlestore sfa db
import pymysql
connection = pymysql.connect(host='13.124.198.70', user='dbadmin', password='quintet', port = 3306, db = 'sfa')
cursor = connection.cursor()
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
cursor = connection.cursor(pymysql.cursors.DictCursor)

#sql작성
mysql = "select * from T_SERIES"
#mysql = "select * from t_reference"

#sql실행
cursor.execute(query=mysql)

#결과가져오기
result = cursor.fetchall() #또는 result = cursor.fetchone()

df_T_SERIES = pd.DataFrame(result)

df_T_SERIES['ATTRIBUTE_11']=df_T_SERIES.replace('ATTRIBUTE_11','END_DT' - 'START_DT')
