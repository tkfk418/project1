# 홈

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import math

st.title('내 방 어디?')

from search import run_search
from predict import run_predict
from suggestions import run_suggestions

selected3 = option_menu(None, ["🏠Home", "🔎전월세 검색",  "📊전세 예측", '💬건의사항'], 
    # icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#47C83E"},
    }
)

# 홈 탭
if selected3 == "🏠Home":
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    data2 = data.copy()
    po = data2['SGG_NM'] == '영등포구'
    tel = data2['HOUSE_GBN_NM'] == '아파트'
    st.write(data2[po & tel]['BOBN'].count())


    # 실거래 현황
    st.subheader('실거래 현황 (최신순)')
    st.write('기간 : 2022.01.01~ 2023.01.30 (계약일 기준)')

    data['FLR_NO'] = data['FLR_NO'].astype(str) + '층'
    cols = ['BOBN', 'BUBN']
    data['번지'] = data[cols].apply(lambda row: '-'.join(row.values.astype(str))
                                            if row['BUBN'] != 0
                                            else row['BOBN'], axis=1)
    data['BLDG_NM'] = data['BLDG_NM'].str.replace('아파트', '')
    data['BLDG_NM'] = data['BLDG_NM'].str.replace('오피스텔', '')                             
    cols1 = ['SGG_NM', 'BJDONG_NM', '번지', 'BLDG_NM', 'HOUSE_GBN_NM', 'FLR_NO']
    data['주소'] = data[cols1].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
    data = data.drop(['SGG_CD', 'BJDONG_CD', 'SGG_NM', 'BJDONG_NM', 'BOBN', 'BUBN', 'FLR_NO', 'BLDG_NM', '번지', 'HOUSE_GBN_NM'], axis=1)
    data['RENT_AREA'] = data['RENT_AREA'].apply(lambda x: math.trunc(x / 3.3058))
    data.columns = ['계약일', '전월세 구분', '임대면적(평)', '보증금(만원)', '임대료(만원)', '건축년도', '주소']
    data = data[['계약일', '주소', '보증금(만원)', '임대료(만원)', '임대면적(평)', '건축년도', '전월세 구분']]
    data = data.reset_index(drop=True)
    data.index = data.index+1
    st.write(data)

    t1, t2 = st.tabs(['전세 월평균 그래프', '월세 월평균 그래프'])
    j_m_mean = pd.read_csv('data/gu_j_m_mean.csv', encoding='cp949')
    w_m_mean = pd.read_csv('data/gu_w_m_mean.csv', encoding='cp949')

    gu = np.array(j_m_mean['SGG_NM'].unique())

    with t1:
        c1 = st.checkbox('전세 월평균 그래프', True)
        
        fig = go.Figure()
        dic = {}
        if c1:
            fig = px.scatter(width=700)
            for i in gu:
                dic.update({i : j_m_mean[j_m_mean['SGG_NM']==i]['RENT_GTN']})
            
            for j in gu:
                df = j_m_mean[j_m_mean['SGG_NM']==j]
                fig.add_scatter(x=df['YM'], y=df['RENT_GTN'], name=j)
            fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')
            st.plotly_chart(fig)

        else:
            st.write(j_m_mean)

    with t2:
        c1, c2 = st.columns([1,1])
        s1 = c1.checkbox('보증금 월평균 그래프', True)
        s2 = c2.checkbox('월세 월평균 그래프', True)

        p1 = c1.empty()
        p2 = c2.empty()
        
        fig = go.Figure()
        dic = {}
        if s1:
            with p1.container():
                fig = px.scatter(width=350)
                for i in gu:
                    dic.update({i : w_m_mean[w_m_mean['SGG_NM']==i]['RENT_GTN']})
                
                for j in gu:
                    df = w_m_mean[w_m_mean['SGG_NM']==j]
                    fig.add_scatter(x=df['YM'], y=df['RENT_GTN'], name=j)
                fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')
                st.plotly_chart(fig)

        else:
            c1.write(j_m_mean)
            p1 = st.empty()

        if s2:
            with p2.container():
                fig = px.scatter(width=350)
                for i in gu:
                    dic.update({i : w_m_mean[w_m_mean['SGG_NM']==i]['RENT_GTN']})
                
                for j in gu:
                    df = w_m_mean[w_m_mean['SGG_NM']==j]
                    
                    fig.add_scatter(x=df['YM'], y=df['RENT_FEE'], name=j)
                fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(만원)')
                st.plotly_chart(fig)
        else:
            c2.write(w_m_mean)
            p2 = st.empty()
        


    # 실거래 수 지역 순위
    col1, col2 = st.columns(2)
    # 월세 실거래 수 지역 순위
    with col1:
        st.subheader('월세 실거래 수 지역 순위')
        # 월세인 데이터 추출
        data_m = data2[data2['RENT_GBN']=='월세']
        # 구, 동 합치기
        cols = ['SGG_NM', 'BJDONG_NM']
        data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
        # 같은 구, 동 카운트
        data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
        #인덱스 재지정
        data_addr = data_addr.reset_index(drop=True)
        data_addr.index = data_addr.index+1

        # 그래프
        c1 = st.checkbox('월세 실거래 수 지역 순위 그래프', True)
        fig = go.Figure()
        if c1:
            fig = px.bar(x=data_addr.head(10)['주소'], y=data_addr.head(10)['거래 수'], width=350,
                        color=data_addr.head(10)['주소'])
            fig.update_layout(xaxis_title='지역 동', yaxis_title='보증금(만원)')
            st.plotly_chart(fig)
        else:
            # 데이터
            st.write(data_addr.head(10))

    # 전세 실거래 수 지역 순위(월세와 같은 방식)
    with col2:
        st.subheader('전세 실거래 수 지역 순위')
        data_m = data2[data2['RENT_GBN']=='전세']
        cols = ['SGG_NM', 'BJDONG_NM']
        data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
        data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
        data_addr = data_addr.reset_index(drop=True)
        data_addr.index = data_addr.index+1
        # 그래프
        c1 = st.checkbox('전세 실거래 수 지역 순위 그래프', True)
        fig = go.Figure()
        if c1:
            fig = px.bar(x=data_addr.head(10)['주소'], y=data_addr.head(10)['거래 수'], width=350,
                        color=data_addr.head(10)['주소'])
            fig.update_layout(xaxis_title='지역 동', yaxis_title='보증금(만원)')
            st.plotly_chart(fig)
        else:
            # 데이터
            st.write(data_addr.head(10))

# 전월세 검색 탭
elif selected3 == "🔎전월세 검색":
    run_search()

# 전세 시세 예측 탭 
elif selected3 == "📊전세 예측":
    run_predict()

# 건의사항 탭
elif selected3 == "💬건의사항":
    run_suggestions()
else:
    selected3 == "🏠Home"
