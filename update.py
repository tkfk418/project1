import requests
import pandas as pd
import streamlit as st
import numpy as np
import csv
import sqlite3
import time
from datetime import datetime

def run_update():
    # DB 접속
    dbConn=sqlite3.connect("data/mydata.db")
    cs=dbConn.cursor()

    # API로 데이터 받아오기
    service_key = '4d42486779706d3034365957634870'
    data = []

    for j in range(1,2):
        url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/{1+((j-1)*1000)}/{j*1000}'
        print(url)
        req = requests.get(url)
        content = req.json()
        con = content['tbLnOpendataRentV']['row']

        for h in con:
            dic = {}
            dic['SGG_CD'] = h['SGG_CD']
            dic['SGG_NM'] = h['SGG_NM']
            dic['BJDONG_CD'] = h['BJDONG_CD']
            dic['BJDONG_NM'] = h['BJDONG_NM']
            dic['BOBN'] = h['BOBN']
            dic['BUBN'] = h['BUBN']
            dic['FLR_NO'] = h['FLR_NO']
            dic['CNTRCT_DE'] = h['CNTRCT_DE']
            dic['RENT_GBN'] = h['RENT_GBN']
            dic['RENT_AREA'] = h['RENT_AREA']
            dic['RENT_GTN'] = h['RENT_GTN']
            dic['RENT_FEE'] = h['RENT_FEE']
            dic['BLDG_NM'] = h['BLDG_NM']
            dic['BUILD_YEAR'] = h['BUILD_YEAR']
            dic['HOUSE_GBN_NM'] = h['HOUSE_GBN_NM']
            data.append(dic)

    # 데이터 전처리
    df = pd.DataFrame(data)
    df['BOBN'].replace('', np.nan, inplace=True)
    df['BUBN'].replace('', np.nan, inplace=True)
    df['BLDG_NM'].replace('', np.nan, inplace=True)
    df['BUILD_YEAR'].replace('', np.nan, inplace=True)
    df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
    df['CNTRCT_DE'] = df['CNTRCT_DE'].apply(lambda x: pd.to_datetime(str(x), format="%Y/%m/%d"))
    df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
    df['CNTRCT_DE'].replace('T00:00:00', '', inplace=True)
    df = df.dropna()
    df['BOBN'] = df['BOBN'].astype('int').astype('str')
    df['BUBN'] = df['BUBN'].astype('int').astype('str')
    df['FLR_NO'] = df['FLR_NO'].astype('int').astype('str')
    df['RENT_AREA'] = df['RENT_AREA'].astype('str') 

    # 데이터 DB 저장
    for row in df.itertuples():
        strSQL="INSERT INTO budongsan2(SGG_CD,SGG_NM,BJDONG_CD,BJDONG_NM,BOBN,BUBN,FLR_NO,CNTRCT_DE,RENT_GBN,RENT_AREA,RENT_GTN,RENT_FEE,BLDG_NM,BUILD_YEAR,HOUSE_GBN_NM)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cs.execute(strSQL,(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]))

    # 중복 데이터 제거
    cs.execute('DELETE FROM budongsan2 WHERE rowid not in (select min(rowid) from budongsan2 group by SGG_CD,SGG_NM,BJDONG_CD,BJDONG_NM,BOBN,BUBN,FLR_NO,CNTRCT_DE,RENT_GBN,RENT_AREA,RENT_GTN,RENT_FEE,BLDG_NM,BUILD_YEAR,HOUSE_GBN_NM)')
    dbConn.commit()

    # DB 접속 종료
    cs.close()
    dbConn.close()

# 전체 데이터 불러오는 함수
def update_data():
    # DB 접속
    dbConn=sqlite3.connect("data/mydata.db")
    cs=dbConn.cursor()

    # 부동산 테이블 조회
    def db_list():
        cs.execute('SELECT * FROM budongsan2 ORDER BY 8 desc')
        bds = cs.fetchall()
        return bds

    # 부동산 테이블 데이터프레임화
    list = db_list()     
    df_bds = pd.DataFrame(list, columns=['SGG_CD','SGG_NM','BJDONG_CD','BJDONG_NM','BOBN','BUBN','FLR_NO','CNTRCT_DE','RENT_GBN','RENT_AREA','RENT_GTN','RENT_FEE','BLDG_NM','BUILD_YEAR','HOUSE_GBN_NM'])     
    df_bds = df_bds.drop(0, axis=0)
    df_bds = df_bds.astype({'RENT_AREA' : 'float'})
    df_bds = df_bds.astype({'FLR_NO' : 'float'})
    df_bds = df_bds.astype({'FLR_NO' : 'int'})

    # DB 접속 종료
    cs.close()
    dbConn.close()
    
    return df_bds

if __name__ == "__main__":
    run_update()
    update_data()
    print("확인")


