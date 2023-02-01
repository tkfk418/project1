import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

st.title('방방콕콕')

from search import run_search
from predict import run_predict
from suggestions import run_suggestions

selected3 = option_menu(None, ["🏠Home", "🔎전월세 검색",  "📊전세 시세 예측", '💬건의사항'], 
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
    st.subheader('가장 HOT한 동네는 어디?')
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    # st.write(data.head())
    # st.dataframe(data, 200, 100)
    # st.write(data.columns)
    # st.write(data.shape)
    # df_sample = data.loc[0:10, 'SGG_CD', 'FLR_NO', 'CNTRCT_DE']
    # st.dataframe(df_sample)
    # st.write(df_sample['지역구'].unique())
    # df_sample_value.columns = ['a']
    # list1 = df_sample['행정동'].tolist()
    # st.write(df_sample)


    df_sample = data[['SGG_NM', 'BJDONG_NM']]   
    df_sample.columns = ['지역구','행정동']
    st.write(df_sample['행정동'].unique())    
    
    df_sample_value = pd.Series(df_sample.value_counts()).to_frame()
    st.write(df_sample_value.head())

    st.write('top 5 지역은')
    st.write()
    
    
    
    
    



    # st.write(df_sample.value_counts())
    # st.write('count = f'{df_sample['행정동'].count()}'')
    # f'{df_sample['행정동'].count()}
   


# 전월세 검색 탭
elif selected3 == "🔎전월세 검색":
    run_search()

# 전세 시세 예측 탭 
elif selected3 == "📊전세 시세 예측":
    run_predict()

# 건의사항 탭
elif selected3 == "💬건의사항":
    run_suggestions()
else:
    selected3 == "🏠Home"