# 홈

# 필요한 라이브러리
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly.express as px
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta



def run_title(data):
    """ 홈페이지에서 인덱스화면을 표시하는 함수입니다.
    SQLite DB(mydata)에 서울시 실거래가(budongsan2)에 대한 데이터를 불러와 
    인덱스화면을 표시합니다.

    Parameters:
    Returns: 최종적으로 가공한 데이터를 리턴합니다.
    
    """

    # 실거래 현황
    st.subheader("""
    👑실거래 현황 (최신순)
    - *최근 서울시 실거래가 현황입니다!*
    - *※ 매일 오전 09시 이후 데이터 갱신 ※*
    """)
    # run_update()
    if data is None:
        pass 
    else:
        latest = data.loc[1,['CNTRCT_DE']].values[0]
        st.write("기간 : 2022.01.01 ~ " +f'{latest}' + " (계약일 기준)")
        # data = data[data['CNTRCT_DE']>=f'{before_month}']

        # 'FLR_NO' 컬럼에 '층'이란 단어 추가
        data['FLR_NO'] = data['FLR_NO'].astype(str) + '층'
        # 본번, 부번 컬럼 합치기
        cols = ['BOBN', 'BUBN']
        # 본번, 부번 컬럼을 합쳐 '번지'라는 컬럼을 생성 후 
        # 부번이 0아니면 join을 하고 0이면 본번만 나타내는 코드
        data['번지'] = data[cols].apply(lambda row: '-'.join(row.values.astype(str))
                                                if row['BUBN'] != 0
                                                else row['BOBN'], axis=1)

        # 'BLDG_NM' 컬럼에서 아파트, 오피스텔이 있으면 없애주는 코드
        data['BLDG_NM'] = data['BLDG_NM'].str.replace('아파트', '')
        data['BLDG_NM'] = data['BLDG_NM'].str.replace('오피스텔', '')  

        # 순서대로 컬럼을 뽑아 냄
        cols1 = ['SGG_NM', 'BJDONG_NM', '번지', 'BLDG_NM', 'HOUSE_GBN_NM', 'FLR_NO']
        # '주소'라는 컬럼을 만들고 cols1 순서대로 join
        data['주소'] = data[cols1].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
        # 필요없는 컬럼명 빼기 drop
        data = data.drop(['SGG_CD', 'BJDONG_CD', 'SGG_NM', 'BJDONG_NM', 'BOBN', 'BUBN', 'FLR_NO', 'BLDG_NM', '번지', 'HOUSE_GBN_NM'], axis=1)
        # 임대면적을 평수로 반환하는 코드
        data['RENT_AREA'] = data['RENT_AREA'].apply(lambda x: math.trunc(x / 3.3058))
        # 데이터의 컬럼명 변경
        data.columns = ['계약일', '전월세 구분', '임대면적(평)', '보증금(만원)', '임대료(만원)', '건축년도', '주소']
        # 데이터 컬럼을 밑에 순서대로 변경
        data = data[['계약일', '주소', '보증금(만원)', '임대료(만원)', '임대면적(평)', '건축년도', '전월세 구분']]
        # 인덱스 재지정
        data = data.reset_index(drop=True)
        data.index = data.index+1
        
        st.write(data)